from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllist()))
    # Visit a parse tree produced by MT22Parser#decllist.
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        if ctx.decllist():
            return [self.visit(ctx.decl())] + self.visit(ctx.decllist())
        return [self.visit(ctx.decl())]

    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        return self.visit(ctx.funcdecl())


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

    def visitArraytyp(self, ctx:MT22Parser.ArraytypContext):
        return ArrayType(self.visit(ctx.dimensions()), self.visit(ctx.atomictyp()))


    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        if ctx.COMMA():
            return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimensions())
        return [int(ctx.INTLIT().getText())]


    def visitArrayindex(self, ctx:MT22Parser.ArrayindexContext):
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.exprlistnonnull()))
    


    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visit(ctx.exprlistnullable())



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
        if ctx.expr7(): return self.visit(ctx.expr7())

    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        if ctx.NOT(): return UnExpr(ctx.NOT().getText(), self.visit(ctx.expr5()))
        if ctx.expr6(): return self.visit(ctx.expr6())

    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        if ctx.MUL(): 
            return BinExpr(ctx.MUL().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        if ctx.DIV(): 
            return BinExpr(ctx.DIV().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        if ctx.MOD(): 
            return BinExpr(ctx.MOD().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())

    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        if ctx.ADD(): 
            return BinExpr(ctx.ADD().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        if ctx.SUB(): 
            return BinExpr(ctx.SUB().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())

    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        if ctx.AND(): 
            return BinExpr(ctx.AND().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        if ctx.OR(): 
            return BinExpr(ctx.OR().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        if ctx.EQUAL(): 
            return BinExpr(ctx.EQUAL().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.NOTEQUAL(): 
            return BinExpr(ctx.NOTEQUAL().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.LESS(): 
            return BinExpr(ctx.LESS().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.GREATER(): 
            return BinExpr(ctx.GREATER().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.LESSEQUAL(): 
            return BinExpr(ctx.LESSEQUAL().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.GREATEREQUAL(): 
            return BinExpr(ctx.LESSEQUAL().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
    
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        if ctx.CONCAT(): 
            return BinExpr(ctx.CONCAT().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))

    # Chưa làm
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        pass

    def visitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt()

    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        return ContinueStmt()
    
    def visitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        return BreakStmt()
    
    def visitDowhilestmt(self, ctx:MT22Parser.DowhilestmtContext):
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.blockstmt()))

    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.stmt()))

    # Chưa làm
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        return ForStmt()

    # Xem lại cái None
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        if ctx.ELSE():
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.stmt(0)), self.visit(ctx.stmt(1)))
        return IfStmt(self.visit(ctx.expr()), self.visit(ctx.stmt(0)))


    # Chưa làm
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        return AssignStmt
    
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        if ctx.assignstmt():
            return self.visit(ctx.assignstmt())
        if ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        if ctx.forstmt():
            return self.visit(ctx.forstmt())
        if ctx.whilestmt():
            return self.visit(ctx.whilestmt())
        if ctx.dowhilestmt():
            return self.visit(ctx.dowhilestmt())
        if ctx.breakstmt():
            return self.visit(ctx.breakstmt())
        if ctx.continuestmt():
            return self.visit(ctx.continuestmt())
        if ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        if ctx.callstmt():
            return self.visit(ctx.callstmt())
        if ctx.blockstmt():
            return self.visit(ctx.blockstmt())

    def visitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        if ctx.stmt():
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())
        if ctx.vardecl():
            return [self.visit(ctx.vardecl())] + self.visit(ctx.stmtlist())
        
    def visitBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        return BlockStmt(self.visit(ctx.stmtlist()))
    
    def visitExprlistnullable(self, ctx:MT22Parser.ExprlistnullableContext):
        if ctx.exprlistnonnull():
            return self.visit(ctx.exprlistnonnull())
        if ctx.getChildCount() == 0:
            return []


    def visitExprlistnonnull(self, ctx:MT22Parser.ExprlistnonnullContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprlistnonnull())

    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        if ctx.COMMA():
            return [ctx.ID().getText()] + self.visit(ctx.idlist())
        return [ctx.ID().getText()]

    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        if ctx.COLON():
            return [VarDecl(x, self.visit(ctx.typ())) for x in self.visit(ctx.idlist())]
        return self.visit(ctx.varinit())

    def visitVarinit(self, ctx:MT22Parser.VarinitContext):
        if ctx.typ():
            return [VarDecl(ctx.ID().getText(), self.visit(ctx.typ()), self.visit(ctx.expr()))]
        childArray = self.visit(ctx.varinit())
        exprlist = [x.init for x in childArray] + [ctx.expr().accept(self)]
        idlist = [ctx.ID().getText()] + [x.name for x in childArray] 
        return [VarDecl(idlist[i], childArray[0].typ, exprlist[i]) for i in range(len(exprlist))]

    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        IDVar, functypVar, paramlistnullableVar, inheritIDVar = self.visit(ctx.funcpro())
        funcbodyVar = self.visit(ctx.funcbody())
        if inheritIDVar:
            return FuncDecl(IDVar,functypVar,paramlistnullableVar,inheritIDVar,funcbodyVar)
        else:
            return FuncDecl(IDVar,functypVar,paramlistnullableVar,None,funcbodyVar)
        


    # Visit a parse tree produced by MT22Parser#funcpro.
    def visitFuncpro(self, ctx:MT22Parser.FuncproContext):
        if ctx.INHERIT():
            return ctx.ID().getText(), self.visit(ctx.functyp()), self.visit(ctx.paramlistnullable), ctx.ID().getText()
        return ctx.ID().getText(), self.visit(ctx.functyp()), self.visit(ctx.paramlistnullable), False


    # Visit a parse tree produced by MT22Parser#paramlistnullable.
    def visitParamlistnullable(self, ctx:MT22Parser.ParamlistnullableContext):
        if ctx.paramlistnonnull():
            return self.visit(ctx.paramlistnonnull())
        return []
        


    # Visit a parse tree produced by MT22Parser#paramlistnonnull.
    def visitParamlistnonnull(self, ctx:MT22Parser.ParamlistnonnullContext):
        if ctx.COMMA():
            return [self.visit(ctx.param())]+self.visit(ctx.paramlistnonnull())
        return [self.visit(ctx.param())]


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        if ctx.getChildCount() == 3:
            return ParamDecl(ctx.ID().getText(),self.visit(ctx.typ()),False, False)
        if ctx.INHERIT() and ctx.OUT():
            return ParamDecl(ctx.ID().getText(),self.visit(ctx.typ()),True, True)
        if ctx.INHERIT():
            return ParamDecl(ctx.ID().getText(),self.visit(ctx.typ()),False, True)
        if ctx.OUT():
            return ParamDecl(ctx.ID().getText(),self.visit(ctx.typ()),True, False)



    def visitFuncbody(self, ctx:MT22Parser.FuncbodyContext):
        return self.visit(ctx.blockstmt())


    def visitFunccall(self, ctx:MT22Parser.FunccallContext):
        return self.visit(ctx.ID().getText(),self.visit(ctx.exprlistnullable()))
    









