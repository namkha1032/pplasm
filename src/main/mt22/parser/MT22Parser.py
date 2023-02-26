# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<")
        buf.write("\u0187\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3`\n\3\3\4\3\4\3\4\5\4e\n\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\br\n\b\3\t\3\t\3")
        buf.write("\t\3\t\5\tx\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u0089\n\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u0098\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\5\17\u00a6\n\17\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00b5")
        buf.write("\n\21\3\22\3\22\5\22\u00b9\n\22\3\23\3\23\3\23\3\23\3")
        buf.write("\23\5\23\u00c0\n\23\3\24\3\24\5\24\u00c4\n\24\3\24\3\24")
        buf.write("\5\24\u00c8\n\24\3\24\3\24\3\24\3\24\3\25\3\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\5\27\u00d7\n\27\3\30\3\30")
        buf.write("\5\30\u00db\n\30\3\30\3\30\3\30\3\30\5\30\u00e1\n\30\5")
        buf.write("\30\u00e3\n\30\3\31\3\31\3\31\3\31\3\31\5\31\u00ea\n\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\5\32\u00f1\n\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\7\33\u00f9\n\33\f\33\16\33\u00fc\13")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0104\n\34\f\34")
        buf.write("\16\34\u0107\13\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35")
        buf.write("\u010f\n\35\f\35\16\35\u0112\13\35\3\36\3\36\3\36\5\36")
        buf.write("\u0117\n\36\3\37\3\37\3\37\5\37\u011c\n\37\3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \5 \u0128\n \3!\3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3\"\5\"\u0132\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\5#\u013f\n#\3$\3$\5$\u0143\n$\3$\3$\3$\3$\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0157\n%\3&\3&\3&\3")
        buf.write("&\5&\u015d\n&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3*\3*\3*\3")
        buf.write("+\3+\3+\3+\3+\3+\5+\u0182\n+\3,\3,\3,\3,\2\5\64\668-\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTV\2\t\b\2\3\3\5\5\t\t\r\r\17\17\22\22")
        buf.write("\6\2\5\5\t\t\r\r\17\17\b\2\3\3\5\5\t\t\r\r\17\17\27\27")
        buf.write("\3\2 %\3\2\36\37\3\2\30\31\3\2\32\34\2\u018b\2X\3\2\2")
        buf.write("\2\4_\3\2\2\2\6d\3\2\2\2\bf\3\2\2\2\nh\3\2\2\2\fj\3\2")
        buf.write("\2\2\16q\3\2\2\2\20w\3\2\2\2\22y\3\2\2\2\24}\3\2\2\2\26")
        buf.write("\u0088\3\2\2\2\30\u008a\3\2\2\2\32\u0097\3\2\2\2\34\u00a5")
        buf.write("\3\2\2\2\36\u00a7\3\2\2\2 \u00aa\3\2\2\2\"\u00b8\3\2\2")
        buf.write("\2$\u00bf\3\2\2\2&\u00c3\3\2\2\2(\u00cd\3\2\2\2*\u00cf")
        buf.write("\3\2\2\2,\u00d6\3\2\2\2.\u00e2\3\2\2\2\60\u00e9\3\2\2")
        buf.write("\2\62\u00f0\3\2\2\2\64\u00f2\3\2\2\2\66\u00fd\3\2\2\2")
        buf.write("8\u0108\3\2\2\2:\u0116\3\2\2\2<\u011b\3\2\2\2>\u0127\3")
        buf.write("\2\2\2@\u0129\3\2\2\2B\u0131\3\2\2\2D\u013e\3\2\2\2F\u0142")
        buf.write("\3\2\2\2H\u0156\3\2\2\2J\u0158\3\2\2\2L\u0167\3\2\2\2")
        buf.write("N\u016d\3\2\2\2P\u0175\3\2\2\2R\u0178\3\2\2\2T\u0181\3")
        buf.write("\2\2\2V\u0183\3\2\2\2XY\5\4\3\2YZ\7\2\2\3Z\3\3\2\2\2[")
        buf.write("\\\5\6\4\2\\]\5\4\3\2]`\3\2\2\2^`\5\6\4\2_[\3\2\2\2_^")
        buf.write("\3\2\2\2`\5\3\2\2\2ae\5\32\16\2be\5\36\20\2ce\5D#\2da")
        buf.write("\3\2\2\2db\3\2\2\2dc\3\2\2\2e\7\3\2\2\2fg\t\2\2\2g\t\3")
        buf.write("\2\2\2hi\t\3\2\2i\13\3\2\2\2jk\t\4\2\2k\r\3\2\2\2lm\5")
        buf.write("\60\31\2mn\7,\2\2no\5\16\b\2or\3\2\2\2pr\5\60\31\2ql\3")
        buf.write("\2\2\2qp\3\2\2\2r\17\3\2\2\2st\7\67\2\2tu\7,\2\2ux\5\20")
        buf.write("\t\2vx\7\67\2\2ws\3\2\2\2wv\3\2\2\2x\21\3\2\2\2yz\7/\2")
        buf.write("\2z{\5\16\b\2{|\7\60\2\2|\23\3\2\2\2}~\7\27\2\2~\177\7")
        buf.write(")\2\2\177\u0080\5\26\f\2\u0080\u0081\7*\2\2\u0081\u0082")
        buf.write("\7\25\2\2\u0082\u0083\5\n\6\2\u0083\25\3\2\2\2\u0084\u0085")
        buf.write("\7\64\2\2\u0085\u0086\7,\2\2\u0086\u0089\5\26\f\2\u0087")
        buf.write("\u0089\7\64\2\2\u0088\u0084\3\2\2\2\u0088\u0087\3\2\2")
        buf.write("\2\u0089\27\3\2\2\2\u008a\u008b\7\67\2\2\u008b\u008c\7")
        buf.write(")\2\2\u008c\u008d\5\16\b\2\u008d\u008e\7*\2\2\u008e\31")
        buf.write("\3\2\2\2\u008f\u0090\5\20\t\2\u0090\u0091\7.\2\2\u0091")
        buf.write("\u0092\5\f\7\2\u0092\u0093\7-\2\2\u0093\u0098\3\2\2\2")
        buf.write("\u0094\u0095\5\34\17\2\u0095\u0096\7-\2\2\u0096\u0098")
        buf.write("\3\2\2\2\u0097\u008f\3\2\2\2\u0097\u0094\3\2\2\2\u0098")
        buf.write("\33\3\2\2\2\u0099\u009a\7\67\2\2\u009a\u009b\7,\2\2\u009b")
        buf.write("\u009c\5\34\17\2\u009c\u009d\7,\2\2\u009d\u009e\5\60\31")
        buf.write("\2\u009e\u00a6\3\2\2\2\u009f\u00a0\7\67\2\2\u00a0\u00a1")
        buf.write("\7.\2\2\u00a1\u00a2\5\f\7\2\u00a2\u00a3\7\61\2\2\u00a3")
        buf.write("\u00a4\5\60\31\2\u00a4\u00a6\3\2\2\2\u00a5\u0099\3\2\2")
        buf.write("\2\u00a5\u009f\3\2\2\2\u00a6\35\3\2\2\2\u00a7\u00a8\5")
        buf.write(" \21\2\u00a8\u00a9\5(\25\2\u00a9\37\3\2\2\2\u00aa\u00ab")
        buf.write("\7\67\2\2\u00ab\u00ac\7.\2\2\u00ac\u00ad\7\13\2\2\u00ad")
        buf.write("\u00ae\5\b\5\2\u00ae\u00af\7\'\2\2\u00af\u00b0\5\"\22")
        buf.write("\2\u00b0\u00b4\7(\2\2\u00b1\u00b2\7\26\2\2\u00b2\u00b5")
        buf.write("\7\67\2\2\u00b3\u00b5\3\2\2\2\u00b4\u00b1\3\2\2\2\u00b4")
        buf.write("\u00b3\3\2\2\2\u00b5!\3\2\2\2\u00b6\u00b9\5$\23\2\u00b7")
        buf.write("\u00b9\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2")
        buf.write("\u00b9#\3\2\2\2\u00ba\u00bb\5&\24\2\u00bb\u00bc\7,\2\2")
        buf.write("\u00bc\u00bd\5$\23\2\u00bd\u00c0\3\2\2\2\u00be\u00c0\5")
        buf.write("&\24\2\u00bf\u00ba\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0%")
        buf.write("\3\2\2\2\u00c1\u00c4\7\26\2\2\u00c2\u00c4\3\2\2\2\u00c3")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00c7\3\2\2\2")
        buf.write("\u00c5\u00c8\7\23\2\2\u00c6\u00c8\3\2\2\2\u00c7\u00c5")
        buf.write("\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("\u00ca\7\67\2\2\u00ca\u00cb\7.\2\2\u00cb\u00cc\5\f\7\2")
        buf.write("\u00cc\'\3\2\2\2\u00cd\u00ce\5@!\2\u00ce)\3\2\2\2\u00cf")
        buf.write("\u00d0\7\67\2\2\u00d0\u00d1\7\'\2\2\u00d1\u00d2\5,\27")
        buf.write("\2\u00d2\u00d3\7(\2\2\u00d3+\3\2\2\2\u00d4\u00d7\5.\30")
        buf.write("\2\u00d5\u00d7\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5")
        buf.write("\3\2\2\2\u00d7-\3\2\2\2\u00d8\u00db\7\67\2\2\u00d9\u00db")
        buf.write("\5\60\31\2\u00da\u00d8\3\2\2\2\u00da\u00d9\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc\u00dd\7,\2\2\u00dd\u00e3\5.\30\2")
        buf.write("\u00de\u00e1\7\67\2\2\u00df\u00e1\5\60\31\2\u00e0\u00de")
        buf.write("\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2")
        buf.write("\u00da\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3/\3\2\2\2\u00e4")
        buf.write("\u00e5\5\62\32\2\u00e5\u00e6\7&\2\2\u00e6\u00e7\5\62\32")
        buf.write("\2\u00e7\u00ea\3\2\2\2\u00e8\u00ea\5\62\32\2\u00e9\u00e4")
        buf.write("\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea\61\3\2\2\2\u00eb\u00ec")
        buf.write("\5\64\33\2\u00ec\u00ed\t\5\2\2\u00ed\u00ee\5\64\33\2\u00ee")
        buf.write("\u00f1\3\2\2\2\u00ef\u00f1\5\64\33\2\u00f0\u00eb\3\2\2")
        buf.write("\2\u00f0\u00ef\3\2\2\2\u00f1\63\3\2\2\2\u00f2\u00f3\b")
        buf.write("\33\1\2\u00f3\u00f4\5\66\34\2\u00f4\u00fa\3\2\2\2\u00f5")
        buf.write("\u00f6\f\4\2\2\u00f6\u00f7\t\6\2\2\u00f7\u00f9\5\66\34")
        buf.write("\2\u00f8\u00f5\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\65\3\2\2\2\u00fc\u00fa")
        buf.write("\3\2\2\2\u00fd\u00fe\b\34\1\2\u00fe\u00ff\58\35\2\u00ff")
        buf.write("\u0105\3\2\2\2\u0100\u0101\f\4\2\2\u0101\u0102\t\7\2\2")
        buf.write("\u0102\u0104\58\35\2\u0103\u0100\3\2\2\2\u0104\u0107\3")
        buf.write("\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106\67")
        buf.write("\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u0109\b\35\1\2\u0109")
        buf.write("\u010a\5:\36\2\u010a\u0110\3\2\2\2\u010b\u010c\f\4\2\2")
        buf.write("\u010c\u010d\t\b\2\2\u010d\u010f\5:\36\2\u010e\u010b\3")
        buf.write("\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111")
        buf.write("\3\2\2\2\u01119\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0114")
        buf.write("\7\35\2\2\u0114\u0117\5:\36\2\u0115\u0117\5<\37\2\u0116")
        buf.write("\u0113\3\2\2\2\u0116\u0115\3\2\2\2\u0117;\3\2\2\2\u0118")
        buf.write("\u0119\7\31\2\2\u0119\u011c\5<\37\2\u011a\u011c\5> \2")
        buf.write("\u011b\u0118\3\2\2\2\u011b\u011a\3\2\2\2\u011c=\3\2\2")
        buf.write("\2\u011d\u0128\7\64\2\2\u011e\u0128\7\65\2\2\u011f\u0128")
        buf.write("\7\66\2\2\u0120\u0128\7\20\2\2\u0121\u0128\7\b\2\2\u0122")
        buf.write("\u0128\7\67\2\2\u0123\u0128\5\22\n\2\u0124\u0128\5\30")
        buf.write("\r\2\u0125\u0128\5\24\13\2\u0126\u0128\5*\26\2\u0127\u011d")
        buf.write("\3\2\2\2\u0127\u011e\3\2\2\2\u0127\u011f\3\2\2\2\u0127")
        buf.write("\u0120\3\2\2\2\u0127\u0121\3\2\2\2\u0127\u0122\3\2\2\2")
        buf.write("\u0127\u0123\3\2\2\2\u0127\u0124\3\2\2\2\u0127\u0125\3")
        buf.write("\2\2\2\u0127\u0126\3\2\2\2\u0128?\3\2\2\2\u0129\u012a")
        buf.write("\7/\2\2\u012a\u012b\5B\"\2\u012b\u012c\7\60\2\2\u012c")
        buf.write("A\3\2\2\2\u012d\u012e\5D#\2\u012e\u012f\5B\"\2\u012f\u0132")
        buf.write("\3\2\2\2\u0130\u0132\3\2\2\2\u0131\u012d\3\2\2\2\u0131")
        buf.write("\u0130\3\2\2\2\u0132C\3\2\2\2\u0133\u013f\5F$\2\u0134")
        buf.write("\u013f\5H%\2\u0135\u013f\5J&\2\u0136\u013f\5L\'\2\u0137")
        buf.write("\u013f\5N(\2\u0138\u013f\5P)\2\u0139\u013f\5R*\2\u013a")
        buf.write("\u013f\5T+\2\u013b\u013f\5V,\2\u013c\u013f\5\32\16\2\u013d")
        buf.write("\u013f\5@!\2\u013e\u0133\3\2\2\2\u013e\u0134\3\2\2\2\u013e")
        buf.write("\u0135\3\2\2\2\u013e\u0136\3\2\2\2\u013e\u0137\3\2\2\2")
        buf.write("\u013e\u0138\3\2\2\2\u013e\u0139\3\2\2\2\u013e\u013a\3")
        buf.write("\2\2\2\u013e\u013b\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013d")
        buf.write("\3\2\2\2\u013fE\3\2\2\2\u0140\u0143\7\67\2\2\u0141\u0143")
        buf.write("\5\30\r\2\u0142\u0140\3\2\2\2\u0142\u0141\3\2\2\2\u0143")
        buf.write("\u0144\3\2\2\2\u0144\u0145\7\61\2\2\u0145\u0146\5\60\31")
        buf.write("\2\u0146\u0147\7-\2\2\u0147G\3\2\2\2\u0148\u0149\7\f\2")
        buf.write("\2\u0149\u014a\7\'\2\2\u014a\u014b\5\60\31\2\u014b\u014c")
        buf.write("\7(\2\2\u014c\u014d\5D#\2\u014d\u0157\3\2\2\2\u014e\u014f")
        buf.write("\7\f\2\2\u014f\u0150\7\'\2\2\u0150\u0151\5\60\31\2\u0151")
        buf.write("\u0152\7(\2\2\u0152\u0153\5D#\2\u0153\u0154\7\7\2\2\u0154")
        buf.write("\u0155\5D#\2\u0155\u0157\3\2\2\2\u0156\u0148\3\2\2\2\u0156")
        buf.write("\u014e\3\2\2\2\u0157I\3\2\2\2\u0158\u0159\7\n\2\2\u0159")
        buf.write("\u015c\7\'\2\2\u015a\u015d\7\67\2\2\u015b\u015d\5\30\r")
        buf.write("\2\u015c\u015a\3\2\2\2\u015c\u015b\3\2\2\2\u015d\u015e")
        buf.write("\3\2\2\2\u015e\u015f\7\61\2\2\u015f\u0160\5\60\31\2\u0160")
        buf.write("\u0161\7,\2\2\u0161\u0162\5\60\31\2\u0162\u0163\7,\2\2")
        buf.write("\u0163\u0164\5\60\31\2\u0164\u0165\7(\2\2\u0165\u0166")
        buf.write("\5D#\2\u0166K\3\2\2\2\u0167\u0168\7\21\2\2\u0168\u0169")
        buf.write("\7\'\2\2\u0169\u016a\5\60\31\2\u016a\u016b\7(\2\2\u016b")
        buf.write("\u016c\5D#\2\u016cM\3\2\2\2\u016d\u016e\7\6\2\2\u016e")
        buf.write("\u016f\5@!\2\u016f\u0170\7\21\2\2\u0170\u0171\7\'\2\2")
        buf.write("\u0171\u0172\5\60\31\2\u0172\u0173\7(\2\2\u0173\u0174")
        buf.write("\7-\2\2\u0174O\3\2\2\2\u0175\u0176\7\4\2\2\u0176\u0177")
        buf.write("\7-\2\2\u0177Q\3\2\2\2\u0178\u0179\7\24\2\2\u0179\u017a")
        buf.write("\7-\2\2\u017aS\3\2\2\2\u017b\u017c\7\16\2\2\u017c\u017d")
        buf.write("\5\60\31\2\u017d\u017e\7-\2\2\u017e\u0182\3\2\2\2\u017f")
        buf.write("\u0180\7\16\2\2\u0180\u0182\7-\2\2\u0181\u017b\3\2\2\2")
        buf.write("\u0181\u017f\3\2\2\2\u0182U\3\2\2\2\u0183\u0184\5*\26")
        buf.write("\2\u0184\u0185\7-\2\2\u0185W\3\2\2\2 _dqw\u0088\u0097")
        buf.write("\u00a5\u00b4\u00b8\u00bf\u00c3\u00c7\u00d6\u00da\u00e0")
        buf.write("\u00e2\u00e9\u00f0\u00fa\u0105\u0110\u0116\u011b\u0127")
        buf.write("\u0131\u013e\u0142\u0156\u015c\u0181")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'auto'", "'break'", "'boolean'", "'do'", 
                     "'else'", "'false'", "'float'", "'for'", "'function'", 
                     "'if'", "'integer'", "'return'", "'string'", "'true'", 
                     "'while'", "'void'", "'out'", "'continue'", "'of'", 
                     "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", 
                     "']'", "'.'", "','", "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                      "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                      "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", 
                      "CONTINUE", "OF", "INHERIT", "ARRAY", "ADD", "SUB", 
                      "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
                      "NOTEQUAL", "LESS", "LESSEQUAL", "GREATER", "GREATEREQUAL", 
                      "CONCAT", "LRB", "RRB", "LSB", "RSB", "DOT", "COMMA", 
                      "SEMI", "COLON", "LCB", "RCB", "ASSIGN", "CCOMMENT", 
                      "CPLUSCOMMENT", "INTLIT", "FLOATLIT", "STRINGLIT", 
                      "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_functyp = 3
    RULE_atomictyp = 4
    RULE_typ = 5
    RULE_exprlist = 6
    RULE_idlist = 7
    RULE_arraylit = 8
    RULE_arrayinit = 9
    RULE_dimensions = 10
    RULE_arrayindex = 11
    RULE_vardecl = 12
    RULE_varinit = 13
    RULE_funcdecl = 14
    RULE_funcpro = 15
    RULE_paramlist = 16
    RULE_paramprime = 17
    RULE_param = 18
    RULE_funcbody = 19
    RULE_funccall = 20
    RULE_arglist = 21
    RULE_argprime = 22
    RULE_expr = 23
    RULE_expr1 = 24
    RULE_expr2 = 25
    RULE_expr3 = 26
    RULE_expr4 = 27
    RULE_expr5 = 28
    RULE_expr6 = 29
    RULE_expr7 = 30
    RULE_blockstmt = 31
    RULE_stmtlist = 32
    RULE_stmt = 33
    RULE_assignstmt = 34
    RULE_ifstmt = 35
    RULE_forstmt = 36
    RULE_whilestmt = 37
    RULE_dowhilestmt = 38
    RULE_breakstmt = 39
    RULE_continuestmt = 40
    RULE_returnstmt = 41
    RULE_callstmt = 42

    ruleNames =  [ "program", "decllist", "decl", "functyp", "atomictyp", 
                   "typ", "exprlist", "idlist", "arraylit", "arrayinit", 
                   "dimensions", "arrayindex", "vardecl", "varinit", "funcdecl", 
                   "funcpro", "paramlist", "paramprime", "param", "funcbody", 
                   "funccall", "arglist", "argprime", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "blockstmt", 
                   "stmtlist", "stmt", "assignstmt", "ifstmt", "forstmt", 
                   "whilestmt", "dowhilestmt", "breakstmt", "continuestmt", 
                   "returnstmt", "callstmt" ]

    EOF = Token.EOF
    AUTO=1
    BREAK=2
    BOOLEAN=3
    DO=4
    ELSE=5
    FALSE=6
    FLOAT=7
    FOR=8
    FUNCTION=9
    IF=10
    INTEGER=11
    RETURN=12
    STRING=13
    TRUE=14
    WHILE=15
    VOID=16
    OUT=17
    CONTINUE=18
    OF=19
    INHERIT=20
    ARRAY=21
    ADD=22
    SUB=23
    MUL=24
    DIV=25
    MOD=26
    NOT=27
    AND=28
    OR=29
    EQUAL=30
    NOTEQUAL=31
    LESS=32
    LESSEQUAL=33
    GREATER=34
    GREATEREQUAL=35
    CONCAT=36
    LRB=37
    RRB=38
    LSB=39
    RSB=40
    DOT=41
    COMMA=42
    SEMI=43
    COLON=44
    LCB=45
    RCB=46
    ASSIGN=47
    CCOMMENT=48
    CPLUSCOMMENT=49
    INTLIT=50
    FLOATLIT=51
    STRINGLIT=52
    ID=53
    WS=54
    UNCLOSE_STRING=55
    ILLEGAL_ESCAPE=56
    UNTERMINATED_COMMENT=57
    ERROR_CHAR=58

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(MT22Parser.DecllistContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.decllist()
            self.state = 87
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MT22Parser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(MT22Parser.DecllistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = MT22Parser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.decl()
                self.state = 90
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MT22Parser.FuncdeclContext,0)


        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.funcdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_functyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctyp" ):
                return visitor.visitFunctyp(self)
            else:
                return visitor.visitChildren(self)




    def functyp(self):

        localctx = MT22Parser.FunctypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.AUTO) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING) | (1 << MT22Parser.VOID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomictypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomictyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomictyp" ):
                return visitor.visitAtomictyp(self)
            else:
                return visitor.visitChildren(self)




    def atomictyp(self):

        localctx = MT22Parser.AtomictypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atomictyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = MT22Parser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.AUTO) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING) | (1 << MT22Parser.ARRAY))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = MT22Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exprlist)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.expr()
                self.state = 107
                self.match(MT22Parser.COMMA)
                self.state = 108
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = MT22Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_idlist)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(MT22Parser.ID)
                self.state = 114
                self.match(MT22Parser.COMMA)
                self.state = 115
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = MT22Parser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MT22Parser.LCB)
            self.state = 120
            self.exprlist()
            self.state = 121
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayinitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def dimensions(self):
            return self.getTypedRuleContext(MT22Parser.DimensionsContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atomictyp(self):
            return self.getTypedRuleContext(MT22Parser.AtomictypContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arrayinit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayinit" ):
                return visitor.visitArrayinit(self)
            else:
                return visitor.visitChildren(self)




    def arrayinit(self):

        localctx = MT22Parser.ArrayinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arrayinit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(MT22Parser.ARRAY)
            self.state = 124
            self.match(MT22Parser.LSB)
            self.state = 125
            self.dimensions()
            self.state = 126
            self.match(MT22Parser.RSB)
            self.state = 127
            self.match(MT22Parser.OF)
            self.state = 128
            self.atomictyp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def dimensions(self):
            return self.getTypedRuleContext(MT22Parser.DimensionsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




    def dimensions(self):

        localctx = MT22Parser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_dimensions)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(MT22Parser.INTLIT)
                self.state = 131
                self.match(MT22Parser.COMMA)
                self.state = 132
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(MT22Parser.INTLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayindexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arrayindex

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayindex" ):
                return visitor.visitArrayindex(self)
            else:
                return visitor.visitChildren(self)




    def arrayindex(self):

        localctx = MT22Parser.ArrayindexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrayindex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(MT22Parser.ID)
            self.state = 137
            self.match(MT22Parser.LSB)
            self.state = 138
            self.exprlist()
            self.state = 139
            self.match(MT22Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(MT22Parser.TypContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def varinit(self):
            return self.getTypedRuleContext(MT22Parser.VarinitContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MT22Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_vardecl)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.idlist()
                self.state = 142
                self.match(MT22Parser.COLON)
                self.state = 143
                self.typ()
                self.state = 144
                self.match(MT22Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.varinit()
                self.state = 147
                self.match(MT22Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarinitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def varinit(self):
            return self.getTypedRuleContext(MT22Parser.VarinitContext,0)


        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(MT22Parser.TypContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_varinit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarinit" ):
                return visitor.visitVarinit(self)
            else:
                return visitor.visitChildren(self)




    def varinit(self):

        localctx = MT22Parser.VarinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_varinit)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(MT22Parser.ID)
                self.state = 152
                self.match(MT22Parser.COMMA)
                self.state = 153
                self.varinit()
                self.state = 154
                self.match(MT22Parser.COMMA)
                self.state = 155
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.match(MT22Parser.ID)
                self.state = 158
                self.match(MT22Parser.COLON)
                self.state = 159
                self.typ()
                self.state = 160
                self.match(MT22Parser.ASSIGN)
                self.state = 161
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcpro(self):
            return self.getTypedRuleContext(MT22Parser.FuncproContext,0)


        def funcbody(self):
            return self.getTypedRuleContext(MT22Parser.FuncbodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MT22Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.funcpro()
            self.state = 166
            self.funcbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncproContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def functyp(self):
            return self.getTypedRuleContext(MT22Parser.FunctypContext,0)


        def LRB(self):
            return self.getToken(MT22Parser.LRB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(MT22Parser.ParamlistContext,0)


        def RRB(self):
            return self.getToken(MT22Parser.RRB, 0)

        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funcpro

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncpro" ):
                return visitor.visitFuncpro(self)
            else:
                return visitor.visitChildren(self)




    def funcpro(self):

        localctx = MT22Parser.FuncproContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_funcpro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(MT22Parser.ID)
            self.state = 169
            self.match(MT22Parser.COLON)
            self.state = 170
            self.match(MT22Parser.FUNCTION)
            self.state = 171
            self.functyp()
            self.state = 172
            self.match(MT22Parser.LRB)
            self.state = 173
            self.paramlist()
            self.state = 174
            self.match(MT22Parser.RRB)
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INHERIT]:
                self.state = 175
                self.match(MT22Parser.INHERIT)
                self.state = 176
                self.match(MT22Parser.ID)
                pass
            elif token in [MT22Parser.LCB]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(MT22Parser.ParamprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = MT22Parser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_paramlist)
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT, MT22Parser.INHERIT, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.paramprime()
                pass
            elif token in [MT22Parser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MT22Parser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def paramprime(self):
            return self.getTypedRuleContext(MT22Parser.ParamprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = MT22Parser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_paramprime)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.param()
                self.state = 185
                self.match(MT22Parser.COMMA)
                self.state = 186
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(MT22Parser.TypContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MT22Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INHERIT]:
                self.state = 191
                self.match(MT22Parser.INHERIT)
                pass
            elif token in [MT22Parser.OUT, MT22Parser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT]:
                self.state = 195
                self.match(MT22Parser.OUT)
                pass
            elif token in [MT22Parser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 199
            self.match(MT22Parser.ID)
            self.state = 200
            self.match(MT22Parser.COLON)
            self.state = 201
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncbody" ):
                return visitor.visitFuncbody(self)
            else:
                return visitor.visitChildren(self)




    def funcbody(self):

        localctx = MT22Parser.FuncbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_funcbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LRB(self):
            return self.getToken(MT22Parser.LRB, 0)

        def arglist(self):
            return self.getTypedRuleContext(MT22Parser.ArglistContext,0)


        def RRB(self):
            return self.getToken(MT22Parser.RRB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = MT22Parser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_funccall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(MT22Parser.ID)
            self.state = 206
            self.match(MT22Parser.LRB)
            self.state = 207
            self.arglist()
            self.state = 208
            self.match(MT22Parser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argprime(self):
            return self.getTypedRuleContext(MT22Parser.ArgprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arglist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = MT22Parser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arglist)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.FALSE, MT22Parser.TRUE, MT22Parser.ARRAY, MT22Parser.SUB, MT22Parser.NOT, MT22Parser.LCB, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.argprime()
                pass
            elif token in [MT22Parser.RRB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def argprime(self):
            return self.getTypedRuleContext(MT22Parser.ArgprimeContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_argprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgprime" ):
                return visitor.visitArgprime(self)
            else:
                return visitor.visitChildren(self)




    def argprime(self):

        localctx = MT22Parser.ArgprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_argprime)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 214
                    self.match(MT22Parser.ID)
                    pass

                elif la_ == 2:
                    self.state = 215
                    self.expr()
                    pass


                self.state = 218
                self.match(MT22Parser.COMMA)
                self.state = 219
                self.argprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 220
                    self.match(MT22Parser.ID)
                    pass

                elif la_ == 2:
                    self.state = 221
                    self.expr()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr1Context,i)


        def CONCAT(self):
            return self.getToken(MT22Parser.CONCAT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.expr1()
                self.state = 227
                self.match(MT22Parser.CONCAT)
                self.state = 228
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr2Context,i)


        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(MT22Parser.NOTEQUAL, 0)

        def LESS(self):
            return self.getToken(MT22Parser.LESS, 0)

        def GREATER(self):
            return self.getToken(MT22Parser.GREATER, 0)

        def LESSEQUAL(self):
            return self.getToken(MT22Parser.LESSEQUAL, 0)

        def GREATEREQUAL(self):
            return self.getToken(MT22Parser.GREATEREQUAL, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = MT22Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.expr2(0)
                self.state = 234
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUAL) | (1 << MT22Parser.NOTEQUAL) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LESSEQUAL) | (1 << MT22Parser.GREATER) | (1 << MT22Parser.GREATEREQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 235
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 243
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 244
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 245
                    self.expr3(0) 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 254
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 255
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADD or _la==MT22Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 256
                    self.expr4(0) 
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def MUL(self):
            return self.getToken(MT22Parser.MUL, 0)

        def DIV(self):
            return self.getToken(MT22Parser.DIV, 0)

        def MOD(self):
            return self.getToken(MT22Parser.MOD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 270
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 265
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 266
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUL) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 267
                    self.expr5() 
                self.state = 272
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MT22Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr5)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(MT22Parser.NOT)
                self.state = 274
                self.expr5()
                pass
            elif token in [MT22Parser.FALSE, MT22Parser.TRUE, MT22Parser.ARRAY, MT22Parser.SUB, MT22Parser.LCB, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(MT22Parser.Expr7Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MT22Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr6)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(MT22Parser.SUB)
                self.state = 279
                self.expr6()
                pass
            elif token in [MT22Parser.FALSE, MT22Parser.TRUE, MT22Parser.ARRAY, MT22Parser.LCB, MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.STRINGLIT, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MT22Parser.STRINGLIT, 0)

        def TRUE(self):
            return self.getToken(MT22Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MT22Parser.FALSE, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def arraylit(self):
            return self.getTypedRuleContext(MT22Parser.ArraylitContext,0)


        def arrayindex(self):
            return self.getTypedRuleContext(MT22Parser.ArrayindexContext,0)


        def arrayinit(self):
            return self.getTypedRuleContext(MT22Parser.ArrayinitContext,0)


        def funccall(self):
            return self.getTypedRuleContext(MT22Parser.FunccallContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MT22Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr7)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(MT22Parser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 285
                self.match(MT22Parser.STRINGLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 286
                self.match(MT22Parser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 287
                self.match(MT22Parser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 288
                self.match(MT22Parser.ID)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 289
                self.arraylit()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 290
                self.arrayindex()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 291
                self.arrayinit()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 292
                self.funccall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(MT22Parser.StmtlistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = MT22Parser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(MT22Parser.LCB)
            self.state = 296
            self.stmtlist()
            self.state = 297
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(MT22Parser.StmtlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = MT22Parser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_stmtlist)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BREAK, MT22Parser.DO, MT22Parser.FOR, MT22Parser.IF, MT22Parser.RETURN, MT22Parser.WHILE, MT22Parser.CONTINUE, MT22Parser.LCB, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.stmt()
                self.state = 300
                self.stmtlist()
                pass
            elif token in [MT22Parser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(MT22Parser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(MT22Parser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MT22Parser.ForstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(MT22Parser.WhilestmtContext,0)


        def dowhilestmt(self):
            return self.getTypedRuleContext(MT22Parser.DowhilestmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MT22Parser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(MT22Parser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MT22Parser.ReturnstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(MT22Parser.CallstmtContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MT22Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_stmt)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.assignstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 307
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 308
                self.whilestmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 309
                self.dowhilestmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 310
                self.breakstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 311
                self.continuestmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 312
                self.returnstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 313
                self.callstmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 314
                self.vardecl()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 315
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def arrayindex(self):
            return self.getTypedRuleContext(MT22Parser.ArrayindexContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MT22Parser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 318
                self.match(MT22Parser.ID)
                pass

            elif la_ == 2:
                self.state = 319
                self.arrayindex()
                pass


            self.state = 322
            self.match(MT22Parser.ASSIGN)
            self.state = 323
            self.expr()
            self.state = 324
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LRB(self):
            return self.getToken(MT22Parser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RRB(self):
            return self.getToken(MT22Parser.RRB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StmtContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StmtContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MT22Parser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ifstmt)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.match(MT22Parser.IF)
                self.state = 327
                self.match(MT22Parser.LRB)
                self.state = 328
                self.expr()
                self.state = 329
                self.match(MT22Parser.RRB)
                self.state = 330
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.match(MT22Parser.IF)
                self.state = 333
                self.match(MT22Parser.LRB)
                self.state = 334
                self.expr()
                self.state = 335
                self.match(MT22Parser.RRB)
                self.state = 336
                self.stmt()
                self.state = 337
                self.match(MT22Parser.ELSE)
                self.state = 338
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LRB(self):
            return self.getToken(MT22Parser.LRB, 0)

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def RRB(self):
            return self.getToken(MT22Parser.RRB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def arrayindex(self):
            return self.getTypedRuleContext(MT22Parser.ArrayindexContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MT22Parser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(MT22Parser.FOR)
            self.state = 343
            self.match(MT22Parser.LRB)
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 344
                self.match(MT22Parser.ID)
                pass

            elif la_ == 2:
                self.state = 345
                self.arrayindex()
                pass


            self.state = 348
            self.match(MT22Parser.ASSIGN)
            self.state = 349
            self.expr()
            self.state = 350
            self.match(MT22Parser.COMMA)
            self.state = 351
            self.expr()
            self.state = 352
            self.match(MT22Parser.COMMA)
            self.state = 353
            self.expr()
            self.state = 354
            self.match(MT22Parser.RRB)
            self.state = 355
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LRB(self):
            return self.getToken(MT22Parser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RRB(self):
            return self.getToken(MT22Parser.RRB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_whilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestmt" ):
                return visitor.visitWhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def whilestmt(self):

        localctx = MT22Parser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(MT22Parser.WHILE)
            self.state = 358
            self.match(MT22Parser.LRB)
            self.state = 359
            self.expr()
            self.state = 360
            self.match(MT22Parser.RRB)
            self.state = 361
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DowhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LRB(self):
            return self.getToken(MT22Parser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RRB(self):
            return self.getToken(MT22Parser.RRB, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dowhilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhilestmt" ):
                return visitor.visitDowhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhilestmt(self):

        localctx = MT22Parser.DowhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_dowhilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(MT22Parser.DO)
            self.state = 364
            self.blockstmt()
            self.state = 365
            self.match(MT22Parser.WHILE)
            self.state = 366
            self.match(MT22Parser.LRB)
            self.state = 367
            self.expr()
            self.state = 368
            self.match(MT22Parser.RRB)
            self.state = 369
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MT22Parser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(MT22Parser.BREAK)
            self.state = 372
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MT22Parser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(MT22Parser.CONTINUE)
            self.state = 375
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MT22Parser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_returnstmt)
        try:
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.match(MT22Parser.RETURN)
                self.state = 378
                self.expr()
                self.state = 379
                self.match(MT22Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.match(MT22Parser.RETURN)
                self.state = 382
                self.match(MT22Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funccall(self):
            return self.getTypedRuleContext(MT22Parser.FunccallContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = MT22Parser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.funccall()
            self.state = 386
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[25] = self.expr2_sempred
        self._predicates[26] = self.expr3_sempred
        self._predicates[27] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




