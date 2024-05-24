from itertools import combinations 

# eratosthenes

l=[1]*3000
for i in range(2, 60):
    if l[i]:
        for j in range(i*2, 3000, i):
            l[j]=0
def solution(nums):
    count=0
    for i in list(combinations(nums, 3)):
        if l[i[0]+i[1]+i[2]]:
            count+=1
            print(i) 
    return count
print(solution([1,2,7,6,4])) 

# result: 4
