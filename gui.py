import sys, os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from hostFileClass import *


class MainWindow(QMainWindow):
    
    """This is the main window for the host file redirector """

    def __init__(self):
        
        super().__init__()
        
        self.setWindowTitle("Windows Host File Redirect")
        self.resize(350,80)

        self.initial_layout()
        #self.showHostFile()
    def showHostFile(self):
        pass
            
    def initial_layout(self):
        self.hostLabel = QLabel("Redirect to")
        self.hostLineEdit = QLineEdit()
        self.host2Label = QLabel("Redirect from")
        self.host2LineEdit = QLineEdit()

        self.updateButton = QPushButton("Add")
        
        self.layout1 = QHBoxLayout()
        self.layout1.addWidget(self.hostLabel)
        self.layout1.addWidget(self.hostLineEdit)

        self.layout2 = QHBoxLayout()
        self.layout2.addWidget(self.host2Label)
        self.layout2.addWidget(self.host2LineEdit)

        self.row1Widget = QWidget()
        self.row1Widget.setLayout(self.layout1)

        self.row2Widget = QWidget()
        self.row2Widget.setLayout(self.layout2)





        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.row1Widget)
        self.mainLayout.addWidget(self.row2Widget)
        self.mainLayout.addWidget(self.updateButton)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)

        self.setCentralWidget(self.mainWidget)
    
def getAdmin():
    import win32com.shell.shell as shell

    ASADMIN = 'asadmin'

    if sys.argv[-1] != ASADMIN:
        
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
        shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
if __name__ == "__main__":
    import subprocess as sp
    programName = "notepad.exe"
    fileName = "C:\Windows\System32\drivers\etc\hosts"
    sp.Popen([programName, fileName])
    app =  QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    #get admin privalleges from the user.
    getAdmin()

    app.exec_()
    
