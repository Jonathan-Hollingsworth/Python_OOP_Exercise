"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        self.next = start
    
    def __repr__(self) -> str:
        return f"SerialGenerator(start={self.start} next={self.next})"
    
    def generate(self):
        "Generates the next number"
        num = self.next
        self.next += 1
        return num
    
    def reset(self):
        "Resets the generator to its starting value"
        self.next = self.start

