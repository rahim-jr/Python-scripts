spam = 'Say hi to him, he\'s a good guy.' #single coat 
print(spam) 

spam = 'Say hi to him, he\t\'s a good guy.' #single Tab
print(spam)

# Multiline strings
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

"""
string index & slicing 
H   e   l   l   o   ,       w   o   r   l    d    !   
0   1   2   3   4   5   6   7   8   9   10   11   12
"""

spam = "Hello world!"

print(spam[0])

print(spam[6])

print(spam[-1])

print(spam[6:])

print(spam[::-1]) # Reverse string # [index : range : counter]

spam = '''There is a container in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob'''

print(spam.split("\n"))