import os
from modules.colors import Colors

class Ls:
    def execute(self, cmd):
        try:
            directory_path = cmd.split("ls ")[1].strip() if len(cmd.split("ls ")) > 1 else "."

            contents = os.listdir(directory_path)

            for item in contents:
                item_path = os.path.join(directory_path, item)
                item_type = "Folder" if os.path.isdir(item_path) else "File"

                color_code = Colors.BLUE if item_type == "Folder" else Colors.GREEN
                reset_code = Colors.RESET

                print(f"{color_code}{item}{reset_code}")

        except IndexError:
            print("Error: Please provide a valid directory path for 'ls'.")
        except FileNotFoundError:
            print("Error: The specified directory does not exist.")
        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}")