# TASK-11,12 
# print('task11')
# l=[]
# n=int(input("enter number of numbers in array"))

# for i in range(n):
#     l.append(int(input('enter the no.')))

# print(l.pop(2))
# print(len(l))
# print(l.reverse())


# TASK-13
# Print max and mini of an array using built in function
# l = [2, 4, 5, 7, 8, 9]
# print(min(l))
# print(max(l))


# TASK-14
# Reverse the given array without using built in function
# arr=[1,2,3,4,5,6]
# n=len(arr)
# i1=0;i2=len(arr)-1
# for i in range (int(n/2)):
#     arr[i1],arr[i2]=arr[i2],arr[i1]
#     i1+=1;i2-=1

# print(arr)

# TASK-15
#Print maximum and minimum of one array without using built in function
# arr=[23,43,12,56,92,1]
# max=arr[0]
# min=arr[0]
# for i in arr:
#     if i<min:
#         min=i
#     elif i>max:
#         max=i
# print('Maximum=',max,'\nMinimum=',min) 

#hw 1. find the kth smallest element of an array 2. find the largest element of an array without using built in function 3. find the union of two given arrays.

#hw1
arr=[52,3,4,55,13,17]
arr.sort()
k=int(input('enter the kth element'))
print(arr[k])