import inspect
import os.path
import json

class Configurator:
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    current_path = os.path.dirname(os.path.abspath(filename))
    def __init__(self):
        self.conf_file_path = Configurator.current_path + '/configs/app.json'

    def __read_config(self):
        data = {}
        with open(self.conf_file_path) as file:
            data = json.load(file)

        return data

    def get_app_configs(self):
        return self.__read_config()
