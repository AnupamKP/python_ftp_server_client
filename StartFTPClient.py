from Client.Client import Client
from Client.ClientCLI import ClientCLI

def start_ftp_client():
    ftpclient = Client('127.0.0.1', 2121)
    ftpclient.login('admin', 'admin')
    CLI = ClientCLI(ftpclient)
    CLI.start_client_cli()
    ftpclient.logout()


if __name__ == "__main__":
    start_ftp_client()