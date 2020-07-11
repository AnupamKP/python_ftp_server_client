from ftplib import FTP
import os,inspect
filename = inspect.getframeinfo(inspect.currentframe()).filename
current_path = os.path.dirname(os.path.abspath(filename))

class Client:
    def __init__(self,ip_addr,port):
        self.ip_addr = ip_addr
        self.port = port
        self.ftp = None
        self.client_storage = current_path + '/storage/'

    def login(self,user,password):
        self.ftp = FTP('')
        self.ftp.connect(self.ip_addr,self.port)
        self.ftp.login(user=user,passwd=password)
        self.ftp.cwd('')
    
    def logout(self):
        self.ftp.quit()
        self.ftp = None
    
    def check_auth(self):
        return True if self.ftp != None else False

    def list_data(self):
        if self.check_auth():
            self.ftp.retrlines('LIST')
        else:
            print("Unauthorized!!!!") 
    
    def upload_data(self,filename):
        if self.check_auth():
            self.ftp.storbinary('STOR '+ filename, open(self.client_storage +filename, 'rb'))
        else:
            print("Unauthorized!!!!")
    
    def download_data(self,filename):
        if self.check_auth():
            localfile = open(self.client_storage + filename, 'wb')
            self.ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
            localfile.close()
        else:
            print("Unauthorized!!!!")
    