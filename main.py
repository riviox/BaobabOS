import os
import importlib

class CommandModule:
    def execute(self, cmd):
        pass

    @classmethod
    def get_instance(cls):
        return cls()

modules_dir = "modules"
autorun_dir = os.path.join(modules_dir, "autorun")

module_objects = {}

def load_module(module_name, file_path):
    try:
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module
    except ModuleNotFoundError as e:
        print(f"Error importing module {module_name}: {e}")
        return None

def load_modules(directory):
    modules = {}
    for module_name in os.listdir(directory):
        if module_name.endswith(".py") and module_name[:-3] != "__init__":
            file_path = os.path.join(directory, module_name)

            module = load_module(module_name, file_path)
            if module:
                modules[module_name[:-3].lower()] = module  # Convert to lowercase
                print(f"Module {module_name[:-3]} loaded successfully with classes: {dir(module)}")

    return modules


module_objects.update(load_modules(modules_dir))
module_objects.update(load_modules(autorun_dir))

print("Loaded Modules:", list(module_objects.keys()))

while True:
    pwd = os.getcwd()
    prompt = f"{pwd} $ "
    cmd = input(prompt)

    cmd_parts = cmd.split()
    command = cmd_parts[0].lower()

    if command in module_objects:
        module_class = getattr(module_objects[command], 'CommandModule', None)
        if module_class and issubclass(module_class, CommandModule):
            module_instance = module_class.get_instance()
            module_instance.execute(cmd)
        else:
            print(f"Error: Module {command} is not a valid command.")
    else:
        print(f"Error: Command '{command}' not recognized.")
