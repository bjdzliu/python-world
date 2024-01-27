#!/usr/bin/python
def f(a,b):
    if a > b:
        smaller=b
    else:
        smaller=a

    for i in range(smaller):
        if a % (smaller-i) ==0 and b % (smaller-i)==0:
            return smaller -i

print(f(18,42))