import os
import sys
import colors as c

def Insert() -> None:
    while True:
        cmd_input: str|int = input(c.color(">>", "green"))
        cmd: list = cmd_input.split(" ")


        if not cmd[:]:
            print("", end="\r")

        if cmd[0] in ["exit", "quit", "#"]:
            if len(cmd) > 1 and cmd[1].isdigit():
                exit(int(cmd[1]))
                break
            else:
                exit(0)
        
        if cmd[0] in ["clear", "cl", "~"]:
            print("\033[H\033[J", end="")
            continue

        if cmd[0] in ["help", "?"]:
            print(c.style(c.color("Commands:", "purple"), "bold"))
            
            print(c.style(c.color("Syntax:", "cyan"), "bold"))
            print(c.color("required_command", "red"), end=" ")
            print(c.color("[optional_argument]", "yellow"), end=" ")
            print(c.color("<required_argument>", "green"), end=" ")
            print(c.color("(option1|option2)", "cyan"))

            print("-" * 50)

            print(c.color("(exit|quit|#)", "cyan"), end=" ")
            print(c.color("[exit_code]", "yellow"), end=" ")
            print("Quit the program")

            print(c.color("(clear|cls|~)", "cyan"), end=" ")
            print("Clear the screen")

            print(c.color("(help|?)", "cyan"), end=" ")
            print("Show this help message")

            print(c.color("!", "red"), end=" ")
            print(c.color("<command>", "green"), end=" ")
            print("Execute command as administrator")



        else:
            print(c.color(f"Command {cmd[0]} is not recognized as Termux command", "red"))

def main():
    print(c.color("Termux ", "purple"), end="")
    print(c.color("v1.0.0", "cyan"))
    print(c.style(c.color("By: Onko Aikuu (@furry_onko)", "blue"), "bold"))
    Insert()

main()