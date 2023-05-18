from ._globalImports import *


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def notImplemented(isOkay=False):
    """
    Print a message saying that the function is not implemented yet or raise an error.
    :param isOkay: If True, the function will not raise an error
    :return: None
    """
    if isOkay:
        colorfulPrint("Not implemented yet", bcolors.FAIL)
        return
    raise NotImplementedError


def colorfulPrint(text, color, **kwargs):
    """
    Print text with color.
    :param text: The text to print
    :param color: The color to print with
    :param kwargs: Any other arguments to pass to print
    :return: None
    """
    print(color + text + bcolors.ENDC, **kwargs)