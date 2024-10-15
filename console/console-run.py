# This is just a simple UI to show how to walk through a text based app
# for interacting with the Movie API. It is not a complete implementation.
import os
import platform

class Term:
    '''
    This class contains methods for displaying text in different colors
    '''
    # ANSI escape codes for colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'  # Reset to default color

    @classmethod
    def red(cls, text):
        return cls.RED + text + cls.RESET

    @classmethod
    def green(cls, text):
        return cls.GREEN + text + cls.RESET

    @classmethod
    def yellow(cls, text):
        return cls.YELLOW + text + cls.RESET

    @classmethod
    def blue(cls, text):
        return cls.BLUE + text + cls.RESET

    @classmethod
    def magenta(cls, text):
        return cls.MAGENTA + text + cls.RESET
    
    @classmethod
    def clear(cls):
        # Check the current operating system
        if platform.system() == "Windows":
            os.system('cls')  # Windows uses 'cls' to clear the screen
        else:
            os.system('clear')  # Linux and macOS use 'clear' to clear the screen

def todo(txt):
    print(Term.blue(f"TODO: {txt}"))
    
def main_menu():
    while True:
        Term.clear()
        print("Welcome to the playlist creator!")
        print(Term.green("1) Work with users"))
        print(Term.green("2) Work with ratings"))
        print(Term.green("3) Work with movies"))
        print(Term.green("4) Exit"))
        choice = input("Enter your choice: ")
        if choice == '1':
            manage_users()
        elif choice == '2':
            manage_ratings()
        elif choice == '3':
            manage_movies()
        elif choice == '4':
            print(Term.blue("Goodbye!"))
            break
        else:
            print(Term.red("Invalid choice!"))

def manage_users():
    pass

def manage_ratings():
    pass

def manage_movies():
    pass

if __name__ == '__main__':
    main_menu()