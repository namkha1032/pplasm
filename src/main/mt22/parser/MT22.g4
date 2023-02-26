grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decllist  EOF ;

// -----------------------------------------------------------------------
// ------------------------------PARSER-----------------------------------
// -----------------------------------------------------------------------

decllist: decl decllist | decl;
decl:  vardecl | funcdecl | stmt;

// type
functyp: BOOLEAN | INTEGER | FLOAT | STRING | AUTO | VOID;
atomictyp: BOOLEAN | INTEGER | FLOAT | STRING ;
typ: BOOLEAN | INTEGER | FLOAT | STRING | AUTO | ARRAY;
// Expr list
exprlist: expr COMMA exprlist | expr;
// ID list
idlist: ID COMMA idlist | ID;
// Literals - parser
arraylit: LCB exprlist RCB;
// Array declaration
arrayinit: ARRAY LSB dimensions RSB OF atomictyp;
dimensions: INTLIT COMMA dimensions | INTLIT;
arrayindex: ID LSB exprlist RSB;
// Var declaration
vardecl:  idlist COLON typ SEMI
	    | varinit SEMI; // init var
varinit: (ID COMMA varinit COMMA expr) | (ID COLON typ ASSIGN expr) ; 
// Func declaration
funcdecl: funcpro funcbody;
// Func prototype
funcpro:  ID COLON FUNCTION functyp LRB paramlist RRB (INHERIT ID | );
paramlist : paramprime | ;
paramprime: param COMMA paramprime| param;
param: (INHERIT | ) (OUT | ) ID COLON typ ;
// Func body
funcbody: blockstmt;
// Func call
funccall: ID LRB arglist RRB;
arglist: argprime | ;
argprime: (ID | expr) COMMA argprime| (ID | expr); 
// Operator precedence and assoc
expr : expr1 CONCAT expr1 | expr1;
expr1: expr2 (EQUAL | NOTEQUAL | LESS | GREATER | LESSEQUAL | GREATEREQUAL) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: INTLIT | FLOATLIT  | STRINGLIT | TRUE | FALSE | ID | arraylit | arrayindex | arrayinit | funccall;

// Statement
blockstmt: LCB stmtlist RCB;
stmtlist: stmt stmtlist | ;
stmt: assignstmt | ifstmt | forstmt | whilestmt | dowhilestmt | breakstmt | continuestmt | returnstmt | callstmt | vardecl | blockstmt ;
// Assign statement
assignstmt: (ID | arrayindex) ASSIGN expr SEMI;
// If statement
// ifstmt: matchstmt 
// 	  | unmatchstmt;
// matchstmt: IF LRB expr RRB matchstmt ELSE matchstmt 
// 		 | stmt;
// unmatchstmt: IF LRB expr RRB ifstmt
// 		   | IF LRB expr RRB matchstmt ELSE unmatchstmt;
ifstmt: IF LRB expr RRB stmt
	  | IF LRB expr RRB stmt ELSE stmt;
// For statement
forstmt: FOR LRB (ID | arrayindex) ASSIGN expr COMMA expr COMMA expr RRB stmt;

// While statement
whilestmt: WHILE LRB expr RRB stmt;

// Do-while statement
dowhilestmt: DO blockstmt WHILE LRB expr RRB SEMI;
// Break statement
breakstmt: BREAK SEMI;

// Continue statement
continuestmt: CONTINUE SEMI; 
// Return statement
returnstmt: RETURN expr SEMI | RETURN SEMI;
// Call statment
callstmt: funccall SEMI;

// -----------------------------------------------------------------------
// ------------------------------LEXER------------------------------------
// -----------------------------------------------------------------------


// Keyword
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true'; 
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

// Operators
ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
MOD : '%';
NOT : '!';
AND : '&&';
OR : '||';
EQUAL : '==';
NOTEQUAL : '!=';
LESS : '<';
LESSEQUAL : '<=';
GREATER : '>';
GREATEREQUAL : '>=';
CONCAT: '::';

// Separator
LRB : '(';
RRB : ')';
LSB : '[';
RSB : ']';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';
LCB : '{';
RCB : '}';
ASSIGN: '=';

// C style comment
CCOMMENT:   '/*' .*? '*/' -> skip;
// C++ style comment
CPLUSCOMMENT:   '//' ~[\n]* -> skip;
// Literals - lexer
INTLIT: '0' | [1-9] [0-9]* ('_'[0-9]+)* {self.text = self.text.replace("_","")};
FLOATLIT: (([0-9]+)('_'[0-9]+)*('.'[0-9]+)('_'[0-9]+)* | ([0-9]+)('_'[0-9]+)*('.'[0-9]+)?('_'[0-9]+)*([eE][-]?[0-9]+)('_'[0-9]+)*) {self.text = self.text.replace("_","")};
// BOOLLIT: 'true' | 'false';
STRINGLIT: ["] (~[\\\n\b\f\r\t'"] | [\\][bfrnt'"\\])*["] {self.text = self.text[1:-1]};
//
ID: ( [a-zA-Z] | '_' ) ([a-zA-Z]  | [0-9] | '_') * ; 
// Whitespace
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


// Error
UNCLOSE_STRING: ["] (~[\\\n\b\f\r\t'"] | [\\][bfrnt'"\\])*[\n]? {
	if self.text.find('\n') != -1:
		pos = self.text.find('\n')
		raise UncloseString(self.text[1:pos])
	else:
		raise UncloseString(self.text[1:])
	};

ILLEGAL_ESCAPE: ["] (~[\\\n\b\f\r\t'"] | [\\][bfrnt'"\\])*[\\]~[bfrnt'"\\] {raise IllegalEscape(self.text[1:])};

UNTERMINATED_COMMENT: '/*' ~[(*/)]*[\n]? {
	if self.text.find('\n') != -1:
		pos = self.text.find('\n')
		raise UnterminatedComment(self.text[0:pos-1])
	else:
		raise UnterminatedComment(self.text[0:])
	};
ERROR_CHAR: .{raise ErrorToken(self.text)};


// comment
// floatlit
// stringlit
// error