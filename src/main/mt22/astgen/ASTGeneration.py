from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program([])
    
    def visitTyp(self, ctx: MT22Parser.TypContext):
        if ctx.BOOLEAN(): return BooleanType()
        if ctx.INTEGER(): return IntegerType()
        if ctx.FLOAT(): return FloatType()
        if ctx.STRING(): return StringType()
        if ctx.AUTO(): return AutoType()
        if ctx.arraytyp(): return self.visit(ctx.arraytyp())
    
    def visitAtomictyp(self, ctx: MT22Parser.TypContext):
        if ctx.BOOLEAN(): return BooleanType()
        if ctx.INTEGER(): return IntegerType()
        if ctx.FLOAT(): return FloatType()
        if ctx.STRING(): return StringType()

    def visitFunctyp(self, ctx:MT22Parser.FunctypContext):
        if ctx.BOOLEAN(): return BooleanType()
        if ctx.INTEGER(): return IntegerType()
        if ctx.FLOAT(): return FloatType()
        if ctx.STRING(): return StringType()
        if ctx.AUTO(): return AutoType()
        if ctx.VOID(): return VoidType()
        if ctx.arraytyp(): return self.visit(ctx.arraytyp())

    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        if ctx.INTEGER(): return IntegerType()
        if ctx.FLOAT(): return FloatType()
        if ctx.STRING(): return StringType()
        if ctx.TRUE(): return BooleanLit(True)
        if ctx.FALSE(): return BooleanLit(False)
        if ctx.ID(): return Id(ctx.ID().getText())
        if ctx.arraylit(): return self.visit(ctx.arraylit())
        if ctx.arrayindex(): return self.visit(ctx.arrayindex())
        if ctx.funccall(): return self.visit(ctx.funccall())
        if ctx.expr(): return self.visit(ctx.expr())

    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        if ctx.SUB(): return UnExpr(ctx.SUB().getText(), self.visit(ctx.expr6()))
        if ctx.expr7()

