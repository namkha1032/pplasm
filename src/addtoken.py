tokendict = {}
inputstring = ""
while inputstring != "x":
    inputstring = input()
    inputlist = inputstring.split('=')
    tokendict[int(inputlist[1])]=inputlist[0]
    print(tokendict)