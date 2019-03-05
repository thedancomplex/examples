default: all

CFLAGS := -I./include -g --std=gnu99
CC := gcc

BINARIES := udp-receiver
all : $(BINARIES)

LIBS := -lrt #-lach 

udp-receiver: src/udp-receiver.o
	gcc -o $@ $< $(LIBS)

%.o: %.c
	$(CC) $(CFLAGS) -o $@ -c $<

clean:
	rm -f $(BINARIES) src/*.o
