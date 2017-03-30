"""Task 
Read an integer N. For all non-negative integers i< N , print i^2 . See the sample for details.

Input Format

The first and only line contains the integer, N.

Constraints
1<= N <=20

Output Format

Print N lines, one corresponding to each i."""

#Solution Below

n = int(raw_input())

"""i in range (0,n), means when input for of n is 5, 
output of i in range is 0,1,2,3,4. (Starts with 0, stops at 4, count 5 digits)"""

for i in range (0,n):

# since output of i is 0,1,2,3,4. Th print of i is 0*0,1*1,2*2,3*3,4*4    
    print i*i


