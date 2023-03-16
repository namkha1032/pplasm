// Nguyễn Nam Kha
// 2052515
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
decl:  vardecl | funcdecl;

// type
typ: BOOLEAN | INTEGER | FLOAT | STRING | AUTO | arraytyp;
atomictyp: BOOLEAN | INTEGER | FLOAT | STRING ;
functyp: BOOLEAN | INTEGER | FLOAT | STRING | AUTO | VOID | arraytyp;
// Array type, lit
arraytyp: ARRAY LSB dimensions RSB OF atomictyp;
dimensions: INTLIT COMMA dimensions | INTLIT;
arrayindex: ID LSB exprlistnonnull RSB;
arraylit: LCB exprlistnullable RCB;
// Expr list
exprlistnullable: exprlistnonnull | ;
exprlistnonnull: expr COMMA exprlistnonnull | expr;
// ID list
idlist: ID COMMA idlist | ID;
// Var declaration
vardecl:  idlist COLON typ SEMI
	    | varinit SEMI; // init var
varinit: (ID COMMA varinit COMMA expr) | (ID COLON typ ASSIGN expr) ; 
// Func declaration
funcdecl: funcpro funcbody;
// Func prototype
funcpro:  ID COLON FUNCTION functyp LRB paramlistnullable RRB
		| ID COLON FUNCTION functyp LRB paramlistnullable RRB INHERIT ID;
paramlistnullable : paramlistnonnull | ;
paramlistnonnull: param COMMA paramlistnonnull| param;
param: ID COLON typ
	 | INHERIT ID COLON typ
	 | OUT ID COLON typ
	 | INHERIT OUT ID COLON typ;
// Func body
funcbody: blockstmt;
// Func call
funccall: ID LRB exprlistnullable RRB;
// Operator precedence and assoc
expr : expr1 CONCAT expr1 | expr1;
expr1: expr2 EQUAL expr2
	 | expr2 NOTEQUAL expr2
	 | expr2 LESS expr2  
	 | expr2 GREATER expr2  
	 | expr2 LESSEQUAL expr2  
	 | expr2 GREATEREQUAL expr2  
	 | expr2;
expr2: expr2 AND expr3 
	 | expr2 OR expr3 
 	 | expr3;
expr3: expr3 ADD expr4 
	 | expr3 ADD expr4 
	 | expr4;
expr4: expr4 MUL expr5 
	 | expr4 DIV expr5 
	 | expr4 MOD expr5 
	 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: INTLIT | FLOATLIT  | STRINGLIT | TRUE | FALSE | ID | arraylit | arrayindex | funccall | (LRB expr RRB);

// Statement
blockstmt: LCB stmtlist RCB;
stmtlist: stmt stmtlist 
		| vardecl stmtlist ;
stmt: assignstmt 
	| ifstmt 
	| forstmt 
	| whilestmt 
	| dowhilestmt 
	| breakstmt 
	| continuestmt 
	| returnstmt
	| callstmt
	| blockstmt ;
// Assign statement
assignstmt: ID ASSIGN expr SEMI
		  | arrayindex ASSIGN expr SEMI;
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
forstmt: FOR LRB ID ASSIGN expr COMMA expr COMMA expr RRB stmt
       | FOR LRB arrayindex ASSIGN expr COMMA expr COMMA expr RRB stmt;

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