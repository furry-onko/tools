def color(text: str, color: str) -> str:
    if color == "red":
        return f"\033[91m{text}\033[0m"
    elif color == "green":
        return f"\033[92m{text}\033[0m"
    elif color == "yellow":
        return f"\033[93m{text}\033[0m"
    elif color == "blue":
        return f"\033[94m{text}\033[0m"
    elif color == "purple":
        return f"\033[95m{text}\033[0m"
    elif color == "cyan":
        return f"\033[96m{text}\033[0m"
    elif color == "white":
        return f"\033[97m{text}\033[0m"
    else:
        return text

def style(text: str, style: str) -> str:
    if style == "bold":
        return f"\033[1m{text}\033[0m"
    elif style == "underline":
        return f"\033[4m{text}\033[0m"
    elif style == "reverse":
        return f"\033[7m{text}\033[0m"
    elif style == "blink":
        return f"\033[5m{text}\033[0m"
    else:
        return text

def Insert() -> None;
    while True:
        cmd_input: str|int = input(color(">>", "green"))
        cmd: list = cmd_input.split(" ")


        if cmd == []:
            print("", end="\r")

        else:
            print(color(f"Command {cmd[0]} is not recognized as Termux command", "red"))
def main():
    print(color("Termux ", "purple"), end="")
    print(color("v1.0.0", "cyan"))
    print(style(color("By: Onko Aikuu (@furry_onko)", "blue"), "bold"))
    Insert()