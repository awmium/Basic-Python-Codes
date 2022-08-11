
# Install matplotlib before you import it
import matplotlib.pyplot as plt


list =[]
# Creating list with all collatz number
def collatz(n):
    while n > 1:
        list.append(n)
        if (n % 2):
            # n is odd
            n = 3*n + 1
        else:
            # n is even
            n = n//2
    list.append(1)
 
n = int(input('Enter n: '))
collatz(n)

# It'll print all Collatz number on the list
print(list)

# Plotting all Collatz Number
with plt.style.context('dark_background'):
    plt.plot(list)
    plt.savefig('test.png')
    plt.show()

