import os
import sys
import colors as c

def Insert() -> None:
    while True:
        cmd_input: str|int = input(c.color(">>", "green"))
        cmd: list = cmd_input.lower().split(" ")

        if not cmd[:]:
            print("", end="\r")

        if cmd[0] in ["exit", "quit", "#"]:
            if len(cmd) > 1 and cmd[1].isdigit():
                exit(int(cmd[1]))

            else:
                exit(0)
        
        if cmd[0] in ["clear", "cl", "~"]:
            print("\033[H\033[J", end="")
            continue
        
        if cmd[0] == "calc":
            if cmd[1].isdigit() and cmd[2].isdigit() and len(cmd) == 4:
                if cmd[3] == 'add':
                    result: float = float(cmd[1]) + float(cmd[2])
                    print(c.color("Sum of", "yellow"), end=" ")
                    print(c.style(c.color(cmd[1], "blue"), "underline"), end=" ")
                    print(c.color("and", "yellow"), end=" ")
                    print(c.style(c.color(cmd[2], "blue"), "underline"), end=" ")
                    print(c.color("is", "yellow"), end=" ")
                    print(c.style(c.color(float(result), "blue"), "underline"))

                if cmd[3] == "sub":
                    result: float = float(cmd[1]) - float(cmd[2])
                    print(c.color("Subtraction of", "yellow"), end=" ")
                    print(c.style(c.color(cmd[1], "blue"), "underline"), end=" ")
                    print(c.color("and", "yellow"), end=" ")
                    print(c.style(c.color(cmd[2], "blue"), "underline"), end=" ")
                    print(c.color("is", "yellow"), end=" ")
                    print(c.style(c.color(float(result), "blue"), "underline"))
                
                if cmd[3] == "mul":
                    result: float = float(cmd[1]) * float(cmd[2])
                    print(c.color("Multiplication of", "yellow"), end=" ")
                    print(c.style(c.color(cmd[1], "blue"), "underline"), end=" ")
                    print(c.color("and", "yellow"), end=" ")
                    print(c.style(c.color(cmd[2], "blue"), "underline"), end=" ")
                    print(c.color("is", "yellow"), end=" ")
                    print(c.style(c.color(float(result), "blue"), "underline"))
                
                if cmd[3] == "div":
                    if cmd[2] != 0:
                        result: float = float(cmd[1]) / float(cmd[2])
                        print(c.color("Division of", "yellow"), end=" ")
                        print(c.style(c.color(cmd[1], "blue"), "underline"), end=" ")
                        print(c.color("and", "yellow"), end=" ")
                        print(c.style(c.color(cmd[2], "blue"), "underline"), end=" ")
                        print(c.color("is", "yellow"), end=" ")
                        print(c.style(c.color(float(result), "blue"), "underline"))
                    else:
                        print(c.color("Division by zero is not allowed", "red"))

                if cmd[3] == "pwr":
                    result: float = float(cmd[1]) ** float(cmd[2])
                    print(c.color("Power of", "yellow"), end=" ")
                    print(c.style(c.color(cmd[1], "blue"), "underline"), end=" ")
                    print(c.color("and", "yellow"), end=" ")
                    print(c.style(c.color(cmd[2], "blue"), "underline"), end=" ")
                    print(c.color("is", "yellow"), end=" ")
                    print(c.style(c.color(float(result), "blue"), "underline"))
                
                if cmd[3] == "sqr":
                    result: float = float(cmd[1]) ** 0.5
                    print(c.color("Square root of", "yellow"), end=" ")
                    print(c.style(c.color(cmd[1], "blue"), "underline"), end=" ")
                    print(c.color("is", "yellow"), end=" ")
                    print(c.style(c.color(float(result), "blue"), "underline"))
            #     else:
            #         print(c.color("Command not recognized", "red"))
            # else:
            #     print(c.color("Invalid arguments", "red"))

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

            print(c.color("calc", "red"), end=" ")
            print(c.color("<number_1> <number_2>", "cyan"), end=" ")
            print(c.color("(add|sub|mul|div|pwr|sqr)", "cyan"), end=" ")
            print("Calculates two numbers together")

        # else:
        #     print(c.color(f"Command {cmd[0]} is not recognized as Termux command", "red"))

def main():
    print(c.color("Termux ", "purple"), end="")
    print(c.color("v1.0.0", "cyan"))
    print(c.style(c.color("By: Onko Aikuu (@furry_onko)", "blue"), "bold"))
    Insert()

main()