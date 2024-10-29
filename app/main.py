import sys


def main():
    # Uncomment this block to pass the first stage

    valid_commands = []

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()
        if command not in valid_commands:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.flush()
            continue



if __name__ == "__main__":
    main()
