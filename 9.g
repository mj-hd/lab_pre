#!/usr/bin/python

%%
parser WIFH:
    token CHAR:   '[A-Za-z]+'
    token NUM:    '[0-9]+'
    token END:    '$'

    rule str:   CHAR                   {{ result = CHAR }}
                (
                  CHAR                 {{ result += CHAR }}
                | NUM                  {{ result += result[-1] * (int(NUM)-1) }}
                ) *                    {{ return result }}
    rule repeat: '\('                  {{ result = "" }}
                    (
                      str              {{ result += str }}
                    | repeat           {{ result += repeat }}
                    ) *
                 '\)' NUM              {{ return result * int(NUM) }}
    rule expr:                         {{ result = "" }}
                 (
                  str                  {{ result += str }}
                  | repeat             {{ result += repeat }}
                 ) *                   {{ return result }}
    rule statement:   expr END         {{ return expr }}

%%

for line in open("./code.txt", "r"):
	print parse("statement", line)
