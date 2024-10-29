import sys


def main():
    # Uncomment this block to pass the first stage

    valid_commands = ['exit 0', 'echo']

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()

        if command == 'exit 0':
            sys.exit(0)
        elif command.startswith('echo'):
            message = command[4:]
            print("1!!!!!!" + command)
            print("2!!!!!!" + message)
            sys.stdout.write(f"{message}")
            sys.stdout.flush()
        elif command not in valid_commands:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.flush()
            continue



if __name__ == "__main__":
    main()
