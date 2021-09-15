class Colors:
    reset = '\033[0m'
    bold = '\033[01m'
    underline = '\033[04m'

    class Fg:
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        lightRed = '\033[91m'
        lightGreen = '\033[92m'
        yellow = '\033[93m'
        lightBlue = '\033[94m'
        pink = '\033[95m'
        lightCyan = '\033[96m'


def bio():
    print(f"My name is {Colors.Fg.blue}Keegan Lenz{Colors.reset}")
    print(f"I am {Colors.bold}{Colors.Fg.yellow}18{Colors.reset} years old")
    print(f"My address is: {Colors.underline}917 North Chapel Hill, Clovis CA{Colors.reset}", '\n')
    print(f"I am taking this class because I am {Colors.Fg.pink}Passionate{Colors.reset} about "
          f"{Colors.Fg.green}Programming{Colors.reset} and want to further my knowledge in "
          f"{Colors.Fg.lightGreen}Computer Science{Colors.reset}.")
    print(f"Although I have no experience in Python, I do have experience in other languages, such as "
          f"{Colors.Fg.orange}Javascript{Colors.reset} and {Colors.Fg.orange}Lua{Colors.reset}.")
    print(f"I also have experience in {Colors.Fg.lightCyan}Web Design{Colors.reset} and "
          f"{Colors.Fg.purple}Game Development{Colors.reset}.")
    print(f"I look forward to learning about {Colors.Fg.lightRed}Python{Colors.reset} as it is a very popular language"
          f"and a great language to know for {Colors.Fg.lightBlue}Future Endeavours{Colors.reset}.")


bio()
