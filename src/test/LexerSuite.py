import unittest
from TestUtils import TestLexer

testcaseArray = [['"hello"', 'hello,<EOF>'],
                 ["123.7", "123.7,<EOF>"],
                 ["10_00_00","100000,<EOF>"],
                 ['1_234.567','abc']
                 ]
class LexerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        testcaseNo = 100
        """test identifiers"""
        for testcase in testcaseArray:
            print("\n\n")
            print("Testcase",testcaseNo,": ", testcase[0])
            print("---------------------------------------------------------------")
            self.assertTrue(TestLexer.test(testcase[0], testcase[1], testcaseNo))
            testcaseNo+=1
