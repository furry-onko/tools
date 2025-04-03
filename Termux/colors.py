from colorama import init

# Initialize colorama to enable ANSI escape codes on all platforms
init()

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
    elif color == "black":
        return f"\033[90m{text}\033[0m"
    else:
        return text

def background(text: str, color: str) -> str:
    if color == "red":
        return f"\033[41m{text}\033[0m"
    elif color == "green":
        return f"\033[42m{text}\033[0m"
    elif color == "yellow":
        return f"\033[43m{text}\033[0m"
    elif color == "blue":
        return f"\033[44m{text}\033[0m"
    elif color == "purple":
        return f"\033[45m{text}\033[0m"
    elif color == "cyan":
        return f"\033[46m{text}\033[0m"
    elif color == "white":
        return f"\033[47m{text}\033[0m"
    elif color == "black":
        return f"\033[40m{text}\033[0m"
    else:
        return text

def style(text: str, style: str) -> str:
    if style == "bold":
        return f"\033[1m{text}\033[0m"
    elif style == "underline":
        return f"\033[4m{text}\033[0m"
    elif style == "reverse":
        return f"\033[7m{text}\033[0m"
    elif style == "dark":
        return f"\033[90m{text}\033[0m"
    else:
        return text