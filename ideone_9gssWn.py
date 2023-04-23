def test_basicUndeclared_Identifier(self):
        input = Program([
                FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", IntegerType(
                ), IntegerLit(65)), AssignStmt(Id("a"), BinExpr("+", Id("a"), Id("b")))]))
        ])
# expect = """main: function void () {
#     a: integer = 65;
#     a = a + b;
# }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 401))

def test_basicUndeclared_Identifier_Param(self):
        """Test basicUndeclared_Identifier_Param"""
        input = Program([
                FuncDecl("bds", IntegerType(), [], None, BlockStmt([ReturnStmt(Id("a"))])),
                FuncDecl("main", VoidType(), [], None, BlockStmt([]))
                ])
        #  """
        #     bds: function integer () {
        #         return a;
        #     }
        #     main: function void () {
        # }"""

        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 402))

def test_basicCallStmt(self):
        """Test basicUndeclared_Function"""
        input = Program([
        FuncDecl("main", VoidType(), [], None, BlockStmt([CallStmt("helloWorld", [])]))
                ])
        expect = "Undeclared Function: helloWorld"
        # main: function void () {
        #                 helloWorld();
        #         }
        self.assertTrue(TestChecker.test(input, expect, 403))
