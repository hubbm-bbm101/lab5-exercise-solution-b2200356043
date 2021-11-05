v=input("Mail: ")

def isValid(v):
    if ("@" in v) & ("." in v):
        return True
    else:
        False
print(str(isValid(v)))
    