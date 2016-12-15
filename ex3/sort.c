#include <stdio.h>
#include <stdlib.h>
#include <assert.h>




int checkIfSorted(int *arr, int num_of_elements)
{
	int i;
	for(i=1; i<num_of_elements; i++)
	{
		if(num_of_elements > 1)
		{
			if(arr[i] < arr[i-1])
			{
				return 0;
			}
		}
	}
	return 1;
}


int checkBufferOverrun(int num_of_elements)
{
	if(num_of_elements > 99 || num_of_elements < 0)
	{
		return 0;
	}
	else
	{
		return 1;
	}
}




int main(int argc, char *argv[])
{
	int num_of_elements;
	int element,tmp;
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
	
	assert(checkBufferOverrun(num_of_elements)==1);

	arr = malloc(sizeof(int)*num_of_elements);
	
	for(int i=0;i<num_of_elements;i++)
	{
		printf("please enter the element %d: ",i);
		if(scanf("%d",&element) != 1)
		{
			free(arr);
			return -1; 
		}
		assert(checkBufferOverrun(i) == 1);
		arr[i] = element;
	}
	
	 for (int i = 0; i < num_of_elements - 1; ++i)
	 {
		  for (int j = 0; j < num_of_elements - 1 - i; ++j )
		  {
			   if (arr[j] > arr[j+1])
			   {
				   assert(checkBufferOverrun(i) == 1);
				   assert(checkBufferOverrun(j) == 1);
					tmp = arr[j+1];
					arr[j+1] = arr[j];
					arr[j] = tmp;
			   }
		  }
	 }
	
	printf("\nThe array sorted.\n");
	for(int i=0; i< num_of_elements;++i)
	{
		assert(checkBufferOverrun(i) == 1);
		printf("%d ",arr[i]);
	}
	printf("\n");
	assert(checkIfSorted(arr, num_of_elements) == 1);
	free(arr);
	
	return 1;
	
}

