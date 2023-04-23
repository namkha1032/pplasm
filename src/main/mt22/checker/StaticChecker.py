from Visitor import Visitor
####################################################
from StaticError import *
from AST import *
from abc import ABC
####################################################
# class Symbol:
#     def __init__(self, decl: Decl, envi: List[ParamDecl] or None=None):
#         self.decl = decl
#         self.envi = envi
class GetEnv(Visitor):
    def __init__(self):
        pass
 
    def check(self):
        return self.visitProgram(self.ast, [[]])
    def visitProgram(self, ctx: Program, o):
        o = [[]]
        for decl in ctx.decls:
            o = self.visit(decl, o)
        return o
    def visitVarDecl(self, ctx:VarDecl, o):
        # for decl in o[0]:
        #     if decl.name == ctx.name:
        #         raise Redeclared(Variable(), ctx.name)
        o[0] += [ctx]
        return o
        
    def visitFuncDecl(self, ctx:FuncDecl, o):
        # Check redeclared function
        # for decl in o[0]:
        #     if decl.name == ctx.name:
        #         raise Redeclared(Function(), ctx.name)
        o[0] += [ctx]
        return o


    def visitIntegerLit(self, ctx:IntegerLit, o):
        return IntegerType()
    def visitFloatLit(self, ctx:FloatLit, o):
        return FloatType()
    def visitStringLit(self, ctx:StringLit, o):
        return StringType()
    def visitBooleanLit(self, ctx:BooleanLit, o):
        return BooleanType()
    def visitArrayLit(self, ctx:ArrayLit, o):
        return ArrayType()

    def visitIntegerType(self, ctx:IntegerType, o):
        return IntegerType()
    def visitFloatType(self,  ctx:FloatType, o): 
        return FloatType()
    def visitBooleanType(self,  ctx:BooleanType, o): 
        return BooleanType()
    def visitStringType(self,  ctx:StringType, o): 
        return StringType()
    def visitArrayType(self,  ctx:ArrayType, o): 
        return ArrayType()
    def visitAutoType(self,  ctx:AutoType, o): 
        return AutoType()
    def visitVoidType(self,  ctx:VoidType, o): 
        return VoidType()


def findParentEnv(ctx, o):
    if ctx.inherit is not None:
        found = False
        parentenv = []
        # Get all environment of current parent
        for parentparam in ctx.params:
            if parentparam.inherit == True:
                parentenv += [parentparam]
        # Find grandparent function
        for decl in o[-1]:
            if (type(decl) is FuncDecl and decl.name == ctx.inherit):
                found = True
                parentenv += findParentEnv(decl,o)
                return parentenv
        if found == False:
            raise Undeclared(Function(), ctx.inherit)
    if ctx.inherit is None:
        parentenv = []
        # Get all environment of current parent
        for parentparam in ctx.params:
            if parentparam.inherit == True:
                parentenv += [parentparam]
        return parentenv


class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
 
    def check(self):
        return self.visitProgram(self.ast, [])
    
    def visitProgram(self, ctx:Program, o):
        o = GetEnv().visit(ctx,o)
        count = 0
        for decl in ctx.decls:
            for i in range(count):
                if decl.name == ctx.decls[i].name:
                    if type(decl) is VarDecl:
                        raise Redeclared(Variable(),decl.name)
                    if type(decl) is FuncDecl:
                        raise Redeclared(Function(),decl.name)
            count+=1
            o = self.visit(decl, o)
        # entry point
        for decl in ctx.decls:
            if decl.name == "main" and type(decl) is FuncDecl:
                return
        raise NoEntryPoint()

    def visitVarDecl(self, ctx:VarDecl, o):
        # Check for redeclared if not global scope
        # if len(o) == 1:
        #     count = 0
        #     for decl in o[-1]:
        #         if decl.name == ctx.name:
        #             count+=1
        #             if count == 2:
        #                 raise Redeclared(Variable(), ctx.name)  
        if len(o) > 1:
            for decl in o[0]:
                if decl.name == ctx.name:
                    raise Redeclared(Variable(), ctx.name)            
        # Check for Invalid auto
        if type(ctx.typ) is AutoType:
            if ctx.init is None:
                raise Invalid(Variable(), ctx.name)
            # type infer for auto
            inittype = self.visit(ctx.init, o)
            ctx.typ = inittype
            if len(o) > 1:
                o[0] += [ctx]
            else:
                for declIndex, decl in enumerate(o[-1]):
                    if decl.name == ctx.name:
                        o[-1][declIndex].typ = inittype
                        return o
            return o
        # Check for init value
        if ctx.init is not None:
            vartype = self.visit(ctx.typ, o)
            inittype = self.visit(ctx.init, o)
            if type(vartype) is ArrayType:
                # if type(vartype.typ) is AutoType:
                #     if len(o) > 1:
                #         o[0] += [ctx]
                #         return o
                #     else:
                #         for arrIndex, arr in enumerate(o[-1]):
                #             if arr.name == ctx.init.name:
                #                 o[-1][arrIndex].typ.typ = inittype
                #                 return o
                if type(vartype.typ) is FloatType and type(inittype) is IntegerType:
                    if len(o) > 1:
                        o[0] += [ctx]
                    return o
                if type(vartype.typ) is type(inittype):
                    if len(o) > 1:
                        o[0] += [ctx]
                    return o
            if type(inittype) is AutoType:
                found = False
                for scopeIndex, scope in enumerate(o):
                    for funcIndex, func in enumerate(scope):
                        if func.name == ctx.init.name:
                            o[scopeIndex][funcIndex].return_type = vartype
                            found = True
                        if found == True:
                            break
                    if found == True:
                        break
                if len(o) > 1:
                    o[0] += [ctx]
                return o
            
            if type(vartype) is not type(inittype):
                if (type(vartype) is FloatType and type(inittype) is IntegerType):
                    if len(o) > 1:
                        o[0] += [ctx]
                    return o
                raise TypeMismatchInVarDecl(ctx)
            if len(o) > 1:
                o[0] += [ctx]
            return o 
        if len(o) > 1:
            o[0] += [ctx]
        return o 

    def visitParamDecl(self, ctx:ParamDecl, localenv):
        for paramdecl in localenv[0]:
            if paramdecl.name == ctx.name:
                raise Redeclared(Parameter(), ctx.name)
        localenv[0] += [ctx]
        return localenv

    def visitFuncDecl(self, ctx:FuncDecl, o):
        # Check redeclared func
        # count = 0
        # for decl in o[-1]:
        #     if decl.name == ctx.name:
        #         count+=1
        #         if count == 2:
        #             raise Redeclared(Function(), ctx.name)  
        # Check local param
        localenv = [[]] + o
        for paramdecl in ctx.params:
            localenv = self.visit(paramdecl, localenv)
        inheritenv = []
        parent = 0
        if ctx.inherit is not None:
            # Check existance of parent function
            for decl in o[-1]:
                if decl.name == ctx.inherit:
                    parent = decl
            if parent is 0:
                raise Undeclared(Function(), ctx.inherit)
            # Get all environment of current parent
            for parentparam in parent.params:
                if parentparam.inherit == True:
                    inheritenv += [parentparam]
            # Check for invalid parameter
            for localparam in localenv[0]:
                for inheritparam in inheritenv:
                    if localparam.name == inheritparam.name:
                        raise Invalid(Parameter(), localparam.name)
        
        # Sum of local param and inherit param
        # sumenv = [localenv + inheritenv] + o
        localenv[0] += inheritenv
        i=0
        for line in ctx.body.body:
            if i == 0 and ctx.inherit is not None:
                if len(parent.params) > 0:
                    if type(line) is not CallStmt:
                        raise TypeMismatchInExpression("")
                    if line.name != "super" and line.name != "preventDefault":
                        raise TypeMismatchInExpression("")
                    if line.name == "super":
                        if len(line.args) > len(parent.params):
                            raise TypeMismatchInExpression(line.args[len(parent.params)])
                        if len(line.args) < len(parent.params):
                            raise TypeMismatchInExpression("")
                        if len(line.args) == len(parent.params):
                            # --------------------------------------------------------------------------------------------
                            # for i in range(len(line.args)):
                            #     argtype = self.visit(line.args[i],localenv)
                            #     paramtype = parent.params[i].typ
                            #     if type(paramtype) is AutoType:
                            #         # for i in range(len(localenv[-1])):
                            #         #     if localenv[-1][i].name == ctx.name:
                            #         #         for j in range(len(localenv[-1][i].params)):
                            #         #             if localenv[-1][i].params[j].name == parent.params[i].name:
                            #         #                 localenv[-1][i].params[j].typ = argtype
                            #         funcIndex = [idx for idx, element in localenv[-1] if element.name == parent.name]
                            #     if type(paramtype) is FloatType and type(argtype) is IntegerType:
                            #         continue
                            #     if type(argtype) is not type(paramtype):
                            #         raise TypeMismatchInExpression(line.args[i])
                            # --------------------------------------------------------------------------------------------
                            for i in range(len(line.args)):
                                argtype = self.visit(line.args[i],localenv)
                                paramtype = parent.params[i].typ
                                if type(paramtype) is FloatType and type(argtype) is IntegerType:
                                    continue
                                if type(paramtype) is AutoType:
                                    found = False
                                    for scopeIndex,decllist in enumerate(localenv):
                                        for declIndex, decl in enumerate(decllist):
                                            if decl.name == parent.name:
                                                for paramIndex, param in enumerate(decl.params):
                                                    if param.name == parent.params[i].name:
                                                        localenv[scopeIndex][declIndex].params[paramIndex].typ = argtype
                                                        found = True
                                                    if found == True:
                                                        break
                                            if found == True:
                                                break
                                        if found == True:
                                            break
                                    continue
                                if type(argtype) is not type(paramtype):
                                    raise TypeMismatchInExpression(line.args[i])
                            # --------------------------------------------------------------------------------------------
                    i+=1
                    continue
                if len(parent.params) == 0:
                    if type(line) is CallStmt:
                        if line.name == "preventDefault":
                            i+=1
                            continue
                        if line.name == "super":
                            if len(line.args) > 0:
                                raise TypeMismatchInExpression(line.args[len(parent.params)])
                            i+=1
                            continue


            if i == 0 and ctx.inherit is None:
                if type(line) is CallStmt:
                    if line.name == "preventDefault" or line.name == "super":
                        raise InvalidStatementInFunction(ctx.name)
            if type(line) is BreakStmt or type(line) is ContinueStmt:
                raise MustInLoop(line)
            if type(line) is ReturnStmt:
                # Xem lại cái này
                if type(ctx.return_type) is VoidType and line.expr is None:
                    o[-1] = localenv[-1]
                    return o
                if type(ctx.return_type) is AutoType and line.expr is not None:
                    retype = self.visit(line.expr,localenv)
                    for i in range(len(localenv[-1])):
                        if localenv[-1][i].name == ctx.name:
                            localenv[-1][i].return_type = retype
                    o[-1] = localenv[-1]
                    return o
                if type(ctx.return_type) is not VoidType and line.expr is None:
                    raise TypeMismatchInStatement(line)
                if type(ctx.return_type) is type(self.visit(line.expr, localenv)):
                    o[-1] = localenv[-1]
                    return o
                raise TypeMismatchInStatement(line)
            localenv = self.visit(line,localenv)
            i+=1
        o[-1] = localenv[-1]
        return o




    def visitBinExpr(self, ctx:BinExpr, o):
        ltype = self.visit(ctx.left, o)
        rtype = self.visit(ctx.right, o)
        # Arithmetic operator
        if ctx.op in ['+', '-', '*', '/']:
            if type(ltype) is AutoType:
                if type(rtype) is IntegerType or type(rtype) is FloatType:
                    for i in range(len(o[-1])):
                        if o[-1][i].name == ctx.left.name:
                            o[-1][i].return_type = rtype
                            return rtype

            if type(rtype) is AutoType:
                if type(ltype) is IntegerType or type(ltype) is FloatType:
                    for i in range(len(o[-1])):
                        if o[-1][i].name == ctx.right.name:
                            o[-1][i].return_type = ltype
                            return ltype
            if type(ltype) is FloatType and type(rtype) is FloatType:
                return FloatType()
            if type(ltype) is IntegerType and type(rtype) is IntegerType:
                return IntegerType()
            if type(ltype) is IntegerType and type(rtype) is FloatType:
                return FloatType()
            if type(ltype) is FloatType and type(rtype) is IntegerType:
                return FloatType()
            raise TypeMismatchInExpression(ctx)
        if ctx.op in ['%']:
            if type(ltype) is AutoType:
                if type(rtype) is IntegerType:
                    for i in range(len(o[-1])):
                        if o[-1][i].name == ctx.left.name:
                            o[-1][i].return_type = rtype
                            return rtype

            if type(rtype) is AutoType:
                if type(ltype) is IntegerType:
                    for i in range(len(o[-1])):
                        if o[-1][i].name == ctx.right.name:
                            o[-1][i].return_type = ltype
                            return ltype
            
            if type(ltype) is IntegerType and type(rtype) is IntegerType:
                return IntegerType()
            raise TypeMismatchInExpression(ctx)
        # Boolean operator
        if ctx.op in ['||','&&']:
            if type(ltype) is AutoType:
                if type(rtype) is BooleanType:
                    for i in range(len(o[-1])):
                        if o[-1][i].name == ctx.left.name:
                            o[-1][i].return_type = rtype
                            return rtype

            if type(rtype) is AutoType:
                if type(ltype) is BooleanType:
                    for i in range(len(o[-1])):
                        if o[-1][i].name == ctx.right.name:
                            o[-1][i].return_type = ltype
                            return ltype
            
            if type(ltype) is BooleanType and type(rtype) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ctx)
        # String operator
        if ctx.op in ['::']:
            if type(ltype) is AutoType:
                if type(rtype) is StringType:
                    for i in range(len(o[-1])):
                        if o[-1][i].name == ctx.left.name:
                            o[-1][i].return_type = rtype
                            return rtype

            if type(rtype) is AutoType:
                if type(ltype) is StringType:
                    for i in range(len(o[-1])):
                        if o[-1][i].name == ctx.right.name:
                            o[-1][i].return_type = ltype
                            return ltype
            
            if type(ltype) is StringType and type(rtype) is StringType:
                return StringType()
            raise TypeMismatchInExpression(ctx)
        # Relational operator
        if ctx.op in ['==','!=', '>', '<', '>=', '<=']:
            if type(ltype) is AutoType:
                if type(rtype) is IntegerType or type(rtype) is FloatType:
                    for i in range(len(o[-1])):
                        if o[-1][i].name == ctx.left.name:
                            o[-1][i].return_type = rtype
                            return BooleanType()
                if ctx.op in ['==','!='] and type(rtype) is BooleanType:
                    for i in range(len(o[-1])):
                        if o[-1][i].name == ctx.left.name:
                            o[-1][i].return_type = rtype
                            return BooleanType()

            if type(rtype) is AutoType:
                if type(ltype) is IntegerType or type(ltype) is FloatType:
                    for i in range(len(o[-1])):
                        if o[-1][i].name == ctx.right.name:
                            o[-1][i].return_type = ltype
                            return BooleanType()
                if ctx.op in ['==','!='] and type(ltype) is BooleanType:
                    for i in range(len(o[-1])):
                        if o[-1][i].name == ctx.right.name:
                            o[-1][i].return_type = ltype
                            return BooleanType()

            if type(ltype) is FloatType and type(rtype) is FloatType:
                return BooleanType()
            if type(ltype) is IntegerType and type(rtype) is IntegerType:
                return BooleanType()
            if type(ltype) is IntegerType and type(rtype) is FloatType:
                return BooleanType()
            if type(ltype) is FloatType and type(rtype) is IntegerType:
                return BooleanType()
            if ctx.op in ['==','!='] and type(ltype) is BooleanType and type(rtype) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ctx)

    def visitUnExpr(self, ctx:UnExpr, o): 
        valtype = self.visit(ctx.val, o)
        # Arithmetic operator
        if ctx.op in ['-']:
            if type(valtype) is IntegerType:
                return IntegerType()
            if type(valtype) is FloatType:
                return FloatType()
            raise TypeMismatchInExpression(ctx)
        # Boolean operator
        if ctx.op in ['!']:
            if type(valtype) is AutoType:
                for i in range(len(o[-1])):
                    if o[-1][i].name == ctx.val.name:
                        o[-1][i].return_type = BooleanType()
                        return BooleanType()
            if type(valtype) is BooleanType:
                return BooleanType()
            raise TypeMismatchInExpression(ctx)




    def visitId(self, ctx:Id, o):
        for decllist in o:
            for decl in decllist:
                if decl.name == ctx.name:
                    if type(decl) is FuncDecl:
                        return decl.return_type
                    else:
                        return decl.typ
        raise Undeclared(Identifier(),ctx.name)
    

    def visitArrayCell(self, ctx:ArrayCell, o):
        arrtype = self.visit(Id(ctx.name),o)
        if type(arrtype) is not ArrayType:
            raise TypeMismatchInExpression(ctx)
        if len(arrtype.dimensions) != len(ctx.cell):
            raise TypeMismatchInExpression(ctx)
        for indexNum in ctx.cell:
            indexType = self.visit(indexNum,o)
            if type(indexType) is not IntegerType:
                raise TypeMismatchInExpression(ctx)
        # Find type of cell
        celltype = 0
        for decllist in o:
            for decl in decllist:
                if decl.name == ctx.name:
                    celltype = decl.typ.typ
                    break
        return celltype

    def visitIntegerLit(self, ctx:IntegerLit, o):
        return IntegerType()
    def visitFloatLit(self, ctx:FloatLit, o):
        return FloatType()
    def visitStringLit(self, ctx:StringLit, o):
        return StringType()
    def visitBooleanLit(self, ctx:BooleanLit, o):
        return BooleanType()
    def visitArrayLit(self, ctx:ArrayLit, o):
        arraytyp = []
        currtyp = 0
        for lit in ctx.explist:
            currtyp = self.visit(lit,o)
            arraytyp += [currtyp]
            if len(arraytyp) > 1:
                if type(arraytyp[-2]) is FloatType and  type(arraytyp[-1]) is IntegerType:
                    arraytyp[-1] = FloatType()
                    currtyp = FloatType()
                    continue
                if type(arraytyp[-1]) is FloatType and  type(arraytyp[-2]) is IntegerType:
                    arraytyp[-2] = FloatType()
                    currtyp = FloatType()
                    continue
                if type(arraytyp[-1]) is not type(arraytyp[-2]):
                    raise IllegalArrayLiteral(ctx)
        return currtyp
    def visitFuncCall(self, ctx:FuncCall, o):
        # check if function exist
        refunc = 0
        found = False
        for scopeIndex,decllist in enumerate(o):
            for declIndex, decl in enumerate(decllist):
                if decl.name == ctx.name:
                    found = True
                    refunc = decl
                    break
            if found == True:
                break       
        if found == False:
            raise Undeclared(Function(), ctx.name)
        # xem lại
        if type(refunc) is not FuncDecl:
            raise TypeMismatchInExpression(ctx)
        # Check return type of function
        if type(refunc.return_type) is VoidType:
            raise TypeMismatchInExpression(ctx)
        # Check len of arg and param
        if len(ctx.args) != len(refunc.params):
            raise TypeMismatchInExpression(ctx)
        # Check type of arg and param
        for i in range(len(ctx.args)):
            argtype = self.visit(ctx.args[i],o)
            paramtype = refunc.params[i].typ
            if type(paramtype) is FloatType and type(argtype) is IntegerType:
                continue
            if type(paramtype) is AutoType:
                found = False
                for scopeIndex,decllist in enumerate(o):
                    for declIndex, decl in enumerate(decllist):
                        if decl.name == refunc.name:
                            for paramIndex, param in enumerate(decl.params):
                                if param.name == refunc.params[i].name:
                                    o[scopeIndex][declIndex].params[paramIndex].typ = argtype
                                    found = True
                                if found == True:
                                    break
                        if found == True:
                            break
                    if found == True:
                        break
                continue
            if type(argtype) is not type(paramtype):
                raise TypeMismatchInExpression(ctx)
        return refunc.return_type

    def visitAssignStmt(self, ctx:AssignStmt, o):
        left = self.visit(ctx.lhs,o)
        right = self.visit(ctx.rhs, o)
        if type(left) is VoidType or type(left) is ArrayType:
            raise TypeMismatchInStatement(ctx)
        if type(left) is FloatType and type(right) is IntegerType:
            return o
        # infer type first usage for auto function
        if type(right) is AutoType:
            for i in range(len(o[-1])):
                if o[-1][i].name == ctx.rhs.name:
                    o[-1][i].return_type = left
        if type(left) is not type(right):
            raise TypeMismatchInStatement(ctx)
        return o



    def visitBlockStmt(self, ctx:BlockStmt, o):
        for line in ctx.body:
            o = self.visit(line,o)
        return o
    def visitIfStmt(self, ctx:IfStmt, o):
        env = [[]] + o
        if type(self.visit(ctx.cond,o)) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        if type(ctx.tstmt) is BlockStmt:
            for line in ctx.tstmt.body:
                if type(line) is BreakStmt or type(line) is ContinueStmt:
                    raise MustInLoop(line)
                env = self.visit(line,env)
            return o
        line = self.visit(line,env)
        if type(line) is BreakStmt or type(line) is ContinueStmt:
            raise MustInLoop(line)
        o[-1] = env[-1]
        return o

    def visitForStmt(self, ctx:ForStmt, o):
        o = self.visit(ctx.init,o)
        if type(self.visit(ctx.init.rhs,o)) is not IntegerType:
            raise TypeMismatchInStatement(ctx)
        env = [[]] + o
        if type(self.visit(ctx.cond, env)) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        if type(self.visit(ctx.upd, env)) is not IntegerType:
            raise TypeMismatchInStatement(ctx)
        # xem lại nên dùng block hay ko
        env = self.visit(ctx.stmt, env)
        o[-1] = env[-1]
        return o
    def visitWhileStmt(self, ctx:WhileStmt, o):
        if type(self.visit(ctx.cond,o)) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        env = [[]] + o
        env = self.visit(ctx.stmt, env)
        o[-1] = env[-1]
        return o
    
    def visitDoWhileStmt(self, ctx:DoWhileStmt, o):
        if type(self.visit(ctx.cond,o)) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        env = [[]] + o
        env = self.visit(ctx.stmt, env)
        o[-1] = env[-1]
        return o
    def visitBreakStmt(self, ctx:BreakStmt, o):
        return o
    def visitContinueStmt(self, ctx:ContinueStmt, o):
        return o
    def visitReturnStmt(self, ctx:ReturnStmt, o):
        return o
    def visitCallStmt(self, ctx:CallStmt, o):
        # check if function exist
        refunc = 0
        found = False
        for decllist in o:
            for decl in decllist:
                if decl.name == ctx.name:
                    found = True
                    refunc = decl
            if found == True:
                break   
        if found == False:
            raise Undeclared(Function(), ctx.name)
        # xem lại
        if type(refunc) is not FuncDecl:
            raise TypeMismatchInExpression(ctx)
        # Check len of arg and param
        if len(ctx.args) != len(refunc.params):
            raise TypeMismatchInExpression(ctx)
        # Check type of arg and param
        for i in range(len(ctx.args)):
            argtype = self.visit(ctx.args[i],o)
            paramtype = refunc.params[i].typ
            if type(paramtype) is FloatType and type(argtype) is IntegerType:
                continue
            if type(paramtype) is AutoType:
                found = False
                for scopeIndex,decllist in enumerate(o):
                    for declIndex, decl in enumerate(decllist):
                        if decl.name == refunc.name:
                            for paramIndex, param in enumerate(decl.params):
                                if param.name == refunc.params[i].name:
                                    o[scopeIndex][declIndex].params[paramIndex].typ = argtype
                                    found = True
                                if found == True:
                                    break
                        if found == True:
                            break
                    if found == True:
                        break
                continue
            if type(argtype) is not type(paramtype):
                raise TypeMismatchInStatement(ctx)
        return o

    def visitIntegerType(self, ctx:IntegerType, o):
        return IntegerType()
    def visitFloatType(self,  ctx:FloatType, o): 
        return FloatType()
    def visitBooleanType(self,  ctx:BooleanType, o): 
        return BooleanType()
    def visitStringType(self,  ctx:StringType, o): 
        return StringType()
    def visitArrayType(self,  ctx:ArrayType, o): 
        return ArrayType(ctx.dimensions, ctx.typ)
    def visitAutoType(self,  ctx:AutoType, o): 
        return AutoType()
    def visitVoidType(self,  ctx:VoidType, o): 
        return VoidType()