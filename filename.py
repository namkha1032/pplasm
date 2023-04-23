# Cau 0
import functools
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object):
        o = [[]]
        for decl in ctx.decl:
            o = self.visit(decl,o)
        return o
        # return functools.reduce(lambda prev, curr: self.visit(curr,prev), ctx.decl, o)

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredVariable(ctx.name)
        o[0] += [ctx.name]
        return o
        
    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredConstant(ctx.name)
        o[0] += [ctx.name]
        return o
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredFunction(ctx.name)
        o[0] += [ctx.name]
        env = [[]] + o
        
        for decl in ctx.param:
            env = self.visit(decl,env)
        for decl in ctx.body[0]:
            env = self.visit(decl,env)
        
        # # Check param
        # env = functools.reduce(lambda prev, curr: self.visit(curr, prev), ctx.param, env)
        # # Check body
        # env = functools.reduce(lambda prev, curr: self.visit(curr, prev), ctx.body[0], env)
        
        for expr in ctx.body[1]:
            self.visit(expr,env)
        # Có thể phải return env
        return o
            
    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

    def visitId(self,ctx:Id,o:object):
        for env in o:
            if ctx.name in env: return
        raise UndeclaredIdentifier(ctx.name)
######################################################################
# cau 1
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o:object): 
        o = []
        for decl in ctx.decl:
            o = self.visit(decl,o)
        return o
 
    def visitClassDecl(self,ctx:ClassDecl,o:object):
        env = []
        for mem in ctx.mem:
            env = self.visit(mem,o)
        return o + [(ctx.name, ctx.parent, env)]
    
    def visitVarDecl(self,ctx:VarDecl,o:object):
        for decl in o:
            if decl.name == ctx.name:
                raise RedeclaredField(ctx.name)
        return o + [ctx]
 
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        for decl in o:
            if decl.name == ctx.name:
                raise RedeclaredMethod(ctx.name)
        return o + [ctx]
    def visitIntType(self,ctx:IntType,o:object):pass
 
    def visitFloatType(self,ctx:FloatType,o:object):pass
 
    def visitClassType(self,ctx:ClassType,o:object):pass
 
    def visitIntLit(self,ctx:IntLit,o:object):pass
 
    def visitId(self,ctx:Id,o:object):pass
 
    def visitFieldAccess(self,ctx:FieldAccess,o:object):pass
######################################################################
# Cau 2
class GetEnv(Visitor):
    def visitProgram(self,ctx:Program,o:object): 
        o = []
        for decl in ctx.decl:
            o = self.visit(decl,o)
        return o
 
    def visitClassDecl(self,ctx:ClassDecl,o:object):
        env = []
        for mem in ctx.mem:
            # Chỗ này có thể là self.visit(mem,env)
            env = self.visit(mem,o)
        return o + [(ctx.name, ctx.parent, env)]
    
    def visitVarDecl(self,ctx:VarDecl,o:object):
        for decl in o:
            if decl.name == ctx.name:
                raise RedeclaredField(ctx.name)
        return o + [ctx]
 
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        for decl in o:
            if decl.name == ctx.name:
                raise RedeclaredMethod(ctx.name)
        return o + [ctx]
 
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o:object): 
        o = GetEnv().visit(ctx, o)
        # print(env)
        for class_decl in ctx.decl:
            self.visit(class_decl, o)
 
    def visitClassDecl(self,ctx:ClassDecl,o:object):
        for mem in ctx.mem:
            if type(mem) is FuncDecl:
                self.visit(mem, o)
 
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        local = ctx.param + ctx.body[0]
        for expr in ctx.body[1]:
            self.visit(expr, (local, o))
 
    def visitId(self,ctx:Id,o:object):
        for decl in o[0]:
            if decl.name == ctx.name:
                return decl.typ
        raise UndeclaredIdentifier(ctx.name)
 
    def visitFieldAccess(self,ctx:FieldAccess,o:object):
        typ = self.visit(ctx.exp, o)
        if type(typ) is ClassType:
            type_info = None
            found = False
            for classdecl in o[1]:
                if typ.name == classdecl[0]:
                    type_info = classdecl
                    found = True
                    break
 
            if not found: raise UndeclaredClass(typ.name)
 
            for mem in type_info[2]:
                if mem.name == ctx.field:
                    return mem.typ
            raise UndeclaredField(ctx.field)