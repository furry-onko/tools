import os
import sys
import colors.py as c

def Insert() -> None;
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
            print(style(color("Commands:", "purple"), "bold"))
            print(style(color("Syntax:", "cyan"), "bold"))
            # <required_argument> [optional_argument] (option1|option2)
            print(color("required_command", ""))

        else:
            print(color(f"Command {cmd[0]} is not recognized as Termux command", "red"))

def main():
    print(color("Termux ", "purple"), end="")
    print(color("v1.0.0", "cyan"))
    print(style(color("By: Onko Aikuu (@furry_onko)", "blue"), "bold"))
    Insert()