class String:
    def __init__(self, value=""):
        self.value = value

    def __iadd__(self, other):
        """Overload += operator for string concatenation."""
        if isinstance(other, String):
            self.value += other.value
        elif isinstance(other, str):
            self.value += other
        else:
            raise TypeError("Can only concatenate with String or str types.")
        return self

    def toLower(self):
        """Convert all uppercase letters to lowercase."""
        self.value = self.value.lower()

    def toUpper(self):
        """Convert all lowercase letters to uppercase."""
        self.value = self.value.upper()

    def display(self):
        print(self.value)


s1 = String("Hell")
s2 = String("ooo!!")

print("Original Strings:")
s1.display()
s2.display()

s1 += s2
print("\nAfter Concatenation (s1 += s2):")
s1.display()

s1.toUpper()
print("\nAfter toUpper():")
s1.display()

s1.toLower()
print("\nAfter toLower():")
s1.display()