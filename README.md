# Python_OOP_Exercise

## wordfinder.py

wordfinder.py contains two classes with doctests for each

### WordFinder

- Word Finder: finds random words from a dictionary.  
- wf = WordFinder("words.txt")  
- word = wf.random()  

### SpecialWordFinder

- A Subclass of WordFinder that ignores blank lines and comments  
- wf = SpecialWordFinder("words.txt")  
- word = wf.random()  

## serial.py

Python serial number generator

### SerialGenerator

- Machine to create unique incrementing serial numbers  
- serial = SerialGenerator(start=100)  
- serial.generate() (100)
- serial.generate() (101)
_ serial.generate() (102)
- serial.reset()
- serial.generate() (100)
