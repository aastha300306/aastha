class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]  

    def __eq__(self, other):
        return self.date == other.date  

    def display(self):
        print(f"Date: {self.date[0]:02d}/{self.date[1]:02d}/{self.date[2]}")


date1 = Date(3, 4, 2025)
date2 = Date(3, 4, 2025)
date3 = Date(7, 4, 2025)

print("Date 1:", end=" ")
date1.display()

print("Date 2:", end=" ")
date2.display()

print("Date 3:", end=" ")
date3.display()

print("\nComparing Date 1 and Date 2:", "Equal" if date1 == date2 else "Not Equal")
print("Comparing Date 1 and Date 3:", "Equal" if date1 == date3 else "Not Equal")