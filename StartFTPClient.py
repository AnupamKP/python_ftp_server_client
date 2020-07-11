from Client.Client import Client

def start_ftp_client():
    ftplient = Client('127.0.0.1',2121)
    ftplient.login('admin','admin')
    option = 'L'
    while(option != 'S'):
        if option == 'U':
            filename = input("Enter filename to upload: ")
            ftplient.upload_data(filename)
        elif option == 'D':
            filename = input("Enter filename to download: ")
            ftplient.download_data(filename)
        else:
            ftplient.list_data()
            print("")
        option = input("Enter U for upload , D for download and S to stop: ")
    ftplient.logout()

if __name__ == "__main__":
    start_ftp_client()