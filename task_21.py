# Given an array of non negative numbers each 
# number tells you the maximum number of steps you can jump
# for ward from that position, find minimum number of jumps needed
# to move from first to last position
arr = [1,2,3,4,5,6]
jump = 0
# for i in range(0,len(arr)-1):
#     i = i + arr[i]
#     for j in range(i,len(arr)):
#         jump = jump+1
i = 0
while(i==len(arr)):
        i = i + arr[i]
        jump = jump + 1
print()

    
