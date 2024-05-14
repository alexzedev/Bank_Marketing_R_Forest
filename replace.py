import sys
import fileinput
 
x = input("Enter text to be replaced:")
y = input("Enter replacement text:")
 
for l in fileinput.input(files = "bank-full.txt"):
    l = l.replace(x, y)

    with open('bank1.txt', 'a') as f:
        f.write(l)