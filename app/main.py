import sys
import subprocess
import os
from os import chdir, getcwd
from sys import executable
from typing import Optional
from os.path import expanduser
from subprocess import call

def locate_executable(command) -> Optional[str]:
    path = os.environ.get("PATH", "")
    for directory in path.split(":"):
        file_path = os.path.join(directory, command)
        if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
            return file_path
    return None

def main():
    commands = {"exit", "echo", "type","pwd"}
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        comm = input()
        command = comm.split()

        match command[0]:
            case "exit":
                if command[1] == "0":
                    sys.exit(0)
            case "echo":
                print(" ".join(command[1:]))
            case "type":
                if command[1] in commands:
                    print(f"{command[1]} is a shell builtin")
                else:
                    paths = os.getenv("PATH").split(":")
                    # print(paths)
                    for path in paths:
                        path_to_command = f"{path}/{command[1]}"
                        # print(path_to_command)
                        if os.path.exists(path_to_command):
                            print(f"{command[1]} is {path_to_command}")
                            break
                    else:
                        print(f"{command[1]}: not found")
            case "pwd":
                print(f"{os.getcwd()}")
            case "cd":
                if len(command) > 1 and command[1] != '~' :
                    try:
                        os.chdir(" ".join(command[1:]))
                    except FileNotFoundError:
                        print(command[0]+ ": " + command[1] + ": No such file or directory")
                else:
                    os.chdir(os.path.expanduser("~"))
            case _:
                executable = locate_executable(command[0])
                if executable:
                    try:
                        subprocess.run([executable] + command[1:], check=True)
                    except subprocess.CalledProcessError as e:
                        print(f"{command[0]}: command failed with error code {e.returncode}")
                else:
                    print(f"{command[0]}: command not found")
if __name__ == "__main__":
    main()




# safs