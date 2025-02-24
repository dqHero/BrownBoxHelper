# BrownBoxHelper
This program gives you the best possible next guess and makes it easy to "guess" the combination using binary search.

Run the program by running the following in your prompt:
python BrownBoxHelper

The window will stay on top of all other windows including your game. It can be minimized. 

How to use:
Start by entering the first number it recommends (54), then click 'lesser' or 'greater' button depending on the in game feedback in the chat log.
A new number will be suggested. Continue until you open the box then select the 'correct' button to clear the previous numbers and start over.

How it works:
Binary search is an efficient algorithm that finds a target value within a sorted array by repeatedly dividing the search space in half, comparing the target value to the middle element, and then eliminating either the lower or upper half based on whether the target is greater or less than the middle element, until the target is found or the search space is exhausted; essentially, it works by "guessing" closer and closer to the correct answer with each iteration.
