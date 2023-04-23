import unittest
from TestUtils import TestChecker
from AST import *
 
class CheckerSuite(unittest.TestCase):
    def test300(self):
        input = """main: function void(){
                    a: integer;
                    b: integer;
                    c: integer;
                    i: integer;
                    for (i=0, i < 10, i+1){
                        a: integer;
                        d: integer;
                        f: float;
                        if (a == d){
                            a: integer;
                            d: integer;
                            f: string;
                        }
                        while(1 == 2){
                            a: integer;
                        }
                    }
                    do{
                        c: integer;
                        f: float;
                    }
                    while(a==f);
        
                   }"""
        expect = "Undeclared Identifier: f"
        self.assertTrue(TestChecker.test(input, expect, 300))
        
    def test301(self):
        input = """a:integer=5;
                    c:auto=1.5;
                    main: function void(){
                        c=a;
                    }
                    a:float;"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 301))

    
    def test302(self):
        input = """a:integer=5;
                    c:auto=1.5;
                    main: function void(){
                        c=a;
                    }
                    main: function void(){
                    }
                    a:float;"""
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 302))

    
    def test303(self):
        input = """a:integer=5;
                    c:auto=1.5;
                    foo: function void(){
                        c=a;
                    }
                    foo: function void(){
                    }
                    a:float;"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 303))
        
    
    def test304(self):
        input = """a:integer=5;
                    c:auto=1.5;
                    foo: function void(){
                        c=a;
                    }
                    inc: function void(){
                    }
                    d:float;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 304))
        
    
    def test305(self):
        input = """foo: function void(){
                        inc();
                    }
                    inc: function void(){
                    }
                    d:float;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 305))

    def test306(self):
        input = """
                    a:integer;
                    foo: function void(){
                        a: float;
                        b: string;
                        b: integer;
                        inc();
                    }
                    inc: function void(){
                    }
                    d:float;"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 306))

    def test307(self):
        input = """
                    a:integer;
                    str:string;
                    f:float;
                    main:function void(){
                        if(a == f){
                            a:integer;
                            c:float;
                            c:string;
                        }
                        else{
                            d:integer;
                        }
                    }
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 307))

    def test308(self):
        input = """
                    a:auto;
                """
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 308))

    def test309(self):
        input = """
                    a:integer;
                    str:string;
                    f:float;
                    main:function void(){
                        if(a == f){
                            a:integer;
                            c:float;
                            str:auto;
                        }
                        else{
                            d:integer;
                        }
                    }
                """
        expect = "Invalid Variable: str"
        self.assertTrue(TestChecker.test(input, expect, 309))

    def test310(self):
        input = """
                    a:integer;
                    str:string;
                    f:float;
                    main:function void(){
                        if(a == f){
                            a:integer;
                            c:float;
                            str:auto;
                        }
                        else{
                            d:integer;
                        }
                    }
                """
        expect = "Invalid Variable: str"
        self.assertTrue(TestChecker.test(input, expect, 310))

    def test311(self):
        input = """
                    sum: function integer(a: integer, b: integer){
                        return a + b;
                    }
                    main: function void(){
                        x: integer;
                        sum: integer;
                        x = sum(1,2);
                    }
                """
        expect = "Type mismatch in expression: FuncCall(sum, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 311))

    def test312(self):
        input = """
                    sum: function integer(a: auto){
                        return 2;
                    }
                    main: function void(){
                        x: integer;
                        sum(1);
                        y: float;
                        sum(1.1);
                    }
                """
        expect = "Type mismatch in statement: CallStmt(sum, FloatLit(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 312))

    def test313(self):
        input = """
                    sum: function integer(a: auto){
                        return 2;
                    }
                    main: function void(){
                        x: integer;
                        sum(1);
                        y: float;
                        //sum(1.1);
                    }
                    foo: function void(){
                        sum(2);
                        sum(2.2);
                    }
                """
        expect = "Type mismatch in statement: CallStmt(sum, FloatLit(2.2))"
        self.assertTrue(TestChecker.test(input, expect, 313))

    def test314(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super(1,2);
                        return 0;
                    }
                    child2: function integer(p: integer, q: integer) inherit parent{
                        super(1.1,2.2);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: FloatLit(1.1)"
        self.assertTrue(TestChecker.test(input, expect, 314))

    def test315(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 315))

    def test316(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        grand();
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 316))

    def test317(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super(a,b,c);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: Id(c)"
        self.assertTrue(TestChecker.test(input, expect, 317))

    def test318(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super("hehe","haha","namkha");
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: StringLit(namkha)"
        self.assertTrue(TestChecker.test(input, expect, 318))

    def test319(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super("adu");
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 319))

    def test320(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:integer) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super("adu", 123);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 320))

    def test321(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:integer) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super("adu", 123);
                        return 0;
                    }
                    child2: function integer(m: integer, n: integer) inherit parent{
                        super(1, 1.2);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, expect, 321))

    def test322(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:integer) inherit grand{
                        super("vip", 123, true);
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super("adu", 123);
                        return 0;
                    }
                    child2: function integer(m: integer, n: integer) inherit parent{
                        super(1, 1.2);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: StringLit(vip)"
        self.assertTrue(TestChecker.test(input, expect, 322))

    def test323(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:integer) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super("adu", 123);
                        return 0;
                    }
                    foo: function void(){
                        preventDefault();
                        a = 123;
                    }
                    child2: function integer(m: integer, n: integer) inherit parent{
                        super(1, 1.2);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 323))

    def test324(self):
        input = """
                    main: function void(){
                        break;
                        continue;
                    }
                    c:integer;
                """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 324))

    def test325(self):
        input = """
                    main: function void(){
                        if (1>2){
                            continue;
                        }
                    }
                    c:integer;
                """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 325))

    def test326(self):
        input = """
                    c: string;
                    main: function void(){
                    i: integer;
                        if (1>2){
                            for(i=1,i<10,i+1){
                                a: integer;
                                break;
                            }
                        }
                    }
                    c:integer;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 326))

    def test327(self):
        input = """
                    c: string;
                    main: function void(){
                        i: integer;
                        if (1>2){
                        }
                        while(i<10){
                            i = i + 1;
                            continue;
                        }
                    }
                    c:integer;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 327))

    def test328(self):
        input = """
                    c: string;
                    main: function void(){
                        i: integer;
                        if (1>2){
                            d: integer;
                        }
                        do{
                            break;
                            continue;
                            i = i + 1;
                        }
                        while(i<10);
                    }
                    c:integer;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 328))

    def test329(self):
        input = """
                    c: string;
                    foo: function void(){
                        return 2;
                    }
                    main: function void(){
                        i: integer;
                        if (1>2){
                        }
                        while(i<10){
                            i = i + 1;
                            continue;
                        }
                    }
                    c:integer;
                """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 329))

    def test330(self):
        input = """
                    c: string;
                    foo: function void(){
                        return;
                    }
                    main: function void(){
                        i: integer;
                        if (1>2){
                        }
                        while(i<10){
                            i = i + 1;
                            continue;
                        }
                    }
                    c:integer;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 330))

    def test331(self):
        input = """
                    c: string;
                    foo: function void(){
                        return;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 331))

    def test332(self):
        input = """
                    c: string;
                    foo: function auto(x: auto){
                        return x;
                    }
                    main: function void(){
                        num: float = foo(1);
                        num2: integer = foo(2);

                    }
                    c:integer;
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(num2, IntegerType, FuncCall(foo, [IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 332))

    def test333(self):
        input = """
                    c: string;
                    foo: function auto(x: auto){
                        return x;
                    }
                    main: function void(){
                        num: integer = foo(1);
                        num2: float = foo(2);

                    }
                    c:integer;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 333))

    def test334(self):
        input = """
                    c: string;
                    foo: function auto(x: auto, c:string, c:auto){
                        return x;
                    }
                    main: function void(){
                        num: integer = foo(1);
                        num2: float = foo(2);

                    }
                    c:integer;
                """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 334))

    def test335(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:integer) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer,x:string, n: integer) inherit parent{
                        super("adu", 123);
                        return 0;
                    }
                    foo: function void(){
                        preventDefault();
                        a = 123;
                    }
                    child2: function integer(m: integer,x:float, n: integer) inherit parent{
                        super(1, 1.2);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Invalid Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 335))

    def test336(self):
        input = """ c: string = "namkha";
                    main: function void(){
                        a: float;
                        a = c[1];
                    }
                """
        expect = "Type mismatch in expression: ArrayCell(c, [IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 336))

    def test337(self):
        input = """ c: array[5] of integer = {1,2,3};
                    main: function void(){
                        a: float;
                        a = c[1];
                    }
                    c: string;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 337))

    def test338(self):
        input = """ c: array[5] of integer = {1,2,3};
                    main: function void(){
                        a: float;
                        a = c[1,2];
                    }
                    c: string;
                """
        expect = "Type mismatch in expression: ArrayCell(c, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 338))

    def test339(self):
        input = """ c: array[5] of integer = {"abc","abc","abc"};
                    main: function void(){
                        a: float;
                        a = c[1,2];
                    }
                    c: string;
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(c, ArrayType([5], IntegerType), ArrayLit([StringLit(abc), StringLit(abc), StringLit(abc)]))"
        self.assertTrue(TestChecker.test(input, expect, 339))

    def test340(self):
        input = """ c: array[5] of integer = {1,1.2,1.2};
                    main: function void(){
                        a: float;
                        a = c[1,2];
                    }
                    c: string;
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(c, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), FloatLit(1.2), FloatLit(1.2)]))"
        self.assertTrue(TestChecker.test(input, expect, 340))

    def test341(self):
        input = """ c: array[5] of float = {1.2,1,1.2};
                    main: function void(){
                        a: float;
                        a = c[1];
                    }
                    c: string;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 341))

    def test342(self):
        input = """ c: auto = 1.5;
                    main: function void(){
                        b: integer = c;
                    }
                    c: string;
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 342))

    def test343(self):
        input = """ 
                    main: function void(){
                        c: auto = 1.5;
                        b: integer = c;
                    }
                    c: string;
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 343))
    
        
    def test344(self):
        input = """a:integer=5;
                    c:auto=1.5;
                    foo: function void(){
                        c=a;
                    }
                    inc: function void(){
                    }
                    d:float;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 344))
        
    
    def test345(self):
        input = """foo: function void(){
                        inc();
                    }
                    inc: function void(){
                    }
                    d:float;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 345))

    def test346(self):
        input = """
                    a:integer;
                    foo: function void(){
                        a: float;
                        b: string;
                        b: integer;
                        inc();
                    }
                    inc: function void(){
                    }
                    d:float;"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 346))

    def test347(self):
        input = """
                    a:integer;
                    str:string;
                    f:float;
                    main:function void(){
                        if(a == f){
                            a:integer;
                            c:float;
                            c:string;
                        }
                        else{
                            d:integer;
                        }
                    }
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 347))

    def test348(self):
        input = """
                    a:auto;
                """
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 348))

    def test349(self):
        input = """
                    a:integer;
                    str:string;
                    f:float;
                    main:function void(){
                        if(a == f){
                            a:integer;
                            c:float;
                            str:auto;
                        }
                        else{
                            d:integer;
                        }
                    }
                """
        expect = "Invalid Variable: str"
        self.assertTrue(TestChecker.test(input, expect, 349))

    def test350(self):
        input = """
                    a:integer;
                    str:string;
                    f:float;
                    main:function void(){
                        if(a == f){
                            a:integer;
                            c:float;
                            str:auto;
                        }
                        else{
                            d:integer;
                        }
                    }
                """
        expect = "Invalid Variable: str"
        self.assertTrue(TestChecker.test(input, expect, 350))

    def test351(self):
        input = """
                    sum: function integer(a: integer, b: integer){
                        return a + b;
                    }
                    main: function void(){
                        x: integer;
                        sum: integer;
                        x = sum(1,2);
                    }
                """
        expect = "Type mismatch in expression: FuncCall(sum, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 351))

    def test352(self):
        input = """
                    sum: function integer(a: auto){
                        return 2;
                    }
                    main: function void(){
                        x: integer;
                        sum(1);
                        y: float;
                        sum(1.1);
                    }
                """
        expect = "Type mismatch in statement: CallStmt(sum, FloatLit(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 352))

    def test353(self):
        input = """
                    sum: function integer(a: auto){
                        return 2;
                    }
                    main: function void(){
                        x: integer;
                        sum(1);
                        y: float;
                        //sum(1.1);
                    }
                    foo: function void(){
                        sum(2);
                        sum(2.2);
                    }
                """
        expect = "Type mismatch in statement: CallStmt(sum, FloatLit(2.2))"
        self.assertTrue(TestChecker.test(input, expect, 353))

    def test354(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super(1,2);
                        return 0;
                    }
                    child2: function integer(p: integer, q: integer) inherit parent{
                        super(1.1,2.2);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: FloatLit(1.1)"
        self.assertTrue(TestChecker.test(input, expect, 354))

    def test355(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 355))

    def test356(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        grand();
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 356))

    def test357(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super(a,b,c);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: Id(c)"
        self.assertTrue(TestChecker.test(input, expect, 357))

    def test358(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super("hehe","haha","namkha");
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: StringLit(namkha)"
        self.assertTrue(TestChecker.test(input, expect, 358))

    def test359(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super("adu");
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 359))

    def test360(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:integer) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super("adu", 123);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 360))

    def test361(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:integer) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super("adu", 123);
                        return 0;
                    }
                    child2: function integer(m: integer, n: integer) inherit parent{
                        super(1, 1.2);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, expect, 361))

    def test362(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:integer) inherit grand{
                        super("vip", 123, true);
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super("adu", 123);
                        return 0;
                    }
                    child2: function integer(m: integer, n: integer) inherit parent{
                        super(1, 1.2);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: StringLit(vip)"
        self.assertTrue(TestChecker.test(input, expect, 362))

    def test363(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:integer) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super("adu", 123);
                        return 0;
                    }
                    foo: function void(){
                        preventDefault();
                        a = 123;
                    }
                    child2: function integer(m: integer, n: integer) inherit parent{
                        super(1, 1.2);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 363))

    def test364(self):
        input = """
                    main: function void(){
                        break;
                        continue;
                    }
                    c:integer;
                """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 364))

    def test365(self):
        input = """
                    main: function void(){
                        if (1>2){
                            continue;
                        }
                    }
                    c:integer;
                """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 365))

    def test366(self):
        input = """
                    c: string;
                    main: function void(){
                    i: integer;
                        if (1>2){
                            for(i=1,i<10,i+1){
                                a: integer;
                                break;
                            }
                        }
                    }
                    c:integer;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 366))

    def test367(self):
        input = """
                    c: string;
                    main: function void(){
                        i: integer;
                        if (1>2){
                        }
                        while(i<10){
                            i = i + 1;
                            continue;
                        }
                    }
                    c:integer;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 367))

    def test368(self):
        input = """
                    c: string;
                    main: function void(){
                        i: integer;
                        if (1>2){
                            d: integer;
                        }
                        do{
                            break;
                            continue;
                            i = i + 1;
                        }
                        while(i<10);
                    }
                    c:integer;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 368))

    def test369(self):
        input = """
                    c: string;
                    foo: function void(){
                        return 2;
                    }
                    main: function void(){
                        i: integer;
                        if (1>2){
                        }
                        while(i<10){
                            i = i + 1;
                            continue;
                        }
                    }
                    c:integer;
                """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 369))

    def test370(self):
        input = """
                    c: string;
                    foo: function void(){
                        return;
                    }
                    main: function void(){
                        i: integer;
                        if (1>2){
                        }
                        while(i<10){
                            i = i + 1;
                            continue;
                        }
                    }
                    c:integer;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 370))

    def test371(self):
        input = """
                    c: string;
                    foo: function void(){
                        return;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 371))

    def test372(self):
        input = """
                    c: string;
                    foo: function auto(x: auto){
                        return x;
                    }
                    main: function void(){
                        num: float = foo(1);
                        num2: integer = foo(2);

                    }
                    c:integer;
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(num2, IntegerType, FuncCall(foo, [IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 372))

    def test373(self):
        input = """
                    c: string;
                    foo: function auto(x: auto){
                        return x;
                    }
                    main: function void(){
                        num: integer = foo(1);
                        num2: float = foo(2);

                    }
                    c:integer;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 373))

    def test374(self):
        input = """
                    c: string;
                    foo: function auto(x: auto, c:string, c:auto){
                        return x;
                    }
                    main: function void(){
                        num: integer = foo(1);
                        num2: float = foo(2);

                    }
                    c:integer;
                """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 374))

    def test375(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:integer) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer,x:string, n: integer) inherit parent{
                        super("adu", 123);
                        return 0;
                    }
                    foo: function void(){
                        preventDefault();
                        a = 123;
                    }
                    child2: function integer(m: integer,x:float, n: integer) inherit parent{
                        super(1, 1.2);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Invalid Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 375))

    def test376(self):
        input = """ c: string = "namkha";
                    main: function void(){
                        a: float;
                        a = c[1];
                    }
                """
        expect = "Type mismatch in expression: ArrayCell(c, [IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 376))

    def test377(self):
        input = """ c: array[5] of integer = {1,2,3};
                    main: function void(){
                        a: float;
                        a = c[1];
                    }
                    c: string;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 377))

    def test378(self):
        input = """ c: array[5] of integer = {1,2,3};
                    main: function void(){
                        a: float;
                        a = c[1,2];
                    }
                    c: string;
                """
        expect = "Type mismatch in expression: ArrayCell(c, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 378))

    def test379(self):
        input = """ c: array[5] of integer = {"abc","abc","abc"};
                    main: function void(){
                        a: float;
                        a = c[1,2];
                    }
                    c: string;
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(c, ArrayType([5], IntegerType), ArrayLit([StringLit(abc), StringLit(abc), StringLit(abc)]))"
        self.assertTrue(TestChecker.test(input, expect, 379))

    def test380(self):
        input = """ c: array[5] of integer = {1,1.2,1.2};
                    main: function void(){
                        a: float;
                        a = c[1,2];
                    }
                    c: string;
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(c, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), FloatLit(1.2), FloatLit(1.2)]))"
        self.assertTrue(TestChecker.test(input, expect, 380))

    def test381(self):
        input = """ c: array[5] of float = {1.2,1,1.2};
                    main: function void(){
                        a: float;
                        a = c[1];
                    }
                    c: string;
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 381))

    def test382(self):
        input = """ c: auto = 1.5;
                    main: function void(){
                        b: integer = c;
                    }
                    c: string;
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 382))

    def test383(self):
        input = """ 
                    main: function void(){
                        c: auto = 1.5;
                        b: integer = c;
                    }
                    c: string;
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 383))
    
    def test384(self):
        input = """a:integer=5;
                    c:auto=1.5;
                    foo: function void(){
                        c=a;
                    }
                    inc: function void(){
                    }
                    d:float;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 384))
        
    
    def test385(self):
        input = """foo: function void(){
                        inc();
                    }
                    inc: function void(){
                    }
                    d:float;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 385))

    def test386(self):
        input = """
                    a:integer;
                    foo: function void(){
                        a: float;
                        b: string;
                        b: integer;
                        inc();
                    }
                    inc: function void(){
                    }
                    d:float;"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 386))

    def test387(self):
        input = """
                    a:integer;
                    str:string;
                    f:float;
                    main:function void(){
                        if(a == f){
                            a:integer;
                            c:float;
                            c:string;
                        }
                        else{
                            d:integer;
                        }
                    }
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 387))

    def test388(self):
        input = """
                    a:auto;
                """
        expect = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 388))

    def test389(self):
        input = """
                    a:integer;
                    str:string;
                    f:float;
                    main:function void(){
                        if(a == f){
                            a:integer;
                            c:float;
                            str:auto;
                        }
                        else{
                            d:integer;
                        }
                    }
                """
        expect = "Invalid Variable: str"
        self.assertTrue(TestChecker.test(input, expect, 389))

    def test390(self):
        input = """
                    a:integer;
                    str:string;
                    f:float;
                    main:function void(){
                        if(a == f){
                            a:integer;
                            c:float;
                            str:auto;
                        }
                        else{
                            d:integer;
                        }
                    }
                """
        expect = "Invalid Variable: str"
        self.assertTrue(TestChecker.test(input, expect, 390))

    def test391(self):
        input = """
                    sum: function integer(a: integer, b: integer){
                        return a + b;
                    }
                    main: function void(){
                        x: integer;
                        sum: integer;
                        x = sum(1,2);
                    }
                """
        expect = "Type mismatch in expression: FuncCall(sum, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 391))

    def test392(self):
        input = """
                    sum: function integer(a: auto){
                        return 2;
                    }
                    main: function void(){
                        x: integer;
                        sum(1);
                        y: float;
                        sum(1.1);
                    }
                """
        expect = "Type mismatch in statement: CallStmt(sum, FloatLit(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 392))

    def test393(self):
        input = """
                    sum: function integer(a: auto){
                        return 2;
                    }
                    main: function void(){
                        x: integer;
                        sum(1);
                        y: float;
                        //sum(1.1);
                    }
                    foo: function void(){
                        sum(2);
                        sum(2.2);
                    }
                """
        expect = "Type mismatch in statement: CallStmt(sum, FloatLit(2.2))"
        self.assertTrue(TestChecker.test(input, expect, 393))

    def test394(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super(1,2);
                        return 0;
                    }
                    child2: function integer(p: integer, q: integer) inherit parent{
                        super(1.1,2.2);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: FloatLit(1.1)"
        self.assertTrue(TestChecker.test(input, expect, 394))

    def test395(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 395))

    def test396(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        grand();
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 396))

    def test397(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super(a,b,c);
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: Id(c)"
        self.assertTrue(TestChecker.test(input, expect, 397))

    def test398(self):
        input = """ c:auto=1;
                    grand: function integer(){
                        return 0;
                    }
                    parent: function integer(inherit x:auto, y:auto) inherit grand{
                        return 0;
                    }
                    child1: function integer(m: integer, n: integer) inherit parent{
                        super("hehe","haha","namkha");
                        return 0;
                    }
                    main: function void(){
                    }
                    c:integer;
                """
        expect = "Type mismatch in expression: StringLit(namkha)"
        self.assertTrue(TestChecker.test(input, expect, 398))

    def test399(self):
        input = """ c:auto=1;
                    arr: array[5] of float = {1, 1.2 ,2};
                    main: string;
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 399))
