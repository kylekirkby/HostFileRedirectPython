import os
import sys
import win32com.shell.shell as shell

class HostFile:

    """This class interfaces with the host file in windows.
    also manage your redirects and host file rules"""

    def __init__(self):

        self.hostFilePath = "C:\\Windows\\System32\\drivers\\etc\\hosts"
        self.ASADMIN = "asadmin"
        self.data = []


        #run core methods

        self.getHostFileData()

        print(self.data)


    def addRedirect(self):
       pass 

    def getHostFileData(self):
        
        with open(self.hostFilePath,mode="r") as hostFile:

            for line in hostFile:
                
                self.data.append(line)

        return self.data

                

if __name__ == "__main__":

    hf = HostFile()
