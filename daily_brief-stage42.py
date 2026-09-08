# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: DailyBrief
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    HIDDEN = "\033[8m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    FG_BLACK = "\033[30m"
    FG_RED = "\033[31m"
    FG_GREEN = "\033[32m"
    FG_YELLOW = "\033[33m"
    FG_BLUE = "\033[34m"
    FG_MAGENTA = "\033[35m"
    FG_CYAN = "\033[36m"
    FG_WHITE = "\033[37m"

    @staticmethod
    def colorize(text, color):
        if not Color.enabled:
            return text
        return f"{color}{text}{Color.RESET}"

    @staticmethod
    def bold(text):
        return Color.colorize(text, Color.BOLD)

    @staticmethod
    def dim(text):
        return Color.colorize(text, Color.DIM)

    @staticmethod
    def underline(text):
        return Color.colorize(text, Color.UNDERLINE)

    @staticmethod
    def blink(text):
        return Color.colorize(text, Color.BLINK)

    @staticmethod
    def hidden(text):
        return Color.colorize(text, Color.HIDDEN)

    @staticmethod
    def bg(text, color):
        return Color.colorize(text, f"{Color.BG_BLACK}{color}{Color.RESET}")

    @staticmethod
    def fg(text, color):
        return Color.colorize(text, f"{color}{Color.RESET}")

    @staticmethod
    def set_enabled(enabled=True):
        Color.enabled = enabled
