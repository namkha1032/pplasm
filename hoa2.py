from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return (Program(ctx.decl().accept(self)))

    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if ctx.decl():
            return ctx.vardecl().accept(self) + ctx.decl().accept(self) if ctx.vardecl() else [ctx.funcdecl().accept(self)] + ctx.decl().accept(self) 
        
        return ctx.vardecl().accept(self) if ctx.vardecl() else [ctx.funcdecl().accept(self)]
    
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.COLON():
            return list(map(lambda x: VarDecl(x, ctx.typ().accept(self)) ,ctx.idlist().accept(self)))
            
        return ctx.fullformat().accept(self)
    
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.COMMA():
            return [ctx.ID().getText()] + ctx.idlist().accept(self)
        return [ctx.ID().getText()]
    
    def visitFullformat(self, ctx: MT22Parser.FullformatContext):
        if ctx.ASSIGN():
            return [VarDecl(ctx.ID().getText(), ctx.typ().accept(self), ctx.expr().accept(self))]
        # a , b, c : int = 1 , 2, 3
        #[Vardecl(c,int,1)]
        #[Vardecl(b,int,1), Vardecl(c,int,2)]
        full = ctx.fullformat().accept(self)
        exprlst = [i.init for i in full] + [ctx.expr().accept(self)]
        idlst = [ctx.ID().getText()] + [i.name for i in full]
        id_type = full[0].typ
        return [VarDecl(idlst[i], id_type, exprlst[i]) for i in range(len(exprlst))]      
    
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.CONCAT():
            return BinExpr(ctx.CONCAT().getText(), ctx.expr1(0).accept(self), ctx.expr1(1).accept(self))
        return ctx.expr1(0).accept(self)
    
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.getChildCount() == 1:
            return ctx.expr2(0).accept(self)
        if ctx.EQUAL():
            return BinExpr(ctx.EQUAL().getText(), ctx.expr2(0).accept(self), ctx.expr2(1).accept(self)) 
        if ctx.NOT_EQUAL():
            return BinExpr(ctx.NOT_EQUAL().getText(), ctx.expr2(0).accept(self), ctx.expr2(1).accept(self)) 
        if ctx.GREATER():
            return BinExpr(ctx.GREATER().getText(), ctx.expr2(0).accept(self), ctx.expr2(1).accept(self)) 
        if ctx.GREATER_EQUAL():
            return BinExpr(ctx.GREATER_EQUAL().getText(), ctx.expr2(0).accept(self), ctx.expr2(1).accept(self)) 
        if ctx.LESS():
            return BinExpr(ctx.LESS().getText(), ctx.expr2(0).accept(self), ctx.expr2(1).accept(self)) 
        if ctx.LESS_EQUAL():
            return BinExpr(ctx.LESS_EQUAL().getText(), ctx.expr2(0).accept(self), ctx.expr2(1).accept(self)) 
        
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.getChildCount() == 1: 
            return ctx.expr3().accept(self)
        if ctx.AND():
            return BinExpr(ctx.AND().getText(), ctx.expr2().accept(self), ctx.expr3().accept(self)) 
        if ctx.OR():
            return BinExpr(ctx.OR().getText(), ctx.expr2().accept(self), ctx.expr3().accept(self)) 
        
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.getChildCount() == 1: 
            return ctx.expr4().accept(self)
        if ctx.ADD():
            return BinExpr(ctx.ADD().getText(), ctx.expr3().accept(self), ctx.expr4().accept(self)) 
        if ctx.SUB():
            return BinExpr(ctx.SUB().getText(), ctx.expr3().accept(self), ctx.expr4().accept(self)) 
        
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.getChildCount() == 1: 
            return ctx.expr5().accept(self)
        if ctx.MUL():
            return BinExpr(ctx.MUL().getText(), ctx.expr4().accept(self), ctx.expr5().accept(self)) 
        if ctx.DIV():
            return BinExpr(ctx.DIV().getText(), ctx.expr4().accept(self), ctx.expr5().accept(self)) 
        if ctx.MOD():
            return BinExpr(ctx.MOD().getText(), ctx.expr4().accept(self), ctx.expr5().accept(self)) 
        
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        return UnExpr(ctx.NOT().getText(), ctx.expr5().accept(self)) if ctx.NOT() else ctx.expr6().accept(self)
    
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        return UnExpr(ctx.SUB().getText(), ctx.expr6().accept(self)) if ctx.SUB() else ctx.expr7().accept(self)
    
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.literal():
            return ctx.literal().accept(self)
        if ctx.sub_expr():
            return ctx.sub_expr().accept(self)
        if ctx.funccall():
            return ctx.funccall().accept(self)
        if ctx.array_index():
            return ctx.array_index().accept(self)
        if ctx.ID():
            return Id(ctx.ID().getText())
        
    def visitLiteral(self, ctx: MT22Parser.LiteralContext): 
        if ctx.INT_LIT():
            return IntegerLit(int(ctx.INT_LIT().getText()))
        if ctx.FLOAT_LIT():
            return FloatLit(float(ctx.FLOAT_LIT().getText()))
        if ctx.TRUE():
            return BooleanLit(True)
        if ctx.FALSE():
            return BooleanLit(False)
        if ctx.STRING_LIT():
            return StringLit(int(ctx.STRING_LIT().getText()))
        return ctx.array_literal().accept(self)
        
    def visitArray_literal(self, ctx: MT22Parser.Array_literalContext):
        return ctx.exprlist().accept(self) 
    
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        return ctx.exprlist1().accept(self) if ctx.exprlist1() else []
    
    def visitExprlist1(self, ctx: MT22Parser.Exprlist1Context):
        if ctx.COMMA():
            return [ctx.expr().accept(self)] + ctx.exprlist1().accept(self)
        return [ctx.expr().accept(self)]
    
    def visitTyp(self, ctx: MT22Parser.TypContext):
        if ctx.INTEGER(): return IntegerType()
        if ctx.FLOAT(): return FloatType()
        if ctx.BOOLEAN(): return BooleanType()
        if ctx.STRING(): return StringType()
        if ctx.AUTO(): return AutoType()
        
        return ctx.array_typ().accept(self)
    
    def visitAtomic_typ(self, ctx: MT22Parser.Atomic_typContext):
        if ctx.INTEGER(): return IntegerType()
        if ctx.FLOAT(): return FloatType()
        if ctx.BOOLEAN(): return BooleanType()
        if ctx.STRING(): return StringType()
    
    def visitArray_typ(self, ctx: MT22Parser.Array_typContext):
        return ArrayType(ctx.dimension().accept(self), ctx.atomic_typ().accept(self))
    
    def visitDimension(self, ctx: MT22Parser.DimensionContext):
        if ctx.COMMA():
            return [int(ctx.INT_LIT().getText())] + ctx.dimension().accept(self)
        return [int(ctx.INT_LIT().getText())]
    
    
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        # funcpro = [name , return type, [paralist], (inherit_name)? ]
        funcpro = ctx.funcpro().accept(self)
        if len(funcpro) == 3:
            return FuncDecl(funcpro[0], funcpro[1], funcpro[2], None, ctx.funcbody().accept(self))
        return FuncDecl(funcpro[0], funcpro[1], funcpro[2], funcpro[3], ctx.funcbody().accept(self))
        
        
    def visitFunc_typ(self, ctx: MT22Parser.Func_typContext):
        if ctx.INTEGER(): return IntegerType()
        if ctx.FLOAT(): return FloatType()
        if ctx.BOOLEAN(): return BooleanType()
        if ctx.STRING(): return StringType()
        if ctx.AUTO(): return AutoType()
        if ctx.VOID(): return VoidType()
        
        return ctx.array_typ().accept(self)
    
    def visitParalist(self, ctx: MT22Parser.ParalistContext):
        return ctx.paralist1().accept(self) if ctx.paralist1() else []
    
    def visitParalist1(self, ctx: MT22Parser.Paralist1Context):
        if ctx.COMMA():
            return [ctx.para().accept(self)] + ctx.paralist1().accept(self)
        return [ctx.para().accept(self)]
    
    def visitPara(self, ctx: MT22Parser.ParaContext):
        isInherit = True if ctx.INHERIT() else False
        isOut= True if ctx.OUT() else False
        
        return ParamDecl(ctx.ID().getText(), ctx.typ().accept(self), isOut, isInherit)
        
    def visitFuncpro(self, ctx: MT22Parser.FuncproContext):
        #[name , return type, [paralist], [inherit_name]? ]
        if ctx.INHERIT():
            return [ctx.ID(0).getText(), ctx.func_typ().accept(self), ctx.paralist().accept(self), ctx.ID(1).getText()]
        return [ctx.ID(0).getText(), ctx.func_typ().accept(self), ctx.paralist().accept(self)]
        
    def visitFuncbody(self, ctx: MT22Parser.FuncbodyContext):
        return ctx.block_stmt().accept(self)
    
    def visitBlock_stmt(self, ctx: MT22Parser.Block_stmtContext):
        return BlockStmt(ctx.block_body().accept(self))
    
    def visitBlock_body(self, ctx: MT22Parser.Block_bodyContext):
        if ctx.getChildCount() == 0: 
            return []
        if ctx.stmt():
            return [ctx.stmt().accept(self)] + ctx.block_body().accept(self)
        return [ctx.vardecl().accept(self)] + ctx.block_body().accept(self)
    
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        if ctx.assign_stmt(): return ctx.assign_stmt().accept(self)
        if ctx.if_stmt(): return ctx.if_stmt().accept(self)
        if ctx.for_stmt(): return ctx.for_stmt().accept(self)
        if ctx.while_stmt(): return ctx.while_stmt().accept(self)
        if ctx.do_while_stmt(): return ctx.do_while_stmt().accept(self)
        if ctx.break_stmt(): return ctx.break_stmt().accept(self)
        if ctx.continue_stmt(): return ctx.continue_stmt().accept(self)
        if ctx.return_stmt(): return ctx.return_stmt().accept(self)
        if ctx.block_stmt(): return ctx.block_stmt().accept(self)
        if ctx.call_stmt(): return ctx.call_stmt().accept(self)
        
    def visitAssign_stmt(self, ctx: MT22Parser.Assign_stmtContext):
        if ctx.ID():
            return AssignStmt(Id(ctx.ID().getText()), ctx.expr().accept(self))
        return AssignStmt(ctx.array_index().accept(self), ctx.expr().accept(self)) 
    
    def visitArray_index(self, ctx: MT22Parser.Array_indexContext):
        return ArrayCell(ctx.ID().getText(), ctx.index_expr().accept(self))
    
    def visitIndex_expr(self, ctx: MT22Parser.Index_exprContext):
        if ctx.COMMA():
            return [ctx.expr().accept(self)] + ctx.index_expr().accept(self)
        return [ctx.expr().accept(self)]
    
    def visitIf_stmt(self, ctx: MT22Parser.If_stmtContext):
        if ctx.ELSE():
            return IfStmt(ctx.expr().accept(self), ctx.stmt(0).accept(self), ctx.stmt(1).accept(self))
        return IfStmt(ctx.expr().accept(self), ctx.stmt(0).accept(self), None)
    
    def visitFor_stmt(self, ctx: MT22Parser.For_stmtContext):
        if ctx.ID():
            return ForStmt(AssignStmt(Id(ctx.ID().getText()), ctx.expr(0).accept(self)), ctx.expr(1).accept(self), ctx.expr(2).accept(self), ctx.stmt().accept(self))
        return ForStmt(AssignStmt(ctx.array_index().accept(self), ctx.expr().accept(self)), ctx.expr(1).accept(self), ctx.expr(2).accept(self), ctx.stmt().accept(self))
    
    def visitWhile_stmt(self, ctx: MT22Parser.While_stmtContext):
        return WhileStmt(ctx.expr().accept(self), ctx.stmt().accept(self))
    
    def visitDo_While_stmt(self, ctx: MT22Parser.Do_while_stmtContext):
        return DoWhileStmt(ctx.expr().accept(self), ctx.block_stmt().accept(self))
    
    def visitBreak_stmt(self, ctx: MT22Parser.Break_stmtContext):
        return BreakStmt()
    
    def visitContinue_stmt(self, ctx: MT22Parser.Continue_stmtContext):
        return ContinueStmt()
    
    def visitReturn_stmt(self, ctx: MT22Parser.Return_stmtContext):
        if ctx.expr():
            return ReturnStmt(ctx.expr().accept(self))
        return ReturnStmt()
    
    def visitCall_stmt(self, ctx: MT22Parser.Call_stmtContext):
        obj = ctx.funccall().accept(self)
        return CallStmt(obj.name, obj.args)
    
    def visitFunccall(self, ctx: MT22Parser.FunccallContext):
        return FuncCall(ctx.ID().getText(), ctx.exprlist().accept(self))
    