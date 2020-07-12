from Client.PrettyPrinter import PrettyPrinter


class ClientCLI:
    def __init__(self, ftpclient):
        self.ftpclient = ftpclient
        self.pprint = PrettyPrinter()

    def __call_upload(self):
        filename = input(self.pprint.out_blue("Enter filename to upload: "))
        try:
            self.ftpclient.upload_data(filename)
            print(self.pprint.out_green("Download Complete!"))
        except:
            print(self.pprint.out_red("Download Failed...Try again!"))

    def __call_download(self):
        filename = input(self.pprint.out_blue("Enter filename to download: "))
        try:
            self.ftpclient.download_data(filename)
            print(self.pprint.out_green("Download Complete!"))
        except:
            print(self.pprint.out_red("Download Failed...Try again!"))

    def __call_list(self):
        try:
            self.ftpclient.list_data()
        except:
            print(self.pprint.out_red("Connection Unavailable. Login again!"))

    def __call_client_list(self):
        try:
            self.ftpclient.list_client_storage()
        except:
            print(self.pprint.out_red("You have no read Permission!"))

    def start_client_cli(self):
        option = None
        while(option != 'S'):
            option = input(self.pprint.out_blue(
                "Enter L to list files in server, CL to list files in client storage, U for upload, D for download and S to stop: "))
            if option == 'U':
                self.__call_upload()
            elif option == 'D':
                self.__call_download()
            elif option == 'L':
                self.__call_list()
            elif option == 'S':
                print(self.pprint.out_yellow("Process Complete!"))
                exit()
            elif option == 'CL':
                self.__call_client_list()
            else:
                print(self.pprint.out_yellow(
                    "Option not available. Try again!"))
            print("")
