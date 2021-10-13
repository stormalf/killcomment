grammar killComment;

/* PARSER rules always in lower case */
program: line+ EOF;
line: instruction | comments | NEWLINE;
comments: COMMENT_HASHTAG NEWLINE?
| COMMENT_TRIPLE_SINGLE_QUOTES NEWLINE?
| COMMENT_TRIPLE_DOUBLE_QUOTES NEWLINE?
| COMMENT_DOUBLE_SLASHES NEWLINE?
| COMMENT_SLASH_STAR NEWLINE?
| COMMENT_DOUBLE_HYPHEN NEWLINE?
;
instruction: ALL NEWLINE?;

//LEXER rules
COMMENT_HASHTAG: WS* '#' ~[\r\n\f]+ | WS* '#';
COMMENT_TRIPLE_SINGLE_QUOTES:  WS* '\'\'\'' .*? '\'\'\'';
COMMENT_TRIPLE_DOUBLE_QUOTES:  WS* '"""' .*?  '"""';
COMMENT_DOUBLE_SLASHES : WS* '//' ~[\r\n\f]* | WS* '//' ; 
COMMENT_SLASH_STAR: WS* '/*'  .*?  '*/' ;
COMMENT_DOUBLE_HYPHEN : WS* '--'  ~[\r\n\f]+ |WS* '--';
NEWLINE: ('\r' '\n'? | '\n')+ ;
ALL: (~[\r\n])+ ;
WS  : [ \t]+ -> skip ; 
