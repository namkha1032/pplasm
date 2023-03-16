class VarDecl():
    def __init__(self, name, typ, init):
        self.name = name
        self.typ = typ
        self.init = init

    def __str__(self):
        return "VarDecl({}, {}{})".format(self.name, str(self.typ), ", " + str(self.init) if self.init else "")

fullArray = [VarDecl("a","int",4), VarDecl("b","int",3), VarDecl("c","int",2), VarDecl("d","int",1)]

finArray = [VarDecl(fullArray[i].name,fullArray[i].typ, fullArray[-(i+1)].init) for i in range(len(fullArray))]
for x in finArray:
    print(x)