# findThisInFile

https://dotesports.com/tft/news/tft-set-8-cheat-sheet-all-traits-and-stats

This site had all the champs and the traits

Instead of just manually looking through, I made a Python program to get it for me.

While you could argue this was a waste of time, this code could come in handy in the future!!!

## First Part
We want to only get champs from the file
Basically, looking for strings that contain "(". An example would be: A.D.M.I.N (2/4/6)


## Second Part
We want to only find champs and additionally search in our list we created for exceptions
We are looking for single word strings
Draven <- Notice how this is all we have!!
