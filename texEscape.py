# Reprints the input file as lateX-friendly input
import sys
import re

conv = {
    '&': r'\&',
    '%': r'\%',
    '$': r'\$',
    '#': r'\#',
    '_': r'\_',
    '{': r'\{',
    '}': r'\}',
    '~': r'\textasciitilde{}',
    '^': r'\^{}',
    '\\': r'\textbackslash{}',
    '<': r'\textless',
    '>': r'\textgreater',
    '\n': r'\\'
}
regex = re.compile('|'.join(re.escape(key) for key in sorted(conv.keys(), key = lambda item: - len(item))))


def texEscape(text):
    """
        :param text: a plain text message
        :return: the message escaped to appear correctly in LaTeX
    """
    return regex.sub(lambda match: conv[match.group()], text)

with open(sys.argv[1]) as file:
    for line in file:
        print(texEscape(line).rstrip())
