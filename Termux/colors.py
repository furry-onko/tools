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
    elif style == "blink":
        return f"\033[5m{text}\033[0m"
    elif style == "dim":
        return f"\033[2m{text}\033[0m"
    elif style == "hidden":
        return f"\033[8m{text}\033[0m"
    elif style == "strikethrough":
        return f"\033[9m{text}\033[0m"
    elif style == "italic":
        return f"\033[3m{text}\033[0m"
    elif style == "light":
        return f"\033[37m{text}\033[0m"
    elif style == "dark":
        return f"\033[90m{text}\033[0m"
    else:
        return text

def debug_color_output():
    """Prints sample outputs for debugging terminal color support."""
    print("Testing colors:")
    print(color("This is red", "red"))
    print(color("This is green", "green"))
    print(color("This is yellow", "yellow"))
    print(color("This is blue", "blue"))
    print(color("This is purple", "purple"))
    print(color("This is cyan", "cyan"))
    print(color("This is white", "white"))
    print(color("This is black", "black"))
    print("\nTesting styles:")
    print(style("This is bold", "bold"))
    print(style("This is underline", "underline"))
    print(style("This is reverse", "reverse"))
    print(style("This is blink", "blink"))
    print(style("This is dim", "dim"))
    print(style("This is hidden", "hidden"))
    print(style("This is strikethrough", "strikethrough"))
    print(style("This is italic", "italic"))
    print(style("This is light", "light"))
    print(style("This is dark", "dark"))

# Uncomment the line below to test the output
debug_color_output()