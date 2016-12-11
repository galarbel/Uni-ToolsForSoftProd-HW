#include <stdio.h>

int main(int argc, char *argv[])
{
	int num_of_elements;
	int element;
	int *arr;
	
	if(argc != 1)
	{
		printf("The program doesn't support any arguments");
		return -1;
	}
	
	printf("please enter the number of elements you want to enter:");
	if(scanf("%d",&num_of_elements) != 1)
	{
		printf("Illegal input, please enter an integer.");
		return -1;
	}
	
	arr = malloc(sizeof(int)*num_of_elements);
	
	for(int i=0;i<num_of_elemnts;i++)
	{
		printf("please enter the element %d",i);
		if(scanf("%d",&element) != 1)
		{
			free(arr);
			return -1; 
		}
		a[i] = element;
	}
	
	//implement merge sort.
	
}

