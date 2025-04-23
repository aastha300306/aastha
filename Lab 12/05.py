class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        """Normalize time so that seconds and minutes are within 0-59"""
        self.minutes += self.seconds // 60
        self.seconds %= 60
        self.hours += self.minutes // 60
        self.minutes %= 60

    def display(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def from_seconds(self, total_seconds):
        self.hours = total_seconds // 3600
        total_seconds %= 3600
        self.minutes = total_seconds // 60
        self.seconds = total_seconds % 60

    def add(self, other):
        total_seconds = self.to_seconds() + other.to_seconds()
        result = Time()
        result.from_seconds(total_seconds)
        return result

    def subtract(self, other):
        total_seconds = abs(self.to_seconds() - other.to_seconds())
        result = Time()
        result.from_seconds(total_seconds)
        return result

time1 = Time(2, 45, 50)
time2 = Time(1, 20, 30)

print("Time 1:", end=" ")
time1.display()
print("Time 2:", end=" ")
time2.display()

added_time = time1.add(time2)
print("Added Time:", end=" ")
added_time.display()

subtracted_time = time1.subtract(time2)
print("Subtracted Time:", end=" ")
subtracted_time.display()