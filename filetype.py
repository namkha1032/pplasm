# 1.1
# 1 int 2 float 3 bool

from typing import List, Tuple
from abc import ABC, abstractmethod, ABCMeta


class Type(ABC):
    pass


class IntType(Type):
    pass


class FloatType(Type):
    pass


class BoolType(Type):
    pass


class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o):
        o = []  # list of {name, type}
        for decl in ctx.decl:
            o = self.visit(decl, o)
        self.visit(ctx.exp, o)

    def visitVarDecl(self, ctx: VarDecl, o):
        return o + [ctx]

    def visitId(self, ctx, o):
        for decl in o:
            if decl.name == ctx.name:
                return decl.typ
        raise UndeclaredIdentifier(ctx.name)

    def visitIntType(self, ctx: IntType, o): pass

    def visitFloatType(self, ctx: FloatType, o): pass

    def visitBoolType(self, ctx: BoolType, o): pass

    def visitBinOp(self, ctx: BinOp, o):
        left = self.visit(ctx.e1, o)
        right = self.visit(ctx.e2, o)
        if ctx.op in ["+", '-', '*']:
            if type(left) is BoolType or type(right) is BoolType:
                raise TypeMismatchInExpression(ctx)
            if type(left) is FloatType or type(right) is FloatType:
                return FloatType()
            return IntType()
        if ctx.op == "/":
            if (type(left) is not BoolType and type(right) is not BoolType):
                return FloatType()
            raise TypeMismatchInExpression(ctx)
        if ctx.op in ['!', "&&", "||"]:
            if (type(left) is BoolType and type(right) is BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ctx)
        if ctx.op in ["<", ">", "==", "!="]:
            if type(left) is type(right):
                return BoolType()
            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self, ctx: UnOp, o):
        t = self.visit(ctx.e, o)
        if ctx.op == "!":
            if type(t) is BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ctx)
        else:
            if type(t) is FloatType:
                return FloatType()
            if type(t) is IntType:
                return IntType()
            raise TypeMismatchInExpression(ctx)

    def visitIntLit(self, ctx: IntLit, o):
        return IntType()

    def visitFloatLit(self, ctx, o):
        return FloatType()

    def visitBoolLit(self, ctx, o):
        return BoolType()

###############################
# 1.2
# 1 int 2 float 3 bool


class Type(ABC):
    pass


class IntType(Type):
    pass


class FloatType(Type):
    pass


class BoolType(Type):
    pass


class StaticCheck(Visitor):
    def visitBinOp(self, ctx: BinOp, o):
        left = self.visit(ctx.e1, o)
        right = self.visit(ctx.e2, o)
        if ctx.op in ["+", '-', '*']:
            if type(left) is BoolType or type(right) is BoolType:
                raise TypeMismatchInExpression(ctx)
            if type(left) is FloatType or type(right) is FloatType:
                return FloatType()
            return IntType()
        if ctx.op == "/":
            if (type(left) is not BoolType and type(right) is not BoolType):
                return FloatType()
            raise TypeMismatchInExpression(ctx)
        if ctx.op in ['!', "&&", "||"]:
            if (type(left) is BoolType and type(right) is BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ctx)
        if ctx.op in ["<", ">", "==", "!="]:
            if type(left) is type(right):
                return BoolType()
            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self, ctx: UnOp, o):
        t = self.visit(ctx.e, o)
        if ctx.op == "!":
            if type(t) is BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ctx)
        else:
            if type(t) is FloatType:
                return FloatType()
            if type(t) is IntType:
                return IntType()
            raise TypeMismatchInExpression(ctx)

    def visitIntLit(self, ctx: IntLit, o):
        return IntType()

    def visitFloatLit(self, ctx, o):
        return FloatType()

    def visitBoolLit(self, ctx, o):
        return BoolType()

#############################
# Program([VarDecl("x")],[Assign(Id("x"),BinOp("*",BinOp("+",Id("x"),IntLit(3)),BinOp("-",Id("x"),FloatLit(2.1))))])
# var x;
# x = (x + 3) * (x - 2.1);
# Type Mismatch In Expression: BinOp("-",Id("x"),FloatLit(2.1))
# Program([VarDecl("x"),VarDecl("y"),VarDecl("z")],[Assign(Id("x"),BinOp(">b",BinOp("&&",Id("x"),Id("y")),BinOp("||",BoolLit(False),BinOp(">",Id("z"),IntLit(3))))),Assign(Id("z"),Id("x"))])
# var x, y, z;
# x = (x && y) >b (False || z > 3);
# z = x;
# Type Mismatch In Statement: Assign(Id("z"),Id("x"))
# Program([VarDecl("x"),VarDecl("y")],[Assign(Id("x"),Id("y"))])
# var x, y;
# x = y;
# Type Cannot Be Inferred: Assign(Id("x"),Id("y"))
#############################
# 1.3


# class AST(ABC): pass
# class Visitor: pass

class Type(AST):
    pass


class IntType(AST):
    pass


class FloatType(AST):
    pass


class BoolType(AST):
    pass


class NoType(AST):
    pass


class Symbol:
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ


class Utils:
    def infer(symbol_list, name, typ):
        # if symbol in symbol_list:??
        for symbol in symbol_list:
            if symbol.name == name:
                symbol.typ = typ
                return typ


class StaticCheck(Visitor):
    # program: decl: List[VarDecl], stmts: List[Assign]
    def visitProgram(self, ctx: Program, o):
        o = []
        for decl in ctx.decl:
            o = self.visit(decl, o)
        for stmt in ctx.stmts:
            self.visit(stmt, o)

    def visitVarDecl(self, ctx: VarDecl, o):
        o += [Symbol(ctx.name, NoType())]
        return o

    def visitAssign(self, ctx: Assign, o):
        rtype = self.visit(ctx.rhs, o)
        ltype = self.visit(ctx.lhs, o)
        if type(ltype) is NoType and type(rtype) is NoType:
            raise TypeCannotBeinferred(ctx)
        if type(ltype) is NoType:
            ltype = Utils.infer(o, ctx.lhs.name, rtype)
            return
        if type(rtype) is NoType:
            rtype = Utils.infer(o, ctx.rhs.name, ltype)
            return
        if type(ltype) is type(rtype):
            return
        raise TypeMismatchInStatement(ctx)


    # var x;
    # x = (x + 3) * (x - 2.1);
    def visitBinOp(self, ctx: BinOp, o):
        e1t = self.visit(ctx.e1, o)  # NoType()
        e2t = self.visit(ctx.e2, o)  # IntType()

        if ctx.op in ['+', '-', '*', '/']:
            if type(e1t) is NoType:
                e1t = Utils.infer(o, ctx.e1.name, IntType())

            if type(e2t) is NoType:
                e2t = Utils.infer(o, ctx.e2.name, IntType())

            if type(e1t) is IntType and type(e2t) is IntType:
                return IntType()
            raise TypeMismatchInExpression(ctx)

        if ctx.op in ['+.', '-.', '*.', '/.']:
            if type(e1t) is NoType:
                e1t = Utils.infer(o, ctx.e1.name, FloatType())

            if type(e2t) is NoType:
                e2t = Utils.infer(o, ctx.e2.name, FloatType())

            if type(e1t) is FloatType and type(e2t) is FloatType:
                return FloatType()
            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self, ctx: UnOp, o): pass

    def visitIntLit(self, ctx: IntLit, o):
        return IntType()

    def visitFloatLit(self, ctx, o):
        return FloatType()

    def visitBoolLit(self, ctx, o):
        return BoolType()

    def visitId(self, ctx, o):
        for symbol in o:
            if ctx.name == symbol.name:
                return symbol.typ
        raise UndeclaredIdentifier(ctx.name)

#####################################
# 2.1


# class AST(ABC): pass
# class Visitor: pass

class Type(AST):
    pass


class IntType(AST):
    pass


class FloatType(AST):
    pass


class BoolType(AST):
    pass


class NoType(AST):
    pass


class Symbol:
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ


class Utils:
    def infer(env, name, typ):
        # Cần ghi 2 vòng lặp do list lồng list
        for symbol_list in env:
            for symbol in symbol_list:
                if symbol.name == name:
                    symbol.typ = typ
                    return typ


class StaticCheck(Visitor):
    # program: decl: List[VarDecl], stmts: List[Assign]
    def visitProgram(self, ctx: Program, o):
        o = [[]]
        for decl in ctx.decl:
            o = self.visit(decl, o)
        for stmt in ctx.stmts:
            self.visit(stmt, o)

    def visitVarDecl(self, ctx: VarDecl, o):
        # Phải check raise lỗi redelcared trước
        o[0] += [Symbol(ctx.name, NoType())]
        return o

    def visitBlock(self, ctx: Block, o):
        env = [[]] + o
        for decl in ctx.decl:
            env = self.visit(decl, env)
        for stmt in ctx.stmts:
            self.visit(stmt, env)

    def visitAssign(self, ctx: Assign, o):
        rtype = self.visit(ctx.rhs, o)
        ltype = self.visit(ctx.lhs, o)
        if type(ltype) is NoType and type(rtype) is NoType:
            raise TypeCannotBeinferred(ctx)
        if type(ltype) is NoType:
            ltype = Utils.infer(o, ctx.lhs.name, rtype)
            return
        if type(rtype) is NoType:
            rtype = Utils.infer(o, ctx.rhs.name, ltype)
            return
        if type(ltype) is type(rtype):
            return
        raise TypeMismatchInStatement(ctx)

    # x + 1
    def visitBinOp(self, ctx: BinOp, o):
        e1t = self.visit(ctx.e1, o)  # NoType()
        e2t = self.visit(ctx.e2, o)  # IntType()

        if ctx.op in ['+', '-', '*', '/']:
            if type(e1t) is NoType:
                e1t = Utils.infer(o, ctx.e1.name, IntType())

            if type(e2t) is NoType:
                e2t = Utils.infer(o, ctx.e2.name, IntType())

            if type(e1t) is IntType and type(e2t) is IntType:
                return IntType()
            raise TypeMismatchInExpression(ctx)

        if ctx.op in ['+.', '-.', '*.', '/.']:
            if type(e1t) is NoType:
                e1t = Utils.infer(o, ctx.e1.name, FloatType())

            if type(e2t) is NoType:
                e2t = Utils.infer(o, ctx.e2.name, FloatType())

            if type(e1t) is FloatType and type(e2t) is FloatType:
                return FloatType()
            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self, ctx: UnOp, o): pass

    def visitIntLit(self, ctx: IntLit, o):
        return IntType()

    def visitFloatLit(self, ctx, o):
        return FloatType()

    def visitBoolLit(self, ctx, o):
        return BoolType()

    def visitId(self, ctx, o):
        # Cần ghi 2 vòng lặp do list lồng list
        for symbol_list in o:
            for symbol in symbol_list:
                if ctx.name == symbol.name:
                    return symbol.typ
        raise UndeclaredIdentifier(ctx.name)
##########################################
# 2.2


class StaticCheck(Visitor):
    def visitProgram(self, ctx: Program, o):
        o = [{}]
        for i in ctx.decl:
            self.visit(i, o)
        for i in ctx.stmts:
            self.visit(i, o)

    def searchAndSet(self, typ, name, o):
        for i in o:
            if name in i:
                i[name] = typ
                return

    def visitVarDecl(self, ctx: VarDecl, o):
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o[0][ctx.name] = 0

    def visitFuncDecl(self, ctx: FuncDecl, o):
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o_1 = [{}] + o
        for i in ctx.param:
            self.visit(i, o_1)
        for i in ctx.local:
            self.visit(i, o_1)
        for i in ctx.stmts:
            self.visit(i, o_1)
        lst_param = []
        for i in ctx.param:
            lst_param += [o_1[0][i.name]]
        o[0][ctx.name] = lst_param

    def visitCallStmt(self, ctx: CallStmt, o):
        if ctx.name not in o[0]:
            raise UndeclaredIdentifier(ctx.name)
        else:
            lst_param = o[0][ctx.name]
            if len(lst_param) != len(ctx.args):
                raise TypeMismatchInStatement(ctx)
            else:
                for i in range(0, len(lst_param)):
                    typ = self.visit(ctx.args[i], o)
                    if lst_param[i] == 0 and typ != 0:
                        o[0][ctx.name][i] = typ
                        continue
                    if lst_param[i] != 0 and typ == 0:
                        self.searchAndSet(lst_param[i], ctx.args[i].name, o)
                    if lst_param[i] == 0 and typ == 0:
                        raise TypeCannotBeInferred(ctx)
                    if lst_param[i] != self.visit(ctx.args[i], o):
                        raise TypeMismatchInStatement(ctx)

    def visitAssign(self, ctx: Assign, o):
        right = self.visit(ctx.rhs, o)
        left = self.visit(ctx.lhs, o)
        if left == 0 and right != 0:
            self.searchAndSet(right, ctx.lhs.name, o)
        if left != 0 and right == 0:
            self.searchAndSet(left, ctx.rhs.name, o)
        if left == 0 and right == 0:
            raise TypeCannotBeInferred(ctx)
        if self.visit(ctx.rhs, o) != self.visit(ctx.lhs, o):
            raise TypeMismatchInStatement(ctx)

    def visitBinOp(self, ctx: BinOp, o):
        l = self.visit(ctx.e1, o)
        r = self.visit(ctx.e2, o)
        if ctx.op in ["+", "-", "*", "/"]:
            if l == 0:
                self.searchAndSet(1, ctx.e1.name, o)
            if r == 0:
                self.searchAndSet(1, ctx.e2.name, o)
            if self.visit(ctx.e1, o) != 1 or self.visit(ctx.e2, o) != 1:
                raise TypeMismatchInExpression(ctx)
            else:
                return 1

        elif ctx.op in ["+.", "-.", "*.", "/."]:
            if l == 0:
                self.searchAndSet(2, ctx.e1.name, o)
            if r == 0:
                self.searchAndSet(2, ctx.e2.name, o)
            if self.visit(ctx.e1, o) != 2 or self.visit(ctx.e2, o) != 2:
                raise TypeMismatchInExpression(ctx)
            else:
                return 2

        elif ctx.op in [">", "="]:
            if l == 0:
                self.searchAndSet(1, ctx.e1.name, o)
            if r == 0:
                self.searchAndSet(1, ctx.e2.name, o)
            if self.visit(ctx.e1, o) != 1 or self.visit(ctx.e2, o) != 1:
                raise TypeMismatchInExpression(ctx)
            else:
                return 3

        elif ctx.op in [">.", "=."]:
            if l == 0:
                self.searchAndSet(2, ctx.e1.name, o)
            if r == 0:
                self.searchAndSet(2, ctx.e1.name, o)
            if self.visit(ctx.e1, o) != 2 or self.visit(ctx.e2, o) != 2:
                raise TypeMismatchInExpression(ctx)
            else:
                return 3

        elif ctx.op in ["||", "&&", "=b", ">b"]:
            if l == 0:
                self.searchAndSet(3, ctx.e1.name, o)
            if r == 0:
                self.searchAndSet(3, ctx.e1.name, o)
            if self.visit(ctx.e1, o) != 3 or self.visit(ctx.e2, o) != 3:
                raise TypeMismatchInExpression(ctx)
            else:
                return 3

    def visitUnOp(self, ctx: UnOp, o):
        typ = self.visit(ctx.e, o)
        if ctx.op == "-":
            if typ != 1:
                if typ == 0:
                    self.searchAndSet(1, ctx.e.name, o)
                    return 1
                raise TypeMismatchInExpression(ctx)
            return 1
        elif ctx.op == "-.":
            if typ != 2:
                if typ == 0:
                    self.searchAndSet(3, ctx.e.name, o)
                    return 2
                raise TypeMismatchInExpression(ctx)
            return 2
        elif ctx.op == "!":
            if typ != 3:
                if typ == 0:
                    self.searchAndSet(3, ctx.e.name, o)
                    return 3
                raise TypeMismatchInExpression(ctx)
            return 3
        elif ctx.op == "i2f":
            if typ != 1:
                if typ == 0:
                    self.searchAndSet(1, ctx.e.name, o)
                    return 2
                raise TypeMismatchInExpression(ctx)
            return 2
        else:  # floor
            if typ != 2:
                if typ == 0:
                    self.searchAndSet(2, ctx.e.name, o)
                    return 1
                raise TypeMismatchInExpression(ctx)
            return 1

    def visitIntLit(self, ctx: IntLit, o):
        return 1

    def visitFloatLit(self, ctx, o):
        return 2

    def visitBoolLit(self, ctx, o):
        return 3

    def visitId(self, ctx, o):
        for i in o:
            if ctx.name in i:
                return i[ctx.name]
        raise UndeclaredIdentifier(ctx.name)
