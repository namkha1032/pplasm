/*
	ASSIGNMENT 1 - PPL
	NGUYEN NGOC HOA - 2052485
*/


grammar hoa;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
			/////////////////////////////////////////////////////
			///					    PARSER					/////
			/////////////////////////////////////////////////////
program: decl EOF ;
//					declaration
decl: (vardecl | funcdecl ) decl | (vardecl | funcdecl );

// type grammar
typ: INTEGER | FLOAT | BOOLEAN | STRING | AUTO | array_typ; 
atomic_typ: INTEGER | FLOAT | BOOLEAN | STRING ;
func_typ: INTEGER | FLOAT | BOOLEAN | STRING | AUTO | VOID | array_typ; 
// variable decl

vardecl:  idlist COLON typ SEMI
	    | fullformat SEMI; // full format
fullformat: (ID COMMA fullformat COMMA expr) | (ID COLON typ ASSIGN expr) ; 
//				<identifier-list>
idlist: ID COMMA idlist | ID ;
//					array
array_typ: ARRAY LSB dimension RSB OF atomic_typ;
dimension: INT_LIT COMMA dimension | INT_LIT;

array_literal: LCB exprlist RCB;
exprlist: exprlist1 | ;
exprlist1: expr COMMA exprlist1 | expr;

array_index: ID LSB index_expr RSB;
index_expr: expr COMMA index_expr | expr;
//				function declaration
funcdecl: funcpro funcbody ;
// 				function prototype
funcpro:  ID COLON FUNCTION func_typ LB paralist RB
		| ID COLON FUNCTION func_typ LB paralist RB INHERIT ID ;
//				function body
funcbody: block_stmt; 				// block of statement define later
//				list of para
paralist : paralist1 | ;
paralist1: para COMMA paralist1| para;
//			<parameter>
para: INHERIT? OUT? ID COLON typ ;
//				function call
funccall: ID LB exprlist RB;



//
//
literal: INT_LIT | FLOAT_LIT | TRUE | FALSE | STRING_LIT | array_literal;
sub_expr: (LB expr RB);
// 						expression
expr : expr1 CONCAT expr1 | expr1; // STRING 
expr1: expr2 (EQUAL | NOT_EQUAL | GREATER | GREATER_EQUAL | LESS | LESS_EQUAL) expr2 | expr2; // RELATIONAL
expr2: expr2 (AND | OR) expr3 | expr3; //LOGICAL
expr3: expr3 (ADD | SUB) expr4 | expr4; //ADDING
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5; //MULTIPLYING
expr5: NOT expr5 | expr6; //LOGICAL
expr6: SUB expr6 | expr7; //SIGN
expr7: literal | sub_expr | funccall | ID | array_index; // 

					// statement
stmt: assign_stmt
	| if_stmt
	| for_stmt
	| while_stmt
	| do_while_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| block_stmt
	| call_stmt; 

// non_block_stmt:   assign_stmt
// 				| if_stmt
// 				| for_stmt
// 				| while_stmt
// 				| do_while_stmt
// 				| break_stmt
// 				| continue_stmt
// 				| return_stmt
// 				| call_stmt;

assign_stmt: (ID | array_index) ASSIGN expr SEMI; 


if_stmt: IF LB expr RB stmt
		|IF LB expr RB stmt ELSE stmt;

for_stmt: FOR LB (ID | array_index) ASSIGN expr COMMA expr COMMA expr RB stmt;

while_stmt: WHILE LB expr RB stmt;

do_while_stmt: DO block_stmt WHILE LB expr RB SEMI;

break_stmt: BREAK SEMI;
continue_stmt: CONTINUE SEMI; 
return_stmt: RETURN SEMI
			|RETURN expr SEMI;
call_stmt: funccall SEMI;

block_stmt: LCB block_body RCB ;
block_body: (stmt | vardecl) block_body | ;

			/////////////////////////////////////////////////////
			///					    LEXER					/////
			/////////////////////////////////////////////////////

// 						type
// 						keywords

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

//				operator

ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
MOD : '%';

AND : '&&';
OR : '||';
NOT : '!';

EQUAL : '==';
NOT_EQUAL : '!=';

LESS : '<';
LESS_EQUAL : '<=';
GREATER : '>';
GREATER_EQUAL : '>=';

CONCAT: '::';

//				seperators
ASSIGN: '=';
LB : '(';
RB : ')';
LSB : '[';
RSB : ']';
LCB : '{';
RCB : '}';
SEMI: ';';
COLON: ':';
COMMA: ',';
DOT: '.';

// 				Indentifier
ID: ( Letter | Underscore ) (Letter | Digit | Underscore) * ; 

// 					Literal
INT_LIT: ('0' | DigitNonZero (Underscore ? Digit) *) {self.text = self.text.replace('_','')};
FLOAT_LIT: ((('0' | DigitNonZero (Underscore ? Digit) *) (DecimalPart ExponentPart ? | ExponentPart)) | (DecimalPart ExponentPart)) {self.text = self.text.replace('_','')};
BOOL_LIT: TRUE | FALSE ;
STRING_LIT: '"'  ( StringChar | EscapeSeq )* '"' {self.text = self.text[1:-1]};
 

// 				fragment

fragment Letter: [a-zA-Z];
fragment Digit: [0-9];
fragment DigitNonZero: [1-9];
fragment Underscore: '_';

fragment DecimalPart: DOT Digit*; 
fragment ExponentPart: [eE] [+-] ? Digit +;

fragment StringChar: (~[\\"\n]);
fragment EscapeSeq: '\\' [bfrnt'"\\]; 
fragment Illegal_EscapeSeq: '\\' ~[bfrnt'"\\] | '\'' ~'"'; 




WS : [ \t\b\f\r\n]+ -> skip ; // skip spaces, tabs, newlines

BLOCK_CMT:   '/*' .*? '*/' -> skip; //NON-GREEDY

LINE_CMT:   '//' ~[\r\n]* -> skip;

// UNTERMINATED_COMMENT:

ILLEGAL_ESCAPE: '"' ( StringChar | EscapeSeq )*  Illegal_EscapeSeq {
					textt = str(self.text)
					raise IllegalEscape(textt[1:])	
};

UNCLOSE_STRING: '"'  ( StringChar | EscapeSeq )* (EOF | '\n') { 
					textt = str(self.text)
					if textt[-1] in ['\n']:
						raise UncloseString(textt[1:-1])
					else:
						raise UncloseString(textt[1:])

}; 

ERROR_CHAR: . {raise ErrorToken(self.text)};