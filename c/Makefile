default: all

CFLAGS := -I./include -g --std=gnu99
CC := gcc

BINARIES := example
all : $(BINARIES)

LIBS := -lrt #-lach 

example: src/example.o
	$(CC) -o $@ $< $(LIBS)

%.o: %.c
	$(CC) $(CFLAGS) -o $@ -c $<

clean:
	rm -f $(BINARIES) src/*.o
