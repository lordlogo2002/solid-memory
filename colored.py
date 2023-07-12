from typing import Any
from colorama import Fore

class MetaColor(type):
    use_color = True

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

    def __getattribute__(cls, name):
        if name == 'use_color' or cls.use_color:
            return type.__getattribute__(cls, name)
        return ""

class Color(metaclass=MetaColor):
    title = Fore.GREEN
    normal_text = Fore.CYAN
    info_text = Fore.LIGHTMAGENTA_EX
    prompt = Fore.MAGENTA
    user_input = Fore.YELLOW
    error_message = Fore.RED
    reset = Fore.RESET

reset_color = lambda: print(Color.reset, end="\r")

def parse_colors(text:str) -> str:
    """
        go trough the text and add color codes
        colors can be changed in colored.Color:
         - %t for title
         - %n for normal_text
         - %i for info_text
         - %ui for user_input
         - %e for error_message
    """
    text = text.replace("%t", Color.title)
    text = text.replace("%n", Color.normal_text)
    text = text.replace("%i", Color.info_text)
    text = text.replace("%ui", Color.user_input)
    text = text.replace("%e", Color.error_message)

    return text

def colored_print(text:str) -> None:
    """
        print the text colored and reset it afterwards.
        color codes:
         - %t for title
         - %n for normal_text
         - %i for info_text
         - %ui for user_input
         - %e for error_message
    """
    text = parse_colors(text)
    print(text)
    reset_color()

def error_message(message:str) -> None:
    """
        shows an error but also checks for color codes
        color codes:
         - %t for title
         - %n for normal_text
         - %i for info_text
         - %ui for user_input
         - %e for error_message
    """
    message = parse_colors(message)
    print(Color.error_message+message)
    reset_color()

def colored_input(prompt:str) -> str:
    """
        asks for input with the given prompt,
        and resets the colors after input
        color codes:
         - %t for title
         - %n for normal_text
         - %i for info_text
         - %ui for user_input
         - %e for error_message
    """
    prompt = parse_colors(prompt)
    value = input(Color.prompt+prompt+Color.user_input)
    reset_color()
    return value

def run_colored(func):
    try:
        Color.use_color = True
        func()
    finally:
        reset_color()
