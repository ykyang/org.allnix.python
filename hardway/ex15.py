import sys

filename = 'ex15_example.txt'

print(f"Here's your file {filename}")

text = open(filename)
print(text.read())