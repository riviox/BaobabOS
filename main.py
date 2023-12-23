import os
import importlib

class CommandModule:
    def execute(self, cmd):
        pass

modules_dir = "modules"
modules = [module[:-3] for module in os.listdir(modules_dir) if module.endswith(".py") and module[:-3] != "__init__"]

module_objects = {}

for module_name in modules:
    module_path = f"{modules_dir}.{module_name}"
    module = importlib.import_module(module_path)
    module_class = getattr(module, module_name.capitalize())
    module_objects[module_name] = module_class()

while True:
    pwd = os.getcwd()
    prompt = f"{pwd} $ "
    cmd = input(prompt)

    cmd_parts = cmd.split()
    command = cmd_parts[0]

    if command in module_objects:
        module = module_objects[command]
        module.execute(cmd)
    else:
        print(f"Error: Command '{command}' not recognized.")
