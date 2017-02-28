

string = "hello"


def rvstring(string):
    new = ''
    index = len(string)
    while index:
        index -= 1
        new += string[index]
    print new
    
rvstring(string)