#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
 
void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
 
void bubbleSort(int arr[], int n){
   int swapped;
   int i, j;

   for (i = 0; i < n-1; i++){
     swapped = 0;
     for (j = 0; j < n-i-1; j++){
        if (arr[j] > arr[j+1]){
           swap(&arr[j], &arr[j+1]);
           swapped = 1;
        }
     }
 
     // IF no two elements were swapped by inner loop, then break
     if (swapped == 0)
        break;
   }
}

// A function to generate a random permutation of arr[]
void randomSort( int arr[], int n )
{
    // Use a different seed value so that we don't get same
    // result each time we run this program
    srand ( time(NULL) );
 
    // Start from the last element and swap one by one. We don't
    // need to run for the first element that's why i > 0
    for (int i = n-1; i > 0; i--)
    {
        // Pick a random index from 0 to i
        int j = rand() % (i+1);
 
        // Swap arr[i] with the element at random index
        swap(&arr[i], &arr[j]);
    }
}


int isSorted(int a[], int n) {
  int i;
  /* descending order */
  for (i=1;i<n;++i) {
    if (a[i]<a[i-1]) {
      break;
    }
  }
  
  if ( i < n ) { /* failed descending order */
    for (i=1;i<n;++i) {  /* ascending order? */
       if (a[i]>a[i-1]) {
          break;
       }
    }
	if ( i < n ) {
		//Array is not sorted
		return 0;
	}
	else {
		 //Array is sorted (descending)
		 return 1;
	}
  }
   else {
	//Array is sorted (ascending)
	return 1;
	}
}

void sort(int a[], int n){
	int i=0;

	while(!isSorted(a,n)){
		if(i <= 100){
			randomSort(a,n);
		}
		else{
			bubbleSort(a,n);
			assert(isSorted);
		}
		i++;
	}
	
}

/* Function to print an array */
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}
 
// For testing above functions
int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90 ,57 ,1 ,44 ,98 ,100 , 16 ,88 ,102};
    int n = sizeof(arr)/sizeof(arr[0]);
    //bubbleSort(arr, n);
	//randomSort(arr,n);
	sort(arr,n);
    printf("Sorted array: \n");
    printArray(arr, n);
    return 0;
}
