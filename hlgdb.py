
import re
from pygments import highlight
from pygments.lexers import CppLexer, TextLexer
from pygments.formatters import Terminal256Formatter
from pygments.styles import get_style_by_name

def highlightLines(listOutput, doEmphCurrentLine = False):
    lp = LinePrinter(doEmphCurrentLine)
    for line in listOutput.splitlines():
        lp.highlightLine(line)

class LinePrinter(object):
    def __init__(self, doEmphCurrentLine = False):
        self.lexer = self.getLexer()
        self.style = get_style_by_name('default')
        self.formatter = Terminal256Formatter(style = self.style, bg = 'dark')
        self.lineNumber = self.getLineNumber(doEmphCurrentLine)

    def getLexer(self):
        languageStr = gdb.execute('show language', False, True)

        if languageStr.find('c++') != -1:
            return CppLexer()
        else:
            return TextLexer()

    def getLineNumber(self, doEmphCurrentLine):
        if not doEmphCurrentLine:
            return 0

        try:
            frameStr = gdb.execute('where', True, True)
            frameStr = frameStr.splitlines()[0]
        except:
            return 0
        try:
            nStr = re.search('[0-9]+$', frameStr).group(0)
            return int(nStr)
        except:
            return 0


    def highlightLine(self, line):
        number, code = self.splitListOutput(line)

        if number == 0:
            print(line)
            return

        numberStr = self.getNumberString(number)
        hlStr = highlight(code, self.lexer, self.formatter)[:-1]
        print(numberStr + '\t' + hlStr)

    def splitListOutput(self, line):
        numberMatch = re.match(r'^ *([0-9]+)\t(.*)', line)

        try:
            number = numberMatch.group(1)
            code = numberMatch.group(2)
            return int(number), code
        except:
            return 0, line

    def getNumberString(self, number):
        if number == 0:
            return ''
        elif number == self.lineNumber:
            return '\033[01;33m' + str(number) + ' ->\033[0m'
        else:
            return str(number)


class ColorList(gdb.Command):
    """Do the same as the standard 'list' command, but colorize the output."""

    def __init__(self):
        gdb.Command.__init__(self, 'l', gdb.COMMAND_FILES, gdb.COMPLETE_FILENAME, False)

    def invoke(self, arg, from_tty):
        try:
            output = gdb.execute('list ' + arg, False, True)
            highlightLines(output, True)
        except gdb.error as error:
            print(error)


class ColorNext(gdb.Command):
    """Do the same as the standard 'next' command, but colorize the output."""

    def __init__(self):
        gdb.Command.__init__(self, 'n', gdb.COMMAND_USER, gdb.COMPLETE_NONE, True)

    def invoke(self, arg, from_tty):
        try:
            output = gdb.execute('next ' + arg, False, True)
            highlightLines(output)
        except gdb.error as error:
            print(error)

class ColorStep(gdb.Command):
    """Do the same as the standard 'step' command, but colorize the output."""

    def __init__(self):
        gdb.Command.__init__(self, 's', gdb.COMMAND_USER, gdb.COMPLETE_NONE, True)

    def invoke(self, arg, from_tty):
        try:
            output = gdb.execute('step ' + arg, False, True)
            highlightLines(output)
        except gdb.error as error:
            print(error)

ColorList()
ColorNext()
ColorStep()
