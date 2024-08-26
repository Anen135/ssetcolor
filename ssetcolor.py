def black(text):
    return("\033[30m{}\033[0m".format(text)).lstrip()
def gray(text):
    return("\033[90m{}\033[0m".format(text)).lstrip()
def red(text):
    return("\033[31m{}\033[0m".format(text)).lstrip()
def green(text):
    return("\033[32m{}\033[0m".format(text)).lstrip()
def amber(text):
    return("\033[33m{}\033[0m".format(text)).lstrip()
def blue(text):
    return("\033[34m{}\033[0m".format(text)).lstrip()
def violet(text):
    return("\033[35m{}\033[0m".format(text)).lstrip()
def cyan(text):
    return("\033[36m{}\033[0m".format(text)).lstrip()
def yellow(text):
    return("\033[33m{}\033[0m".format(text)).lstrip()
def orange(text):
    return("\x1b[38;5;208m{}\x1b[0m".format(text)).lstrip()
def white(text):
    return("\033[37m{}\033[0m".format(text)).lstrip()
def bold(text):
    return("\033[1m{}\033[0m".format(text)).lstrip()
def UNDERLINE(text):
    return("\033[4m{}\033[0m".format(text)).lstrip()