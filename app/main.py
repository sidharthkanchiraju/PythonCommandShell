import sys
import os

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")
    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        sys.stdout.flush()

        shell_commands = ["exit", "echo", "type"]

        # Wait for user input
        cmd = input()
        if cmd.split(" ")[0] in shell_commands:
            if cmd.startswith("exit"):
                code = cmd[len("exit "):]
                try:
                    return int(code)
                except:
                    return 0
            elif cmd.startswith("echo"):
                text = cmd[len("echo "):]
                sys.stdout.write(text + "\n")
            elif cmd.startswith("type"):
                if cmd[len('type '):] in shell_commands:
                    sys.stdout.write(f"{cmd[len('type '):]} is a shell builtin\n")
                    continue
                path = os.popen("echo $PATH").read().strip("\n")
                dirs = path.split(":")
                response = f"{cmd[len('type '):]}: not found\n"
                for dir in dirs:
                    try:
                        if cmd[len('type '):] in os.listdir(dir):
                            response = f"{cmd[len('type '):]} is {dir}/{cmd[len('type '):]}\n"
                    except:
                        continue
                sys.stdout.write(response)
        else:
            response = f"{cmd.split(' ')[0]}: command not found"
            # for dir in os.popen("echo $PATH").read().strip("\n").split(":"):
            #     try:
            #         if cmd.split(" ")[0] in os.listdir(dir):
            #             response = os.popen(f".{dir}/{cmd.split(' ')[0]}.sh").read().strip("\n")
            #     except:
            #         continue
            path = os.popen("echo $PATH").read().strip("\n")
            dirs = path.split(":")
            for dir in dirs:
                if cmd.split(" ")[0] in os.listdir(dir):
                    # os.system(cmd)
                    response = os.popen(cmd).read().strip("\n")
            if response.startswith("/bin/sh: "):
                response = f"{cmd}: command not found"
            
            print(response)

if __name__ == "__main__":
    main()
