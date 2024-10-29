import sys
import re
import os

def main():
    # Uncomment this block to pass the first stage

    valid_commands = ['exit 0', 'echo', 'exit', 'type']
    PATH = os.environ.get("PATH")
    # print("PPPAAATTTHHH     : "+ PATH)
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()
        # comm = command[5:]
        # print("!!!!!    " + comm)

        if command.startswith('type'):
            comm = command[5:]
            comm_path = None
            paths = PATH.split(':')
            print(paths)
            for path in paths:
                if os.path.isfile(f"{path}/{comm}"):
                    comm_path = f"{path}/{comm}"

            if comm in valid_commands:
                sys.stdout.write(f"{comm} is a shell builtin\n")
            elif comm_path:
                sys.stdout.write(f"{comm} is {comm_path}\n")
            else:
                sys.stdout.write(f"{comm}: not found\n")
        elif command == 'exit 0':
            sys.exit(0)
        elif command.startswith('echo'):
            message = command[5:]
            # print("1!!!!!!" + command)
            # print("2!!!!!!" + message)
            sys.stdout.write(f"{message}\n")
            sys.stdout.flush()
        elif command not in valid_commands:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.flush()
            continue



if __name__ == "__main__":
    main()
