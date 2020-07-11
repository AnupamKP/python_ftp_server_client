from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from Server.Configurator import Configurator
import logging

logging.basicConfig(filename=Configurator.current_path + '/logs/server.log', level=logging.INFO)

class Server:
    def __init__(self, ip_addr, port):
        self.ip_addr = ip_addr
        self.port = port
        configs = Configurator().get_app_configs()
        self.user = configs['user']
        self.password = configs['password']
        self.dir = Configurator.current_path + "/" + configs['storage_dir']
        self.max_conn = configs['allow_max_conn']
        self.max_conn_per_ip = configs['max_conn_per_ip']

    def __init_server(self):
        authorizer = DummyAuthorizer()
        authorizer.add_user(self.user, self.password,
                            self.dir, perm='elradfmw')
        handler = FTPHandler
        handler.authorizer = authorizer

        address = (self.ip_addr, self.port)
        server = FTPServer(address, handler)

        server.max_cons = self.max_conn
        server.max_cons_per_ip = self.max_conn_per_ip

        return server

    def start_server(self):
        server = self.__init_server()
        server.serve_forever()
