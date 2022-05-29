nums=[3,4,2,3]
c=0
i=0
while i<len(nums)-1:
    if nums[i]<=nums[i+1]:
        c+=1
    else:
        c=0  
    i+=1
if c==len(nums):
    print(True)
if c!=len(nums) and c>0:
    print(True)
if c==0:
    print(False)

print(c)