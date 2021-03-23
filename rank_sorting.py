import array	# importing to work with Arrays

def disp_sort(arr):
	# Function to display - formatted way
	for i in range(0,len(arr)):
		print(str(i+1), " - ", str(arr[i]))

def rank_sort(arr):
	# Function to sort
	if len(arr)==1:
		# If only 1 variable is available, its the best rank
		return
	else:
		# Bubble sort
		for i in range(0,len(arr)-1):
			for j in range(0,len(arr)-i-1):
				if(arr[j]>arr[j+1]):
					arr[j],arr[j+1]=arr[j+1],arr[j]

# Store ranks - array variable
arr=[]
# Temporary hold of variable
temp=0
# Max Ranks
max_=0
max_=int(input("enter the maximum players : "))
for i in range(0,max_):
	temp=int(input("enter rank : "))
	# Add to array
	arr.append(temp)
	# Calling Sort
	rank_sort(arr)
	# Calling Display
	disp_sort(arr)