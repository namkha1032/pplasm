import unittest
from TestUtils import TestLexer

testcaseArray = [
                    # Testcase 100 - 109: INTLIT
                    ['123','123,<EOF>'],
                    ['1_23','123,<EOF>'],
                    ['1_2_34','1234,<EOF>'],
                    ['1_2_3 567 8_9','123,567,89,<EOF>'],
                    ['a = 123;','a,=,123,;,<EOF>'],
                    ['a : integer = 1_23;','a,:,integer,=,123,;,<EOF>'],
                    ['23 11 1973','23,11,1973,<EOF>'],
                    ['21 11 1974','21,11,1974,<EOF>'],
                    ['10 3 2002','10,3,2002,<EOF>'],
                    ['26 2 2005','26,2,2005,<EOF>'],

                    # Testcase 110 - 119: FLOATLIT
                    ['0.1','0.1,<EOF>'],
                    ['1.0e10','1.0e10,<EOF>'],
                    ['1e1_0_3','1e103,<EOF>'],
                    ['1.5e-10','1.5e-10,<EOF>'],
                    ['1_0_0.5e-10','100.5e-10,<EOF>'],
                    ['103.5_5e-10','103.55e-10,<EOF>'],
                    ['103.55e-10_2','103.55e-102,<EOF>'],
                    ['1_3.5_5e-1_0','13.55e-10,<EOF>'],
                    ['1_3.5_5e1_0','13.55e10,<EOF>'],
                    ['0.5e1_0 123','0.5e10,123,<EOF>'],

                    # Testcase 120 - 129: STRINGLIT
                    ['"khadeptrai"', 'khadeptrai,<EOF>'],
                    ['a = "namkha";','a,=,namkha,;,<EOF>'],
                    ['str = "use \\\\ after"','str,=,use \\\\ after,<EOF>'],
                    ['str = "use \\n after"','str,=,use \\n after,<EOF>'],
                    ['str = "use \\b after"','str,=,use \\b after,<EOF>'],
                    ['str = "use \\f after"','str,=,use \\f after,<EOF>'],
                    ['str = "use \\r after"','str,=,use \\r after,<EOF>'],
                    ['str = "use \\t after"','str,=,use \\t after,<EOF>'],
                    ['str = "use \\\' after"','str,=,use \\\' after,<EOF>'],
                    ['str = "use \\" after"','str,=,use \\" after,<EOF>'],

                    # Testcase 130 - 139: ID
                    ['khadeptrai', 'khadeptrai,<EOF>'],
                    ['a = 1;', 'a,=,1,;,<EOF>'],
                    ['super_var', 'super_var,<EOF>'],
                    ['camelVar', 'camelVar,<EOF>'],
                    ['snake_var_hahaha', 'snake_var_hahaha,<EOF>'],
                    ['numvar123', 'numvar123,<EOF>'],
                    ['_underscoreVar', '_underscoreVar,<EOF>'],
                    ['snake_SNAKE_123','snake_SNAKE_123,<EOF>'],
                    ['UPPERCASEVAR','UPPERCASEVAR,<EOF>'],
                    ['Normalvar','Normalvar,<EOF>'],

                    # Testcase 140 - 149: C style comment
                    ['/* a comment */', '<EOF>'],
                    ['beforecmt/* a comment */aftercmt','beforecmt,aftercmt,<EOF>'],
                    ['beforecmt/* a comment */aftercmt','beforecmt,aftercmt,<EOF>'],
                    ['a = x + 1;\n/* a comment */\nprint(a);','a,=,x,+,1,;,print,(,a,),;,<EOF>'],
                    ['/* a \nmultiline\ncomment */', '<EOF>'],
                    ['a = x + 1;/* 1st comment */\nprint(a);/* 2nd comment */','a,=,x,+,1,;,print,(,a,),;,<EOF>'],
                    ['/* 1st comment */a = x + 1;\n/* 2nd comment */print(a);','a,=,x,+,1,;,print,(,a,),;,<EOF>'],
                    ['/* 1st comment */a = x + 1;/* 2nd comment */','a,=,x,+,1,;,<EOF>'],
                    ['a = x + 1;/*multiline\ncomment */print(a);','a,=,x,+,1,;,print,(,a,),;,<EOF>'],
                    ['/* last comment */', '<EOF>'],

                    # Testcase 150 - 159: C++ style comment
                    ['// comment', '<EOF>'],
                    ['// comment\nx = 1;', 'x,=,1,;,<EOF>'],
                    ['x = 1;\n// comment', 'x,=,1,;,<EOF>'],
                    ['x = 1;\n// comment\nprint(x);', 'x,=,1,;,print,(,x,),;,<EOF>'],
                    ['x = 1;// 1stcomment\nprint(x);// 2nd comment;', 'x,=,1,;,print,(,x,),;,<EOF>'],
                    ['// 1stcomment\nprint(x);\n// 2nd comment;', 'print,(,x,),;,<EOF>'],
                    ['// 1st comment\n// 2nd comment', '<EOF>'],
                    ['// 1st comment\n// 2nd comment\n// 3rd comment', '<EOF>'],
                    ['// 1st comment\n// 2nd comment\nprint(x);// 3rd comment', 'print,(,x,),;,<EOF>'],
                    ['// 1st comment\nprint(x);// 2nd comment\n// 3rd comment', 'print,(,x,),;,<EOF>'],

                    # Testcase 160 - 169: Unclose string
                    ['"unclose string','Unclosed String: unclose string'],
                    ['"unclose string\nhehehe"','Unclosed String: unclose string'],
                    ['"good str""unclose string\nhehehe"','good str,Unclosed String: unclose string'],
                    ['"unclose string\n"','Unclosed String: unclose string'],
                    ['"good str""unclose string','good str,Unclosed String: unclose string'],
                    ['a = "unclose string\nhehehe"','a,=,Unclosed String: unclose string'],
                    ['print("unclose str)','print,(,Unclosed String: unclose str)'],
                    ['str1, str2 : string = "good str", "unclose str; ','str1,,,str2,:,string,=,good str,,,Unclosed String: unclose str; '],
                    ['"uncls str:','Unclosed String: uncls str:'],
                    ['"uncls str:\nx = x + 1;','Unclosed String: uncls str:'],

                    # Testcase 170 - 179: Illegal escape
                    ['"str with bad escape:\\a"','Illegal Escape In String: str with bad escape:\\a'],
                    ['"unclose str with bad escape (catch bad escape first):\\e','Illegal Escape In String: unclose str with bad escape (catch bad escape first):\\e'],
                    ['"good escape: \\b,\\f,\\r,\\n,\\t,\\\\,\\\',\\". Bad escape: \\a"','Illegal Escape In String: good escape: \\b,\\f,\\r,\\n,\\t,\\\\,\\\',\\". Bad escape: \\a'],
                    ['print("str with bad escape:\\a")','print,(,Illegal Escape In String: str with bad escape:\\a'],
                    ['print("str with good escape:\\n","str with bad escape:\\x");','print,(,str with good escape:\\n,,,Illegal Escape In String: str with bad escape:\\x'],
                    ['"str with good escape:\\n""str with bad escape:\\x"','str with good escape:\\n,Illegal Escape In String: str with bad escape:\\x'],
                    ['a="str with good escape:\\n";\nb="str with bad escape:\\x"','a,=,str with good escape:\\n,;,b,=,Illegal Escape In String: str with bad escape:\\x'],
                    ['"hehehe\\a"','Illegal Escape In String: hehehe\\a'],
                    ['"hahaha\\x"','Illegal Escape In String: hahaha\\x'],
                    ['"hohoho\\y"','Illegal Escape In String: hohoho\\y'],

                    # Testcase 180 - 189: Unterminated comment
                    ['/*unclose comment','Unterminated Comment: /*unclose comment'],
                    ['/*unclose comment\nx=y+1;','Unterminated Comment: /*unclose comment'],
                    ['x=1;//good cmt\ny=2;/*unclose comment','x,=,1,;,y,=,2,;,Unterminated Comment: /*unclose comment'],
                    ['x=1;//good cmt\ny=2;/*unclose comment\nz=3;','x,=,1,;,y,=,2,;,Unterminated Comment: /*unclose comment'],
                    ['x=1;/*unclose comment\ny=2;\nz=3;//good cmt','x,=,1,;,Unterminated Comment: /*unclose comment'],
                    ['x="namkha";/*unclose comment','x,=,namkha,;,Unterminated Comment: /*unclose comment'],
                    ['/*unclose comment\nx="namkha";','Unterminated Comment: /*unclose comment'],
                    ['/*unclose comment\nx="unclose str;','Unterminated Comment: /*unclose comment'],
                    ['/*unclose comment\nx="unclose str;','Unterminated Comment: /*unclose comment'],
                    ['/*unclose comment "str";','Unterminated Comment: /*unclose comment "str";'],

                    # Testcase 190 - 199: Error token
                    ['namkha@','namkha,Error Token @'],
                    ['namkha#','namkha,Error Token #'],
                    ['namkha\'','namkha,Error Token \''],
                    ['namkha~','namkha,Error Token ~'],
                    ['namkha$','namkha,Error Token $'],
                    ['"not error token $" $','not error token $,Error Token $'],
                    ['namkha^','namkha,Error Token ^'],
                    ['namkha&','namkha,Error Token &'],
                    ['namkha&& &','namkha,&&,Error Token &'],
                    ['namkha`','namkha,Error Token `'],

                ]
class LexerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        testcaseNo = 100
        """test identifiers"""
        for testcase in testcaseArray:
            print("\n\n")
            print("Testcase",testcaseNo,": ")
            print("---------------------------------------------------------------")
            print(testcase[0])
            print("---------------------------------------------------------------")
            self.assertTrue(TestLexer.test(testcase[0], testcase[1], testcaseNo))
            testcaseNo+=1
