# Chris Nassour, Python Stats Script, Works on Python 3
import math

def average( mylist ):
    return sum(mylist)/len(mylist)
    
def variance( mylist ):
    sum = 0
    for i in mylist:
        sum += (i - average(mylist))**2
    return sum / len(mylist)

num_list = []
num_list.append(int(input("Enter a + number: ")))

while (num_list[-1] > 0):
    num_list.append(int(input("Enter a + number: ")))
    
num_list.pop()      #remove the pesky terminating number
print(num_list)
print("Average is ", average(num_list))
print("Variance is ", variance(num_list)) 
print("Standard Deviation is ", math.sqrt(variance(num_list)))
