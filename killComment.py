#!/usr/bin/python3
# encoding: utf-8
import sys
from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from killCommentLexer import killCommentLexer
from killCommentParser import killCommentParser
from antlr4.tree.Trees import Trees
import argparse

__version__ = "1.0.0"

PY_LIKE = [killCommentParser.COMMENT_HASHTAG, killCommentParser.COMMENT_TRIPLE_SINGLE_QUOTES, killCommentParser.COMMENT_TRIPLE_DOUBLE_QUOTES]
SHELL_LIKE = [killCommentParser.COMMENT_HASHTAG]
C_LIKE = [killCommentParser.COMMENT_DOUBLE_SLASHES, killCommentParser.COMMENT_SLASH_STAR]
SQL_LIKE = [killCommentParser.COMMENT_DOUBLE_HYPHEN, killCommentParser.COMMENT_SLASH_STAR]

def validComment(typeComment):
    if typeComment == "py-like":
        return PY_LIKE
    elif typeComment == "c-like":
        return C_LIKE
    elif typeComment == "shell-like":
        return SHELL_LIKE
    elif typeComment == "sql-like":
        return SQL_LIKE

    return 

def main(file, typeComment):
    filename = file
    filewext = file.split('.')[0]
    woComment = filewext + ".woc"
    input_stream = FileStream(filename, encoding="utf-8")
    output = open(woComment, "w")

    lexer = killCommentLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = killCommentParser(stream)
    tree = parser.program()
    #print(Trees.toStringTree(tree, None, parser))
    removeComment(tree, output, typeComment)
    output.close()
    
def removeComment(tree, output3, typeComment):
    if tree.getText() == "<EOF>":
        return
    elif isinstance(tree, TerminalNodeImpl): 
        # if tree.getSymbol().type != killCommentParser.COMMENT and tree.getSymbol().type != killCommentParser.NEWLINE:   
        if tree.getSymbol().type not in validComment(typeComment) and tree.getSymbol().type != killCommentParser.NEWLINE:
            output3.write(tree.getText() + "\n")                    
    else:
        #print(tree.getText())
        for child in tree.children:
            removeComment(child, output3, typeComment)        

def killCommentVersion():
    return "killComment version : " + __version__
 
if __name__ == '__main__':
    description = "killComment is a python3 program that removes comment and compact code.\n"
    description = description + "It compacts code too but keep readable and executable\n"
    description = description + "Only some comments are taken in account :\n"
    description = description + " - c-like : /*...*/ and //\n"
    description = description + " - py-like : # and ''' and \"\"\"\n"
    description = description + " - shell-like : #\n"
    description = description + " - SQL-like : -- and /* */\n"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-V', '--version', help='Display the version of killComment', action='version', version=killCommentVersion())
    parser.add_argument('filename', help="file to remove comment and compact")
    parser.add_argument('-t', '--type', help="type of comments to remove c-like, py-like, shell-like, sql-like", default="py-like", choices=["py-like", "c-like", "shell-like", "sql-like"], required=False)
    args = parser.parse_args()
    main(args.filename, args.type)        
