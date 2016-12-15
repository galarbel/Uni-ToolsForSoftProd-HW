all: sort sort_sortedBug sort_overrunBug sort_permutaionBug

clean:
	-rm sort.o sort sort_sortedBug.o sort_sortedBug sort_overrunBug.o sort_overrunBug sort_permutaionBug.o sort_permutaionBug

sort: sort.o
	gcc  -o sort sort.o

sort.o: sort.c
	gcc -c -Wall -g sort.c

sort_sortedBug: sort_sortedBug.o
	gcc  -o sort_sortedBug sort_sortedBug.o
	
sort_sortedBug.o: sort_sortedBug.c
	gcc -c -Wall -g sort_sortedBug.c
	
sort_overrunBug: sort_overrunBug.o
	gcc  -o sort_overrunBug sort_overrunBug.o
	
sort_overrunBug.o: sort_overrunBug.c
	gcc -c -Wall -g sort_overrunBug.c
	
sort_permutaionBug: sort_permutaionBug.o
	gcc  -o sort_permutaionBug sort_permutaionBug.o
	
sort_permutaionBug.o: sort_permutaionBug.c
	gcc -c -Wall -g sort_permutaionBug.c
