import sys
import subprocess
import os
from os import chdir
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
                try:
                    os.chdir(" ".join(command[1:]))
                except FileNotFoundError:
                    print(command[0]+ ": " + command[1] + ": No such file or directory")
            case _:
                #         elif executable := locate_executable(user_command):
                #             subprocess.run([executable, *args])
                if executable := locate_executable(command[0]):
                    subprocess.run([command[0], command[1:]])
                else:
                    # print("i'm here")
                    print(f"${command[0]}: command not found")
if __name__ == "__main__":
    main()










# def locate_executable(command) -> Optional[str]:
#     path = os.environ.get("PATH", "")
#
#     for directory in path.split(":"):
#         file_path = os.path.join(directory, command)
#
#         if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
#             return file_path
#
#
# def main():
#     commands = {"exit", "echo", "type", "pwd"}
#     while True:
#         sys.stdout.write("$ ")
#         sys.stdout.flush()
#         # Wait for user input
#         comm = input()
#         command = comm.split()
#         user_command , args = comm.split(" ")
#         # if command[0] not in commands:
#         #     print(f"${command[0]}: command not found")
#         # elif command[0] == "exit" and command[1] == "0":
#         #     sys.exit(0)
#         # elif command[0] == "echo":
#         #     print(" ".join(command[1:]))
#         match command[0]:
#             case "exit":
#                 if command[1] == "0":
#                     sys.exit(0)
#             case "echo":
#                 print(" ".join(command[1:]))
#             case "type":
#                 if command[1] in commands:
#                     print(f"{command[1]} is a shell builtin")
#                 else:
#                     paths = os.getenv("PATH").split(":")
#                     # print(paths)
#                     for path in paths:
#                         path_to_command = f"{path}/{command[1]}"
#                         # print(path_to_command)
#                         if os.path.exists(path_to_command):
#                             print(f"{command[1]} is {path_to_command}")
#                             break
#                     else:
#                         print(f"{command[1]}: not found")
#             case "pwd":
#                 print(f"{os.getcwd()}")
#             case "cd":
#                 try:
#                     os.chdir(" ".join(command[1:]))
#                 except FileNotFoundError:
#                     print(command[0]+ ": " + command[1] + ": No such file or directory")
#             case _:
#                 if executable := locate_executable(user_command):
#                     subprocess.run([executable, args])
#                 else:
#                     # print("i'm here")
#                     print(f"${command[0]}: command not found")
# if __name__ == "__main__":
#     main()






# def main():
#     # Uncomment this block to pass the first stage
#
#     valid_commands = ['exit 0', 'echo', 'exit', 'type','pwd','cd']
#     PATH = os.environ.get("PATH")
#     # print("PPPAAATTTHHH     : "+ PATH)
#     while True:
#         sys.stdout.write("$ ")
#         sys.stdout.flush()
#         # Wait for user input
#         command = input()
#         user_command , args = command.split(" ")
#         comm = command[5:]
#
#
#
#         if command.startswith('type'):
#             comm_path = None
#             paths = PATH.split(':')
#             # print(paths)
#             for path in paths:
#                 if os.path.isfile(f"{path}/{comm}"):
#                     comm_path = f"{path}/{comm}"
#
#             if comm in valid_commands:
#                 sys.stdout.write(f"{comm} is a shell builtin\n")
#             elif comm_path:
#                 sys.stdout.write(f"{comm} is {comm_path}\n")
#             else:
#                 if os.path.isfile(command.split(" ")[0]):
#                     os.system(command)
#                 else:
#                     sys.stdout.write(f"{comm}: not found\n")
#         elif command == 'exit 0':
#             sys.exit(0)
#         elif user_command == 'pwd':
#             dir = os.getcwd()
#             sys.stdout.write(f"{dir}\n")
#         elif user_command == "cd":
#             directory = command.split(" ")[1]
#             # print("asdas    " + directory)
#             try:
#                 # print("drr")
#                 chdir((directory))
#                 # sys.stdout.write("CURRENT DIR:  " + os.getcwd() + "\n")
#                 # print("drr changed")
#             except OSError:
#                 sys.stdout.write(f"cd: {directory}: No such file or directory\n")
#
#
#         elif command.startswith("/"):
#             call("{} {}".format(command, " ".join(args)), shell=True)
#         elif command.startswith('echo'):
#             message = command[5:]
#             sys.stdout.write(f"{message}\n")
#             sys.stdout.flush()
#         elif executable := locate_executable(user_command):
#             subprocess.run([executable, *args])
#         else:
#             sys.stdout.write(f"{command}: command not found\n")
#         sys.stdout.flush()
#
#
#
# if __name__ == "__main__":
#     main()
