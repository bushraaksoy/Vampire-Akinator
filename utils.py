import sys, time

class Color:
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'  # Reset to default color and formatting


def print_color(text, color):
    print(color + text + Color.RESET)
    # Example usage: print_color("This is red text", Color.RED)


def typewriter(str, color):
    for char in str: 
        print(colored(char, color), end='') 
        sys.stdout.flush() 
        time.sleep(0.03) 


def colored(str, color):
    return color + str + Color.RESET
