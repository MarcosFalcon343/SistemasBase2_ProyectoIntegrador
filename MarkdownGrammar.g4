grammar MarkdownGrammar;

// --- PARSER ---

doc : (block | NEWLINE)* EOF;

block
    : horizontalRule
    | header
    | table
    | blockquote
    | list
    | paragraph
    ;

header : HASHES inlineContent? NEWLINE;
blockquote : blockquoteLine+;
blockquoteLine : GT inlineContent? NEWLINE;
list : listItem+ ;

listItem
    : ul_marker inlineContent NEWLINE        # unorderedItem
    | OL_NUM inlineContent NEWLINE           # orderedItem
    ;

ul_marker : STAR | PLUS | MINUS ;

horizontalRule : (HR_DASH | HR_STAR | HR_UNDER | BOLD_ITALIC_STAR) NEWLINE;

// --- TABLAS -
table : tableHeaderLine tableSepLine tableBodyLine*;

// Cabecera: Una fila normal
tableHeaderLine : tableRow;


tableSepLine : WS? PIPE (WS? (DASHES | HR_DASH | MINUS | DASHES_COLON | COLON_DASHES | COLON_DASHES_COLON) WS? PIPE)+ WS? NEWLINE;

// Cuerpo: Filas normales
tableBodyLine : tableRow;

// Fila: | celda | celda |
tableRow : WS? PIPE (inlineItem_no_pipe* PIPE)+ WS? NEWLINE;

paragraph : inlineContent NEWLINE;

inlineContent : inlineItem+ ;

inlineItem
    : link
    | bold_italic
    | bold
    | italic
    | strikethrough
    | WS
    | INDENT
    | TEXT
    | DOT | COLON
    | STAR | PLUS | MINUS | HASHES | GT | OL_NUM | HR_DASH | HR_STAR | HR_UNDER
    | PIPE | COLON_DASHES_COLON | DASHES_COLON | COLON_DASHES | DASHES
    | BOLD_ITALIC_STAR | BOLD_ITALIC_STAR_UNDER_START | BOLD_ITALIC_STAR_UNDER_END
    | BOLD_ITALIC_UNDER_STAR_START | BOLD_ITALIC_UNDER_STAR_END
    | BOLD_STAR | BOLD_UNDER | STRIKE | UNDER
    | LBRACKET | RBRACKET | LPAREN | RPAREN
    | ANY_SYMBOL
    ;

inlineItem_no_pipe
    : link
    | bold
    | italic
    | strikethrough
    | WS
    | INDENT
    | TEXT
    | ANY_SYMBOL_NO_PIPE
    | DOT | COLON
    | STAR | PLUS | MINUS | HASHES | GT | OL_NUM | HR_DASH | HR_STAR | HR_UNDER
    | BOLD_ITALIC_STAR | BOLD_ITALIC_STAR_UNDER_START | BOLD_ITALIC_STAR_UNDER_END
    | BOLD_ITALIC_UNDER_STAR_START | BOLD_ITALIC_UNDER_STAR_END
    | BOLD_STAR | BOLD_UNDER | STRIKE | UNDER
    | LBRACKET | RBRACKET | LPAREN | RPAREN
    ;

bold_italic
    : (BOLD_ITALIC_STAR inlineContent BOLD_ITALIC_STAR)
    | (BOLD_ITALIC_STAR_UNDER_START inlineContent BOLD_ITALIC_STAR_UNDER_END)
    | (BOLD_ITALIC_UNDER_STAR_START inlineContent BOLD_ITALIC_UNDER_STAR_END)
    ;
bold
    : (BOLD_STAR inlineContent BOLD_STAR)
    | (BOLD_UNDER inlineContent BOLD_UNDER)
    ;
italic
    : (STAR inlineContent STAR)
    | (UNDER inlineContent UNDER)
    ;
strikethrough : STRIKE inlineContent STRIKE;
link : LBRACKET inlineContent RBRACKET LPAREN URL RPAREN;

// --- LEXER ---

NEWLINE  : [\r\n]+ ;
HASHES   : '#' + ;
GT       : '>' ;
INDENT   : [ \t]{2,} ;

BOLD_ITALIC_STAR: '***';
BOLD_ITALIC_STAR_UNDER_START: '**_';
BOLD_ITALIC_STAR_UNDER_END: '_**';
BOLD_ITALIC_UNDER_STAR_START: '__*';
BOLD_ITALIC_UNDER_STAR_END: '*__';
BOLD_STAR  : '**' ;
BOLD_UNDER : '__' ;
STRIKE     : '~~' ;

HR_DASH  : '---' '-'* ;
HR_STAR  : '****' '*'* ;
HR_UNDER : '___' '_'* ;

STAR      : '*' ;
PLUS      : '+' ;
MINUS     : '-' ;
UNDER     : '_' ;
DOT       : '.' ;
COLON     : ':' ;

OL_NUM    : [0-9]+ DOT ;

PIPE     : '|' ;
COLON_DASHES_COLON : ':' '-' '-'* ':' ;
DASHES_COLON       : '-' '-'* ':' ;
COLON_DASHES       : ':' '-' '-'* ;
DASHES             : '-' '-'* ;

LBRACKET : '[' ;
RBRACKET : ']' ;
LPAREN   : '(' ;
RPAREN   : ')' ;

URL      : 'http' [a-zA-Z0-9:/?#[\]@!$&'*+,;=.\-_%]+ ;

WS : [ \t]+ ;

TEXT : ~[#*+\-_>~[\]():|.\r\n]+ ;

ANY_SYMBOL_NO_PIPE : ~[|\r\n] ;
ANY_SYMBOL : . ;