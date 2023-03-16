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
        return self.visitChildren(ctx)












