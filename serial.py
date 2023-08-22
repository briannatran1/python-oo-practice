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
        """Create serial generator from start number"""
        self.start = start
        self.count = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start}>"

    def generate(self):
        """Generates next number in sequence"""
        self.count += 1
        return self.count - 1

    def reset(self):
        """Resets count back to start"""
        self.count = self.start
