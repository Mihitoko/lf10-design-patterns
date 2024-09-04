class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[1;32m"
    NC = '\033[0m'
    LIGHT_BLACK = '\033[0;90m'
    CYAN = '\033[0;36m'
    YELLOW = '\033[0;33m'

    @staticmethod
    def color_string(text: str, color: str) -> str:
        return f"{color}{text}{Colors.NC}"
