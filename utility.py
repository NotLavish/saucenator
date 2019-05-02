import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cwopy(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)
    
def anyKey():
    os.system('pause')

def lengthChecker(target, limit):
    if len(target) != limit:
        if len(target) >= limit:
            lengthResult = "long"
            return lengthResult
        elif len(target) <= limit:
            lengthResult = "short"
            return lengthResult
    elif len(target) == limit:
        lengthResult = "pass"
        return lengthResult

def numCheck(target):
    try:
        int(target)
        numCheckResult = 'pass'
        return numCheckResult
    except ValueError:
        numCheckResult = 'fail'
        return numCheckResult