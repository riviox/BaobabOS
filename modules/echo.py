class Echo():
    def execute(self, cmd):
        a = cmd.split("echo ")[1]
        print(a)