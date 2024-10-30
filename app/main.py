import sys
import subprocess
import os
from os import chdir
from typing import Optional
from os.path import expanduser


def locate_executable(command) -> Optional[str]:
    path = os.environ.get("PATH", "")

    for directory in path.split(":"):
        file_path = os.path.join(directory, command)

        if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
            return file_path

def main():
    # Uncomment this block to pass the first stage

    valid_commands = ['exit 0', 'echo', 'exit', 'type','pwd','cd']
    PATH = os.environ.get("PATH")
    # print("PPPAAATTTHHH     : "+ PATH)
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()
        user_command , args = command.split(" ")
        comm = command[5:]



        if command.startswith('type'):
            comm_path = None
            paths = PATH.split(':')
            # print(paths)
            for path in paths:
                if os.path.isfile(f"{path}/{comm}"):
                    comm_path = f"{path}/{comm}"

            if comm in valid_commands:
                sys.stdout.write(f"{comm} is a shell builtin\n")
            elif comm_path:
                sys.stdout.write(f"{comm} is {comm_path}\n")
            else:
                if os.path.isfile(command.split(" ")[0]):
                    os.system(command)
                else:
                    sys.stdout.write(f"{comm}: not found\n")
        elif command == 'exit 0':
            sys.exit(0)
        elif user_command == 'pwd':
            sys.stdout.write(f"{os.getcwd()}\n")
        elif user_command == "cd":
            directory = command.split(" ")[1]
            # print("asdas    " + directory)
            try:
                # print("drr")
                chdir(expanduser(directory))
                # print("drr changed")
            except OSError:
                print(f"cd: {directory}: No such file or directory")



        elif command.startswith('echo'):
            message = command[5:]
            sys.stdout.write(f"{message}\n")
            sys.stdout.flush()
        elif executable := locate_executable(user_command):
            subprocess.run([executable, *args])
        else:
            sys.stdout.write(f"{command}: command not found\n")
        sys.stdout.flush()



if __name__ == "__main__":
    main()
