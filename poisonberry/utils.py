from datetime import datetime

ERROR = 1
ALERT = 2
WARN = 3
INFO = 4
DEBUG = 5

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

logOutput = DEBUG
_logLevels = {ERROR: "ERROR", ALERT: "ALERT", WARN:"WARN", INFO: "INFO", DEBUG:"DEBUG"}

_levelMap = {ERROR: bcolors.FAIL + bcolors.UNDERLINE + bcolors.BOLD,
             ALERT: bcolors.WARNING + bcolors.UNDERLINE + bcolors.BOLD,
             WARN: bcolors.WARNING + bcolors.BOLD,
             INFO: bcolors.OKGREEN + bcolors.BOLD,
             DEBUG: bcolors.OKBLUE }

def log(level, msg):
    if level <= logOutput:
        print("[%s] - %s%s%s: %s" %
              ("{:%d/%m/%Y %H:%M:%S}".format(datetime.now()), _levelMap[level], _logLevels[level], bcolors.ENDC, msg))
