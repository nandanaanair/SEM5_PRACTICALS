from math import *
import sys

x={} # to store which queen is stored at in which column
n=int(4) # number of queens and rows
#function to clear the blocks 
def clear_future_blocks(k):
    for i in range(k,n+1):
        x[i]=None

def place(k,i):
    if(i in x.values()):
        return False
    j=1
    while(j<k):
        if abs(x[j]-i)==abs(j-k):
           return False
        j+=1
    return True

def Nqueens(k):
    for i in range(1,n+1):
        clear_future_blocks(k)
        if place(k,i):
            x[k]=i
            #print(i)
            #print(n)
            if k == n:
                for j in x:
                    print(x[j],end='')
                print()
                print('_________')
            else:
                Nqueens(k+1)

Nqueens(1)
        
