# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01fd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%")
        buf.write("\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-")
        buf.write("\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\7\61\u0132")
        buf.write("\n\61\f\61\16\61\u0135\13\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\7\62\u0140\n\62\f\62\16\62\u0143")
        buf.write("\13\62\3\62\3\62\3\63\3\63\3\63\7\63\u014a\n\63\f\63\16")
        buf.write("\63\u014d\13\63\3\63\3\63\6\63\u0151\n\63\r\63\16\63\u0152")
        buf.write("\7\63\u0155\n\63\f\63\16\63\u0158\13\63\3\63\5\63\u015b")
        buf.write("\n\63\3\64\6\64\u015e\n\64\r\64\16\64\u015f\3\64\3\64")
        buf.write("\6\64\u0164\n\64\r\64\16\64\u0165\7\64\u0168\n\64\f\64")
        buf.write("\16\64\u016b\13\64\3\64\3\64\6\64\u016f\n\64\r\64\16\64")
        buf.write("\u0170\3\64\3\64\6\64\u0175\n\64\r\64\16\64\u0176\7\64")
        buf.write("\u0179\n\64\f\64\16\64\u017c\13\64\3\64\6\64\u017f\n\64")
        buf.write("\r\64\16\64\u0180\3\64\3\64\6\64\u0185\n\64\r\64\16\64")
        buf.write("\u0186\7\64\u0189\n\64\f\64\16\64\u018c\13\64\3\64\3\64")
        buf.write("\6\64\u0190\n\64\r\64\16\64\u0191\5\64\u0194\n\64\3\64")
        buf.write("\3\64\6\64\u0198\n\64\r\64\16\64\u0199\7\64\u019c\n\64")
        buf.write("\f\64\16\64\u019f\13\64\3\64\3\64\5\64\u01a3\n\64\3\64")
        buf.write("\6\64\u01a6\n\64\r\64\16\64\u01a7\3\64\3\64\6\64\u01ac")
        buf.write("\n\64\r\64\16\64\u01ad\7\64\u01b0\n\64\f\64\16\64\u01b3")
        buf.write("\13\64\5\64\u01b5\n\64\3\64\3\64\3\65\3\65\3\65\3\65\7")
        buf.write("\65\u01bd\n\65\f\65\16\65\u01c0\13\65\3\65\3\65\3\65\3")
        buf.write("\66\5\66\u01c6\n\66\3\66\7\66\u01c9\n\66\f\66\16\66\u01cc")
        buf.write("\13\66\3\67\6\67\u01cf\n\67\r\67\16\67\u01d0\3\67\3\67")
        buf.write("\38\38\38\38\78\u01d9\n8\f8\168\u01dc\138\38\58\u01df")
        buf.write("\n8\38\38\39\39\39\39\79\u01e7\n9\f9\169\u01ea\139\39")
        buf.write("\39\39\39\3:\3:\3:\3:\7:\u01f4\n:\f:\16:\u01f7\13:\3:")
        buf.write("\3:\3;\3;\3;\3\u0133\2<\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<\3\2\17\3\2\f\f\3\2\63;\3\2")
        buf.write("\62;\4\2GGgg\3\2//\3\2$$\7\2\n\f\16\17$$))^^\3\2^^\n\2")
        buf.write("$$))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17")
        buf.write("\17\"\"\4\2*,\61\61\2\u021e\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\3w\3\2\2\2\5|\3\2\2\2\7\u0082\3\2\2\2\t\u008a\3\2\2")
        buf.write("\2\13\u008d\3\2\2\2\r\u0092\3\2\2\2\17\u0098\3\2\2\2\21")
        buf.write("\u009e\3\2\2\2\23\u00a2\3\2\2\2\25\u00ab\3\2\2\2\27\u00ae")
        buf.write("\3\2\2\2\31\u00b6\3\2\2\2\33\u00bd\3\2\2\2\35\u00c4\3")
        buf.write("\2\2\2\37\u00c9\3\2\2\2!\u00cf\3\2\2\2#\u00d4\3\2\2\2")
        buf.write("%\u00d8\3\2\2\2\'\u00e1\3\2\2\2)\u00e4\3\2\2\2+\u00ec")
        buf.write("\3\2\2\2-\u00f2\3\2\2\2/\u00f4\3\2\2\2\61\u00f6\3\2\2")
        buf.write("\2\63\u00f8\3\2\2\2\65\u00fa\3\2\2\2\67\u00fc\3\2\2\2")
        buf.write("9\u00fe\3\2\2\2;\u0101\3\2\2\2=\u0104\3\2\2\2?\u0107\3")
        buf.write("\2\2\2A\u010a\3\2\2\2C\u010c\3\2\2\2E\u010f\3\2\2\2G\u0111")
        buf.write("\3\2\2\2I\u0114\3\2\2\2K\u0117\3\2\2\2M\u0119\3\2\2\2")
        buf.write("O\u011b\3\2\2\2Q\u011d\3\2\2\2S\u011f\3\2\2\2U\u0121\3")
        buf.write("\2\2\2W\u0123\3\2\2\2Y\u0125\3\2\2\2[\u0127\3\2\2\2]\u0129")
        buf.write("\3\2\2\2_\u012b\3\2\2\2a\u012d\3\2\2\2c\u013b\3\2\2\2")
        buf.write("e\u015a\3\2\2\2g\u01b4\3\2\2\2i\u01b8\3\2\2\2k\u01c5\3")
        buf.write("\2\2\2m\u01ce\3\2\2\2o\u01d4\3\2\2\2q\u01e2\3\2\2\2s\u01ef")
        buf.write("\3\2\2\2u\u01fa\3\2\2\2wx\7c\2\2xy\7w\2\2yz\7v\2\2z{\7")
        buf.write("q\2\2{\4\3\2\2\2|}\7d\2\2}~\7t\2\2~\177\7g\2\2\177\u0080")
        buf.write("\7c\2\2\u0080\u0081\7m\2\2\u0081\6\3\2\2\2\u0082\u0083")
        buf.write("\7d\2\2\u0083\u0084\7q\2\2\u0084\u0085\7q\2\2\u0085\u0086")
        buf.write("\7n\2\2\u0086\u0087\7g\2\2\u0087\u0088\7c\2\2\u0088\u0089")
        buf.write("\7p\2\2\u0089\b\3\2\2\2\u008a\u008b\7f\2\2\u008b\u008c")
        buf.write("\7q\2\2\u008c\n\3\2\2\2\u008d\u008e\7g\2\2\u008e\u008f")
        buf.write("\7n\2\2\u008f\u0090\7u\2\2\u0090\u0091\7g\2\2\u0091\f")
        buf.write("\3\2\2\2\u0092\u0093\7h\2\2\u0093\u0094\7c\2\2\u0094\u0095")
        buf.write("\7n\2\2\u0095\u0096\7u\2\2\u0096\u0097\7g\2\2\u0097\16")
        buf.write("\3\2\2\2\u0098\u0099\7h\2\2\u0099\u009a\7n\2\2\u009a\u009b")
        buf.write("\7q\2\2\u009b\u009c\7c\2\2\u009c\u009d\7v\2\2\u009d\20")
        buf.write("\3\2\2\2\u009e\u009f\7h\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1")
        buf.write("\7t\2\2\u00a1\22\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4")
        buf.write("\7w\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7e\2\2\u00a6\u00a7")
        buf.write("\7v\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa")
        buf.write("\7p\2\2\u00aa\24\3\2\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad")
        buf.write("\7h\2\2\u00ad\26\3\2\2\2\u00ae\u00af\7k\2\2\u00af\u00b0")
        buf.write("\7p\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3")
        buf.write("\7i\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5\7t\2\2\u00b5\30")
        buf.write("\3\2\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9")
        buf.write("\7v\2\2\u00b9\u00ba\7w\2\2\u00ba\u00bb\7t\2\2\u00bb\u00bc")
        buf.write("\7p\2\2\u00bc\32\3\2\2\2\u00bd\u00be\7u\2\2\u00be\u00bf")
        buf.write("\7v\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7p\2\2\u00c2\u00c3\7i\2\2\u00c3\34\3\2\2\2\u00c4\u00c5")
        buf.write("\7v\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8")
        buf.write("\7g\2\2\u00c8\36\3\2\2\2\u00c9\u00ca\7y\2\2\u00ca\u00cb")
        buf.write("\7j\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7n\2\2\u00cd\u00ce")
        buf.write("\7g\2\2\u00ce \3\2\2\2\u00cf\u00d0\7x\2\2\u00d0\u00d1")
        buf.write("\7q\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3\7f\2\2\u00d3\"")
        buf.write("\3\2\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7")
        buf.write("\7v\2\2\u00d7$\3\2\2\2\u00d8\u00d9\7e\2\2\u00d9\u00da")
        buf.write("\7q\2\2\u00da\u00db\7p\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd")
        buf.write("\7k\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7w\2\2\u00df\u00e0")
        buf.write("\7g\2\2\u00e0&\3\2\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3")
        buf.write("\7h\2\2\u00e3(\3\2\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6")
        buf.write("\7p\2\2\u00e6\u00e7\7j\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9")
        buf.write("\7t\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7v\2\2\u00eb*\3")
        buf.write("\2\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef")
        buf.write("\7t\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1\7{\2\2\u00f1,\3")
        buf.write("\2\2\2\u00f2\u00f3\7-\2\2\u00f3.\3\2\2\2\u00f4\u00f5\7")
        buf.write("/\2\2\u00f5\60\3\2\2\2\u00f6\u00f7\7,\2\2\u00f7\62\3\2")
        buf.write("\2\2\u00f8\u00f9\7\61\2\2\u00f9\64\3\2\2\2\u00fa\u00fb")
        buf.write("\7\'\2\2\u00fb\66\3\2\2\2\u00fc\u00fd\7#\2\2\u00fd8\3")
        buf.write("\2\2\2\u00fe\u00ff\7(\2\2\u00ff\u0100\7(\2\2\u0100:\3")
        buf.write("\2\2\2\u0101\u0102\7~\2\2\u0102\u0103\7~\2\2\u0103<\3")
        buf.write("\2\2\2\u0104\u0105\7?\2\2\u0105\u0106\7?\2\2\u0106>\3")
        buf.write("\2\2\2\u0107\u0108\7#\2\2\u0108\u0109\7?\2\2\u0109@\3")
        buf.write("\2\2\2\u010a\u010b\7>\2\2\u010bB\3\2\2\2\u010c\u010d\7")
        buf.write(">\2\2\u010d\u010e\7?\2\2\u010eD\3\2\2\2\u010f\u0110\7")
        buf.write("@\2\2\u0110F\3\2\2\2\u0111\u0112\7@\2\2\u0112\u0113\7")
        buf.write("?\2\2\u0113H\3\2\2\2\u0114\u0115\7<\2\2\u0115\u0116\7")
        buf.write("<\2\2\u0116J\3\2\2\2\u0117\u0118\7*\2\2\u0118L\3\2\2\2")
        buf.write("\u0119\u011a\7+\2\2\u011aN\3\2\2\2\u011b\u011c\7]\2\2")
        buf.write("\u011cP\3\2\2\2\u011d\u011e\7_\2\2\u011eR\3\2\2\2\u011f")
        buf.write("\u0120\7\60\2\2\u0120T\3\2\2\2\u0121\u0122\7.\2\2\u0122")
        buf.write("V\3\2\2\2\u0123\u0124\7=\2\2\u0124X\3\2\2\2\u0125\u0126")
        buf.write("\7<\2\2\u0126Z\3\2\2\2\u0127\u0128\7}\2\2\u0128\\\3\2")
        buf.write("\2\2\u0129\u012a\7\177\2\2\u012a^\3\2\2\2\u012b\u012c")
        buf.write("\7?\2\2\u012c`\3\2\2\2\u012d\u012e\7\61\2\2\u012e\u012f")
        buf.write("\7,\2\2\u012f\u0133\3\2\2\2\u0130\u0132\13\2\2\2\u0131")
        buf.write("\u0130\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0134\3\2\2\2")
        buf.write("\u0133\u0131\3\2\2\2\u0134\u0136\3\2\2\2\u0135\u0133\3")
        buf.write("\2\2\2\u0136\u0137\7,\2\2\u0137\u0138\7\61\2\2\u0138\u0139")
        buf.write("\3\2\2\2\u0139\u013a\b\61\2\2\u013ab\3\2\2\2\u013b\u013c")
        buf.write("\7\61\2\2\u013c\u013d\7\61\2\2\u013d\u0141\3\2\2\2\u013e")
        buf.write("\u0140\n\2\2\2\u013f\u013e\3\2\2\2\u0140\u0143\3\2\2\2")
        buf.write("\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0144\3")
        buf.write("\2\2\2\u0143\u0141\3\2\2\2\u0144\u0145\b\62\2\2\u0145")
        buf.write("d\3\2\2\2\u0146\u015b\7\62\2\2\u0147\u014b\t\3\2\2\u0148")
        buf.write("\u014a\t\4\2\2\u0149\u0148\3\2\2\2\u014a\u014d\3\2\2\2")
        buf.write("\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u0156\3")
        buf.write("\2\2\2\u014d\u014b\3\2\2\2\u014e\u0150\7a\2\2\u014f\u0151")
        buf.write("\t\4\2\2\u0150\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0155\3\2\2\2")
        buf.write("\u0154\u014e\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154\3")
        buf.write("\2\2\2\u0156\u0157\3\2\2\2\u0157\u0159\3\2\2\2\u0158\u0156")
        buf.write("\3\2\2\2\u0159\u015b\b\63\3\2\u015a\u0146\3\2\2\2\u015a")
        buf.write("\u0147\3\2\2\2\u015bf\3\2\2\2\u015c\u015e\t\4\2\2\u015d")
        buf.write("\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u015d\3\2\2\2")
        buf.write("\u015f\u0160\3\2\2\2\u0160\u0169\3\2\2\2\u0161\u0163\7")
        buf.write("a\2\2\u0162\u0164\t\4\2\2\u0163\u0162\3\2\2\2\u0164\u0165")
        buf.write("\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166")
        buf.write("\u0168\3\2\2\2\u0167\u0161\3\2\2\2\u0168\u016b\3\2\2\2")
        buf.write("\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016c\3")
        buf.write("\2\2\2\u016b\u0169\3\2\2\2\u016c\u016e\7\60\2\2\u016d")
        buf.write("\u016f\t\4\2\2\u016e\u016d\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u017a\3")
        buf.write("\2\2\2\u0172\u0174\7a\2\2\u0173\u0175\t\4\2\2\u0174\u0173")
        buf.write("\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0174\3\2\2\2\u0176")
        buf.write("\u0177\3\2\2\2\u0177\u0179\3\2\2\2\u0178\u0172\3\2\2\2")
        buf.write("\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3")
        buf.write("\2\2\2\u017b\u01b5\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u017f")
        buf.write("\t\4\2\2\u017e\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u018a\3\2\2\2")
        buf.write("\u0182\u0184\7a\2\2\u0183\u0185\t\4\2\2\u0184\u0183\3")
        buf.write("\2\2\2\u0185\u0186\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187")
        buf.write("\3\2\2\2\u0187\u0189\3\2\2\2\u0188\u0182\3\2\2\2\u0189")
        buf.write("\u018c\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018b\u0193\3\2\2\2\u018c\u018a\3\2\2\2\u018d\u018f\7")
        buf.write("\60\2\2\u018e\u0190\t\4\2\2\u018f\u018e\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2")
        buf.write("\u0192\u0194\3\2\2\2\u0193\u018d\3\2\2\2\u0193\u0194\3")
        buf.write("\2\2\2\u0194\u019d\3\2\2\2\u0195\u0197\7a\2\2\u0196\u0198")
        buf.write("\t\4\2\2\u0197\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019c\3\2\2\2")
        buf.write("\u019b\u0195\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b\3")
        buf.write("\2\2\2\u019d\u019e\3\2\2\2\u019e\u01a0\3\2\2\2\u019f\u019d")
        buf.write("\3\2\2\2\u01a0\u01a2\t\5\2\2\u01a1\u01a3\t\6\2\2\u01a2")
        buf.write("\u01a1\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a5\3\2\2\2")
        buf.write("\u01a4\u01a6\t\4\2\2\u01a5\u01a4\3\2\2\2\u01a6\u01a7\3")
        buf.write("\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01b1")
        buf.write("\3\2\2\2\u01a9\u01ab\7a\2\2\u01aa\u01ac\t\4\2\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ab\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae\u01b0\3\2\2\2\u01af\u01a9\3")
        buf.write("\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2")
        buf.write("\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4")
        buf.write("\u015d\3\2\2\2\u01b4\u017e\3\2\2\2\u01b5\u01b6\3\2\2\2")
        buf.write("\u01b6\u01b7\b\64\4\2\u01b7h\3\2\2\2\u01b8\u01be\t\7\2")
        buf.write("\2\u01b9\u01bd\n\b\2\2\u01ba\u01bb\t\t\2\2\u01bb\u01bd")
        buf.write("\t\n\2\2\u01bc\u01b9\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd")
        buf.write("\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2")
        buf.write("\u01bf\u01c1\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c2\t")
        buf.write("\7\2\2\u01c2\u01c3\b\65\5\2\u01c3j\3\2\2\2\u01c4\u01c6")
        buf.write("\t\13\2\2\u01c5\u01c4\3\2\2\2\u01c6\u01ca\3\2\2\2\u01c7")
        buf.write("\u01c9\t\f\2\2\u01c8\u01c7\3\2\2\2\u01c9\u01cc\3\2\2\2")
        buf.write("\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cbl\3\2\2")
        buf.write("\2\u01cc\u01ca\3\2\2\2\u01cd\u01cf\t\r\2\2\u01ce\u01cd")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0")
        buf.write("\u01d1\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3\b\67\2")
        buf.write("\2\u01d3n\3\2\2\2\u01d4\u01da\t\7\2\2\u01d5\u01d9\n\b")
        buf.write("\2\2\u01d6\u01d7\t\t\2\2\u01d7\u01d9\t\n\2\2\u01d8\u01d5")
        buf.write("\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da")
        buf.write("\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01de\3\2\2\2")
        buf.write("\u01dc\u01da\3\2\2\2\u01dd\u01df\t\2\2\2\u01de\u01dd\3")
        buf.write("\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e1")
        buf.write("\b8\6\2\u01e1p\3\2\2\2\u01e2\u01e8\t\7\2\2\u01e3\u01e7")
        buf.write("\n\t\2\2\u01e4\u01e5\t\t\2\2\u01e5\u01e7\t\n\2\2\u01e6")
        buf.write("\u01e3\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01ea\3\2\2\2")
        buf.write("\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01eb\3")
        buf.write("\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ec\t\t\2\2\u01ec\u01ed")
        buf.write("\n\n\2\2\u01ed\u01ee\b9\7\2\u01eer\3\2\2\2\u01ef\u01f0")
        buf.write("\7\61\2\2\u01f0\u01f1\7,\2\2\u01f1\u01f5\3\2\2\2\u01f2")
        buf.write("\u01f4\n\16\2\2\u01f3\u01f2\3\2\2\2\u01f4\u01f7\3\2\2")
        buf.write("\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f8")
        buf.write("\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8\u01f9\b:\b\2\u01f9")
        buf.write("t\3\2\2\2\u01fa\u01fb\13\2\2\2\u01fb\u01fc\b;\t\2\u01fc")
        buf.write("v\3\2\2\2\'\2\u0133\u0141\u014b\u0152\u0156\u015a\u015f")
        buf.write("\u0165\u0169\u0170\u0176\u017a\u0180\u0186\u018a\u0191")
        buf.write("\u0193\u0199\u019d\u01a2\u01a7\u01ad\u01b1\u01b4\u01bc")
        buf.write("\u01be\u01c5\u01c8\u01ca\u01d0\u01d8\u01da\u01de\u01e6")
        buf.write("\u01e8\u01f5\n\b\2\2\3\63\2\3\64\3\3\65\4\38\5\39\6\3")
        buf.write(":\7\3;\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    ELSE = 5
    FALSE = 6
    FLOAT = 7
    FOR = 8
    FUNCTION = 9
    IF = 10
    INTEGER = 11
    RETURN = 12
    STRING = 13
    TRUE = 14
    WHILE = 15
    VOID = 16
    OUT = 17
    CONTINUE = 18
    OF = 19
    INHERIT = 20
    ARRAY = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    NOT = 27
    AND = 28
    OR = 29
    EQUAL = 30
    NOTEQUAL = 31
    LESS = 32
    LESSEQUAL = 33
    GREATER = 34
    GREATEREQUAL = 35
    CONCAT = 36
    LRB = 37
    RRB = 38
    LSB = 39
    RSB = 40
    DOT = 41
    COMMA = 42
    SEMI = 43
    COLON = 44
    LCB = 45
    RCB = 46
    ASSIGN = 47
    CCOMMENT = 48
    CPLUSCOMMENT = 49
    INTLIT = 50
    FLOATLIT = 51
    STRINGLIT = 52
    ID = 53
    WS = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    UNTERMINATED_COMMENT = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", "','", 
            "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
            "NOTEQUAL", "LESS", "LESSEQUAL", "GREATER", "GREATEREQUAL", 
            "CONCAT", "LRB", "RRB", "LSB", "RSB", "DOT", "COMMA", "SEMI", 
            "COLON", "LCB", "RCB", "ASSIGN", "CCOMMENT", "CPLUSCOMMENT", 
            "INTLIT", "FLOATLIT", "STRINGLIT", "ID", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", 
                  "OR", "EQUAL", "NOTEQUAL", "LESS", "LESSEQUAL", "GREATER", 
                  "GREATEREQUAL", "CONCAT", "LRB", "RRB", "LSB", "RSB", 
                  "DOT", "COMMA", "SEMI", "COLON", "LCB", "RCB", "ASSIGN", 
                  "CCOMMENT", "CPLUSCOMMENT", "INTLIT", "FLOATLIT", "STRINGLIT", 
                  "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.INTLIT_action 
            actions[50] = self.FLOATLIT_action 
            actions[51] = self.STRINGLIT_action 
            actions[54] = self.UNCLOSE_STRING_action 
            actions[55] = self.ILLEGAL_ESCAPE_action 
            actions[56] = self.UNTERMINATED_COMMENT_action 
            actions[57] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	if self.text.find('\n') != -1:
            		pos = self.text.find('\n')
            		raise UncloseString(self.text[1:pos])
            	else:
            		raise UncloseString(self.text[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text[1:])
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	if self.text.find('\n') != -1:
            		pos = self.text.find('\n')
            		raise UnterminatedComment(self.text[0:pos])
            	else:
            		raise UnterminatedComment(self.text[0:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     


