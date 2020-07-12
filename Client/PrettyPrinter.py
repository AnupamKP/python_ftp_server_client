class PrettyPrinter:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

    def out_blue(self, line):
        return "{}{}{}".format(self.BLUE,line, self.ENDC)

    def out_green(self, line):
        return "{}{}{}".format(self.GREEN,line, self.ENDC)

    def out_red(self, line):
        return "{}{}{}".format(self.RED,line, self.ENDC)

    def out_yellow(self, line):
        return "{}{}{}".format(self.YELLOW,line,self.ENDC)
