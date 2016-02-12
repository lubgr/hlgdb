
SRC = hlgdb.py 

all:

install: $(SRC)
	@install -D -m 644 $(SRC) /usr/local/share/gdb/$(SRC)

clean:
	@rm -f *.pyc

.PHONY:
	install clean
