import unittest
from TestUtils import TestChecker
from AST import *
 
class CheckerSuite(unittest.TestCase):
    def test300(self):
        input = """a:integer=5;
        c:auto;"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 300))
        
    def test301(self):
        input = """a:integer=5;
                    c:auto=1;
                    main: function void(){
                        c=b;
                    }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 301))
        
    def test302(self):
        input = """a:integer=5;
                    c:auto=1;
                    
                    grand: function integer(inherit a: integer, b:integer){
                        return 0;
                    }
                    parent: function integer(inherit x:integer, y:integer) inherit grand{
                        preventDefault();
                        return 0;
                    }
                    child: function integer(m: integer, n: integer) inherit parent{
                        preventDefault();
                        return m+n+x+a;
                    }
                    main: function void(){
                    }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 302))

    def test303(self):
        input = """x: function void() {}
    main: function void() inherit x {
        super(); //?
    }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 303))