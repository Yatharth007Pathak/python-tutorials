# Creating a progress bar using python

import time
from tqdm import tqdm
for i in tqdm (range(100)):
    time.sleep(1)


'''
This code runs a loop 100 times, and during each iteration, it pauses for 1 second. A progress bar shows the current progress as the loop runs.


Here's a line-by-line breakdown of your code:

import time
Purpose: Imports the time module from Python's standard library, which provides various time-related functions.
Why it's needed: The time.sleep() function, used later, pauses the execution for a given number of seconds.

from tqdm import tqdm
Purpose: Imports the tqdm function from the tqdm module. tqdm is a library that displays progress bars for loops.
Why it's needed: It helps visualize the progress of loops in a simple, readable format by showing the progress bar.

for i in tqdm(range(100)):
Purpose: Starts a loop that iterates 100 times. The tqdm(range(100)) wraps the range(100) iterator, which generates numbers from 0 to 99. 
The tqdm() function visually shows a progress bar during the loop's execution.
Why it's needed: The loop controls the iterations, while tqdm provides feedback on how much of the loop has been completed.

time.sleep(1)
Purpose: Pauses the execution of the program for 1 second in each iteration of the loop.
Why it's needed: Simulates some processing time, creating a delay of 1 second between each iteration. 
It also helps the progress bar to advance gradually and visibly.
'''


'''
tqdm is a Python library that provides a fast, extensible progress bar for loops and iterable objects. 
Its main purpose is to make tracking the progress of time-consuming operations (like loops) easier to visualize.

Here are some key points about tqdm:
Progress Bars: It adds a progress bar around loops or other iterable objects, so you can see how far the operation has progressed.
Ease of Use: tqdm is very simple to integrate with existing code. You only need to wrap your loop or iterable with tqdm().
Real-Time Feedback: It shows real-time information such as the current progress, 
time elapsed, estimated time remaining, and the speed of iterations.
Flexible: Works with any iterable, including Python lists, ranges, and file objects.
Lightweight: The overhead of using tqdm is very low, meaning it doesn't significantly slow down your program.
'''