# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

string=raw_input()

string.replace("A","B")
string.replace("T","U")
string.replace("G","H")
string.replace("C","D")

string.replace("B","T")
string.replace("U","A")
string.replace("H","C")
string.replace("D","G")

# Extended slice syntax --> [begin:end:step]
print string[::-1]