import os
import importlib

class CommandModule:
    def execute(self, cmd):
        pass

modules_dir = "modules"
autorun_dir = os.path.join(modules_dir, "autorun")

modules = [module[:-3] for module in os.listdir(modules_dir) if module.endswith(".py") and module[:-3] != "__init__"]
autorun_modules = [module[:-3] for module in os.listdir(autorun_dir) if module.endswith(".py")]

all_modules = modules + ["autorun\\" + module for module in autorun_modules]

module_objects = {}

for module_name in modules:
    try:
        module_path = f"{modules_dir}.{module_name}"
        file_path = os.path.join(modules_dir, f"{module_name}.py")
        print(f"Attempting to load module: {file_path}")

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        
        module_objects[module_name] = module
    except ModuleNotFoundError as e:
        print(f"Error importing module {module_name}: {e}")


for module_name in autorun_modules:
    try:
        module_path = f"{modules_dir}.autorun.{module_name}"
        file_path = os.path.join(autorun_dir, f"{module_name}.py")

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        
        module_objects[module_name] = module
    except ModuleNotFoundError as e:
        print(f"Error importing autorun module {module_name}: {e}")

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
