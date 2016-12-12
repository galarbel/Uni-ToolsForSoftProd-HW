all: sort

clean:
	-rm sort.o sort

sort: sort.o
	gcc  -o sort sort.o

sort.o: sort.c
	gcc -c -Wall -g sort.c


