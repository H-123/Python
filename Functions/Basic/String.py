# Code here is the answer, please help me understnad the math logic of using range and the if
# Enter 2 sets of info, any spacing of the input info will be removed. 
# A is ABCDCDC
# x is CDC
A = raw_input().strip()
x = raw_input().strip()

# The range is length of A (7) minus length of x (3), then add 1. So i in range is 5 (0,1,2,3,4)
count = 0
for i in range(len(A) - len(x) + 1):
    
# if in A input
    if A[i:i+len(x)] == x:
        count += 1
print count
