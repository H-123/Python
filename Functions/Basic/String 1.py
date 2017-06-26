#Task 
#Read a given string, change the character at a given index and then print the modified string.

#Input Format 
#The first line contains a string, S.
#The next line contains an integer i, denoting the index location and a character c separated by a space.

#Output Format 
#Using any of the methods explained above, replace the character at index i with character c.


s = list(raw_input())

index, letter = raw_input().split()
# what is the purpose of using split here?

s[int(index)] = letter


print("".join(s))
