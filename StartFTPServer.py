from Server.Server import Server


def start_ftp_Server():
    ftpserver = Server('0.0.0.0',2121) 
    ftpserver.start_server()

if __name__ == '__main__':
    start_ftp_Server()