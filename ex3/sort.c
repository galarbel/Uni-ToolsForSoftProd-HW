#include <stdio.h>
#include <stdlib.h>
#include <assert.h>


int checkPermutation1(int* a, int* b, int n)
{

	if(a==NULL && b==NULL)
	{ 
		return 1; 
	} 
	
	int mul1 = 1; 
	int mul2 = 1;
	int sum1 = 0;
	int sum2 = 0; 
	
	for(int i=0; i<n; i++)
	{ 
		mul1 *= a[i];
		mul2 *= b[i];
		sum1 += a[i];
		sum2 += b[i];
	} 
	
	if(mul1 == mul2 && sum1 == sum2)
	{
		return 1;
	}

	else 
	{
		return 0;
	}
	
	return -1;
}


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
	int *org_arr;
	int *arr;
	
	if(argc != 1)
	{
		printf("The program doesn't support any arguments");
		return -1;
	}
	
	printf("please enter the number of elements you want to enter:");
	//Get the number of elements.
	if(scanf("%d",&num_of_elements) != 1)
	{
		printf("Illegal input, please enter an integer.");
		return -1;
	}
	
	assert(checkBufferOverrun(num_of_elements)==1);
	
	org_arr = malloc(sizeof(int)*num_of_elements);
	// Get elements from the user
	for(int i=0;i<num_of_elements;i++)
	{
		printf("please enter the element %d: ",i);
		if(scanf("%d",&element) != 1)
		{
			free(org_arr);
			return -1; 
		}
		assert(checkBufferOverrun(i) == 1);
		org_arr[i] = element;
	}
	
	// Copy the original array.
	arr = malloc(sizeof(int)*num_of_elements);
	for(int i=0; i< num_of_elements;++i)
	{
		assert(checkBufferOverrun(i) == 1);
		arr[i] = org_arr[i];
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
	assert(checkPermutation1(arr, org_arr, num_of_elements) == 1);
	free(arr);
	free(org_arr);
	
	return 1;
	
}

