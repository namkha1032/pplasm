grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decllist EOF ;

// Cau 1 viet declare list co the declare nhieu lan, mot declare co the la var hoac func
decllist: decl decllist | decl;
decl: vardecl | funcdecl;

// Cau 2 viet mo ta cho vardec va funcdec
// vardec bat dau bang mot type, type co the la int hoac float, 
// theo do la danh sach cac ID cach nhau boi dau COMMA, ket thuc boi dau ;
vardecl: typ idlist SEMI;
typ: INT | FLOAT;
idlist: ID COMMA idlist | ID;
// funcdec bat dau bang mot type, sau do la ID ten ham
// tiep theo la khai bao param, ket thuc bang mot body
// param bat dau bang (), o giua la cac khai bao cac thong so bat dau bang ; co the rong
// moi khai bao thong so bat dau bang ten, tiep theo do la danh sach cac ID cach nhau boi dau COMMA
funcdecl: typ ID paramdecl body;
paramdecl: LB paramlist RB;
paramlist: paramprime | ;
paramprime: param SEMI paramprime | param;
param: typ idlist; 

//Cau 3: Mo ta body
// Body bat dau ket thuc bang {}, trong body co the co nhieu var decl hoac statement
// Co 3 loai statement:assign, call, return
// Statement ket thuc bang dau SEMI
//		- assign bat dau bang mot ID, sau do la dau '=', sau do la expression
//		- call bat dau bang mot ID, sau do la mot list cac expression cach nhau boi COMMA enclose by (), co the rong
//		- return bat dau bang keyword 'return', sau do la expression
// expression da duoc dac ta san
body: LP stmtlist RP;
stmtlist: stmt stmtlist | ;
stmt: vardecl | assignstmt | callstmt | returnstmt;
assignstmt: ID EQ expr SEMI;
callstmt: ID LB exprlist RB SEMI;
exprlist: exprprime | ;
exprprime: expr COMMA exprprime | expr;
returnstmt: RETURN expr;
//Cau 4: mo ta expression
// expression bao gom operator va operand
// co 4 indix operator: + - * /
//+ < - < (* /)
//+ is right assoc
//- is non assoc
// * / is left assoc
// subex is enclosed in roundbracket
// operand can be intlit, floatlit, ID, call expression, sub-ex
// callexpr khac voi call: (callexpr la call bo di dau SEMI)
//	foo(): call (phat bieu goi ham)
//	foo() + 1: callexpr (bieu thuc goi ham)
expr: expr1 ADD expr | expr1;
expr1: expr2 SUB expr2 | expr2;
expr2: expr2 (MUL | DIV) expr3 | expr3;
expr3: INTLIT | FLOATLIT | ID | callexpr | subexpr;
callexpr: ID LB exprlist RB;
subexpr: LB expr RB;
// Cau 4: mieu ta expression
// -----------------------------------------------------------------------
//-----------------TOKEN----------------------------



//Keyword
INT: 'int';
FLOAT: 'float';
RETURN: 'return';
//Separator
SEMI: ';';
COMMA: ',';
LB: '(';
RB: ')';
LP: '{';
RP: '}';
EQ: '=';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
//Regex
INTLIT: [0-9]+;
FLOATLIT: [0-9]+'.'[0-9]+ | [0-9]+ ('.'[0-9])?([eE][0-9]+);
ID:[a-zA-Z]+;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// fragment
fragment INTPART: 

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;