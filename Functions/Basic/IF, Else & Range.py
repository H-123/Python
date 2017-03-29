# Write if, else-if and else statement
# Source, https://www.programiz.com/python-programming/if-elif-else
# Source, https://www.programiz.com/python-programming/examples/odd-even
# a%2 == 0, meaing can be divided by 2, an even number as result

# "Given an integer, , perform the following conditional actions:
# If a is odd, print Weird
# If a is even and in the inclusive range of 2 to 5, print Not Weird
# If a is even and in the inclusive range of 6 to 20, print Weird
# If a is even and greater than 20, print Not Weird


a = int(raw_input())

if a>=1 and a<=100:
    if a%2 == 0:
        if a in range (2, 6):
            print "Not Weird"
            
        if a in range (6, 21):
            print "Weird"
            
        if a>20:
            print "Not Weird"            
       
    else:
            print "Weird"   
