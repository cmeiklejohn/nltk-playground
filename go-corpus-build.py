import pygments 
import pygments.lexers

def _remove_block_comments(txt, delim):
    'Strips first nest of block comments'
 
    deliml, delimr = delim
    out = ''
    if deliml in txt:
        indx = txt.index(deliml)
        out += txt[:indx]
        txt = txt[indx+len(deliml):]
        txt = _remove_block_comments(txt, delim)
        assert delimr in txt, 'Cannot find closing comment delimiter in ' + txt
        indx = txt.index(delimr)
        out += txt[(indx+len(delimr)):]
    else:
        out = txt
    return out
 
def remove_block_comments(txt, delim=('/*', '*/')):
    'Strips nests of block comments'
 
    deliml, delimr = delim
    while deliml in txt:
        txt = _remove_block_comments(txt, delim)
    return txt

def tokenize(filename, output):
    try:
        data = ""

        # Read in the example Go file.
        with open(filename, 'r') as fh:
            for line in fh:
                line = line
                data = data + line

        # Remove block comments
        data = remove_block_comments(data)
        data = remove_block_comments(data, delim=('//', '\n'))

        # Attempt to guess the lexer.
        lexer = pygments.lexers.guess_lexer_for_filename(filename, data)

        # Attempt to lex.
        tokens = pygments.lex(data, lexer)
        for token in tokens:
            # print token[1],
            output.write(token[1])
    except:
        print "Skipping file due to parse error: " + filename

import os

# Iterate the Go corpus.
go_corpus = "go-corpus"

with open("go-corpus.txt", "w") as output:
    for subdir, dirs, files in os.walk(go_corpus):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".go"):
                print (filepath)
                tokenize(filepath, output)