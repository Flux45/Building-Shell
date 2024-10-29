import sys


def main():
    # Uncomment this block to pass the first stage

    valid_commands = ['exit 0', 'echo']

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()
        if command not in valid_commands:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.flush()
            continue
        elif command == 'exit 0':
            sys.exit(0)
        elif command == 'echo':
            message = command[4:]
            sys.stdout.write(f"{message}")
            sys.stdout.flush()



if __name__ == "__main__":
    main()
