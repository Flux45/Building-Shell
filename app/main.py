import sys


def main():
    # Uncomment this block to pass the first stage

    valid_commands = ['exit 0', 'echo', 'exit', 'type']

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()

        if command.startswith('type') in valid_commands:
            comm = command[5:]
            if comm in valid_commands:
                sys.stdout.write(f"{comm} is a shell builtin")
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
