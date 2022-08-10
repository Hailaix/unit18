"""Python serial number generator."""

from locale import currency


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
        self.curr = start
    def generate(self):
        """Returns the next number in the sequence"""
        current = self.curr
        self.curr += 1
        return current
    def reset(self):
        """Resets the serial to the original number"""
        self.curr = self.start


