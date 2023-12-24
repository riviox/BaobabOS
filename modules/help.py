class Help():
    def execute(self, cmd):
        help = {
            "ls": "lists directory",
            "echo": "prints text",
            "help": "displays help"
        }
        print(help)