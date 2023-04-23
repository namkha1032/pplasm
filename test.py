from abc import ABC, abstractmethod, ABCMeta
from typing import List, Tuple


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def accept(self, v, param):
        method_name = 'visit{}'.format(self.__class__.__name__)
        visit = getattr(v, method_name)
        return visit(self, param)


class Stmt(AST):
    pass


class Expr(Stmt):
    pass


class Type(AST):
    pass


class Decl(AST):
    pass
class VarDecl(Decl):
    def __init__(self, name: str, typ: str, init: str or None = None):
        self.name = name
        self.typ = typ
        self.init = init

    def __str__(self):
        return "VarDecl({}, {}{})".format(self.name, str(self.typ), ", " + str(self.init) if self.init else "")
class BlockStmt(Stmt):
    def __init__(self, body: List[Stmt or VarDecl]):
        self.body = body

    def __str__(self):
        return "BlockStmt([{}])".format(", ".join([str(body) for body in self.body]))

class FuncDecl(Decl):
    def __init__(self, name: str, body: BlockStmt):
        self.name = name
        self.body = body

    def __str__(self):
        return "FuncDecl({}, {})".format(self.name, str(self.body))
    
class ReturnStmt(Stmt):
    def __init__(self, expr: str or None = None):
        self.expr = expr

    def __str__(self):
        return "ReturnStmt({})".format(str(self.expr) if self.expr else "")

a = VarDecl("namkha","student","hcmut")
b = VarDecl("ngochoa","student","hcmut")
c = VarDecl("quanghuy","student","hcmut")
d = ReturnStmt("return hehehe")
e = VarDecl("hoquang","student","hcmut")
arr = [a,b,c,d,e]

block = BlockStmt(arr)
foo = FuncDecl("foo", block)
for x in foo.body.body:
    if type(x) is ReturnStmt:
        print(x, x.expr)
    else:
        print(x)

o = [[1,2,3],[5,6,7],[8,9]]
flag = True
o[0] += [4] if len(o) is not 3 else [69]
print(o)

lit = [1,2,3,4,5]
print(lit[-1])
print(lit[-2])