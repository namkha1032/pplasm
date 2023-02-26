import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener
if not './main/mt22/parser/' in sys.path:
    sys.path.append('./main/mt22/parser/')
if os.path.isdir('../target/main/mt22/parser') and not '../target/main/mt22/parser/' in sys.path:
    sys.path.append('../target/main/mt22/parser/')
from MT22Lexer import MT22Lexer
from MT22Parser import MT22Parser
from lexererr import *
import subprocess
token_dict = {1: 'AUTO', 2: 'BREAK', 3: 'BOOLEAN', 4: 'DO', 5: 'ELSE', 6: 'FALSE', 7: 'FLOAT', 8: 'FOR', 9: 'FUNCTION', 10: 'IF', 11: 'INTEGER', 12: 'RETURN', 13: 'STRING', 14: 'TRUE', 15: 'WHILE', 16: 'VOID', 17: 'OUT', 18: 'CONTINUE', 19: 'OF', 20: 'INHERIT', 21: 'ARRAY', 22: 'ADD', 23: 'SUB', 24: 'MUL', 25: 'DIV', 26: 'MOD', 27: 'NOT', 28: 'AND', 29: 'OR', 30: 'EQUAL', 31: 'NOTEQUAL', 32: 'LESS', 33: 'LESSEQUAL', 34: 'GREATER', 35: 'GREATEREQUAL', 36: 'CONCAT', 37: 'LRB', 38: 'RRB', 39: 'LSB', 40: 'RSB', 41: 'DOT', 42: 'COMMA', 43: 'SEMI', 44: 'COLON', 45: 'LCB', 46: 'RCB', 47: 'ASSIGN', 48: 'CCOMMENT', 49: 'CPLUSCOMMENT', 50: 'INTLIT', 51: 'FLOATLIT', 52: 'STRINGLIT', 53: 'ID', 54: 'WS', 55: 'UNCLOSE_STRING', 56: 'ILLEGAL_ESCAPE', 57: 'UNTERMINATED_COMMENT', 58: 'ERROR_CHAR'}
JASMIN_JAR = "./external/jasmin.jar"
TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"
Lexer = MT22Lexer
Parser = MT22Parser

class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        TestLexer.check(SOL_DIR, inputfile, num)
        dest = open(SOL_DIR + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, inputfile, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        lexer = Lexer(inputfile)
        try:
            TestLexer.printLexeme(dest, lexer)
        except (ErrorToken, UncloseString, IllegalEscape, UnterminatedComment) as err:
            print(f"Error: {err.message}")
            dest.write(err.message)
        finally:
            dest.close()

    @staticmethod
    def printLexeme(dest, lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            res = tok.text + ":" + token_dict[tok.type] + " "
            print(res)
            dest.write(tok.text+",")
            TestLexer.printLexeme(dest, lexer)
        else:
            dest.write("<EOF>")


class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line " + str(line) +
                              " col " + str(column) + ": " + offendingSymbol.text)


NewErrorListener.INSTANCE = NewErrorListener()


class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg


class TestParser:
    @staticmethod
    def createErrorListener():
        return NewErrorListener.INSTANCE

    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        TestParser.check(SOL_DIR, inputfile, num)
        dest = open(SOL_DIR + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, inputfile, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        lexer = Lexer(inputfile)
        listener = TestParser.createErrorListener()
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()


class TestAST:
    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        TestAST.check(SOL_DIR, inputfile, num)
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, inputfile, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        lexer = Lexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        dest.write(str(asttree))
        dest.close()


class TestChecker:
    @staticmethod
    def test(input, expect, num):
        if type(input) is str:
            inputfile = TestUtil.makeSource(input, num)
            lexer = Lexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = Parser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input), num)
            asttree = input
        TestChecker.check(SOL_DIR, asttree, num)
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, asttree, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
        checker = StaticChecker(asttree)
        try:
            res = checker.check()
            dest.write(str(list(res)))
        except StaticError as e:
            dest.write(str(e))
        finally:
            dest.close()


class TestCodeGen():
    @staticmethod
    def test(input, expect, num):
        if type(input) is str:
            inputfile = TestUtil.makeSource(input, num)
            lexer = Lexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = Parser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input), num)
            asttree = input

        TestCodeGen.check(SOL_DIR, asttree, num)

        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, asttree, num):
        codeGen = CodeGenerator()
        path = os.path.join(soldir, str(num))
        if not os.path.isdir(path):
            os.mkdir(path)
        f = open(os.path.join(soldir, str(num) + ".txt"), "w")
        try:
            codeGen.gen(asttree, path)

            subprocess.call("java  -jar " + JASMIN_JAR + " " + path +
                            "/MT22Class.j", shell=True, stderr=subprocess.STDOUT)

            subprocess.run("java -cp ./lib:. MT22Class",
                           shell=True, stdout=f, timeout=10)
        except StaticError as e:
            f.write(str(e))
        except subprocess.TimeoutExpired:
            f.write("Time out\n")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(
                e.cmd, e.returncode, e.output))
        finally:
            f.close()
