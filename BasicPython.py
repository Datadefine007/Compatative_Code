# Fibonacci series
a = 0
b = 1
d = []
while a < 9:
    d.append(a)
    a, b = b, a + b
print(d)

# Multithreading example
import threading
import time

class Demo:
    def print_numbers(self):
        for i in range(5):
            time.sleep(1)
            print(f"Thread 1: {i}")

    def print_letters(self):
        for letter in 'ABCDE':
            time.sleep(1)
            print(f"Thread 2: {letter}")

# Create an instance of the class
demo_instance = Demo()

# Create two threads, passing the instance methods as targets
thread1 = threading.Thread(target=demo_instance.print_numbers)
thread2 = threading.Thread(target=demo_instance.print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")

# Class hierarchy and methods
class Demo:
    def run(self):
        print("Worker node is working")

    def execute(self):
        print("deepclone")

    def pull(self):
        print("Might not be available")

class Runtime(Demo):
    def env(self):
        print("Compiler by IDLE")

    def lan(self):
        print("Easy to use")

    def fact(self, x1):
        # Fix: Change 'x1' to 'x'
        x = [i for i in range(1, x1 + 1)]
        d = 1
        for i in x:
            d *= i
        return d

    def palindrome(self, x):
        # Fix: Change 'while' to 'if', and 'x==x[::-1]' to 'x == x[::-1]'
        if x == x[::-1]:
            print("palindrome")
        else:
            print("not palindrome")

# Create an instance of the class and call the palindrome method
task = Runtime()
task.palindrome("pop")

# Check for palindrome from user input
user_input = input("Enter a string: ")
if user_input == user_input[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# Sorting list in ascending order
a = [121, 2, 23, 2, 34, 3, 434, 54, 54, 534, 432, 4, 324324]
a.sort()
print("Sorted List:", a)

# Extracting elements less than 1000 and greater than or equal to 1000
a1 = [x for x in a if x < 1000]
a2 = [x for x in a if x >= 1000]
a1.append(5555)
print("Modified List:", a1 + a2)
