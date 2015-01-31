# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

string=raw_input()

print string.count("A"),string.count("C"),string.count("G"),string.count("T")