from functions import square
for i in range(10):
    print(f"The square of {i} is {square(i)}")
    #running this function ny itself will results in an Exception:
    #Traceback (most recent call last):
    #File "D:\Desktop\EDX Courses\EDXnotes\squares.py", line 2, in <module>
    #print(f"The square of {i} is {square(i)}")
    #NameError: name 'square' is not defined