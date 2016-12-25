Highlight source code in GDB
============================

Syntax highlighting for gdb with a python extension that uses
[pygments](http://http://pygments.org/). This affects the commands `list`, `next` and `step` and is
achieved by overriding their shortcuts `l`, `n` and `s` (thus, the default behavior is retained by
invoking the full command).

**Requirements**

* the [pygments](http://http://pygments.org/) package for python
* gdb version 7.6\* or higher

**Installation**

Simple as that:

* download the script and store it where you like
* invoke it from your .gdbinit via `source path/to/the/script`

**Languages**

Currently, only C++ is supported, but it's easy to add new languages by modifying the script. Check
out lexer types supported by pygments [here](http://pygments.org/docs/lexers/).

**Color scheme**

The color scheme is adjustable, see the [pygments docs](http://pygments.org/docs/styles/) on the
choice of styles or the creation of custom schemes.
