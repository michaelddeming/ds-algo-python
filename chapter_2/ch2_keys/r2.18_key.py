"""Give a short fragment of Python code that uses the progression classes
from Section 2.4.2 to find the 8th value of a Fibonacci progression that
starts with 2 and 2 as its first two values."""


class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        """Advance to the next value (overridden by subclasses)."""
        self._current += 1

    def __next__(self):
        """Return the next element, or raise StopIteration."""
        if self._current is None:  # Convention to signal the end of progression
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """Return the iterator itself."""
        return self

    def print_progression(self, n):
        """Print the next n values of the progression."""
        print(' '.join(str(next(self)) for _ in range(n)))


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        """Create a Fibonacci progression."""
        super().__init__(first)  # Start progression at first
        self._prev = second - first  # Implicitly set up the "previous" value

    def _advance(self):
        """Advance to the next value in the Fibonacci sequence."""
        self._prev, self._current = self._current, self._prev + self._current



prog = FibonacciProgression(first=2,second=2)

prog.print_progression(8)

# 42 is the 8th value