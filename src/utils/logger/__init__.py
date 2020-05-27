import sys
from utils import cls


class Logger:

    def __init__(self):
        cls()
        self.RED = "\033[1;31;10m"
        self.GRN = "\033[1;32;10m"
        self.YLW = "\033[1;32;10m"
        self.GRY_BLD = "\033[1;30;2m"
        self.WHT_BLD = "\033[1;37;2m"

        self.END_COLOR = "\033[0m"

    def log(self, process, message):
        print(f"{self.GRN} LOG {self.END_COLOR}")
        print(f'{self.GRY_BLD}----------------------------------{self.END_COLOR}\n')
        print(f"{self.GRN}{process}{self.END_COLOR}")
        print(f'{self.GRY_BLD}----------------------------------{self.END_COLOR}\n')
        print(f"{self.GRY_BLD}status: {self.END_COLOR}{self.GRN} OK{self.END_COLOR}")
        print(f"{self.GRY_BLD}message:{self.END_COLOR} {message}")
        print(f'{self.GRY_BLD}----------------------------------{self.END_COLOR}\n')

    def warn(self, process, message):
        print(
            f"||  STATUS == WARN  || :: {self.GRY}{process}{self.END_COLOR}\nmessage: {message}\n")

    def error(self, process, message):
        print(
            f"||  STATUS == ERROR  || :: {self.GRY}{process}{self.END_COLOR}\nmessage {message}\n")
