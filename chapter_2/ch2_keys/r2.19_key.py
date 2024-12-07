"""When using the ArithmeticProgression class of Section 2.4.2 with an increment of 128 and a start of 0, how many calls to next can we make before we reach an integer of 2^(63) or larger?"""

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

class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment
    def advance(self):
        self._current += self._increment


prog = ArithmeticProgression(increment=128, start=0)


# answer@step = current_value + increment * step
# refactor and sub in your values, start (current), increment, answer@step to solve for step

step = (2**63) // 128

print(step)

# step = 72057594037927936



