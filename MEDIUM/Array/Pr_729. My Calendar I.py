class MyCalendar:
    def __init__(self):
        self.bookings = []  # list of (start, end) tuples

    def book(self, start, end):
        for s, e in self.bookings:
            # overlap exists unless end <= s or start >= e
            if not (end <= s or start >= e):
                return False
        self.bookings.append((start, end))
        return True

# quick test
if __name__ == "__main__":
    cal = MyCalendar()
    print(cal.book(10, 20))  # True
    print(cal.book(15, 25))  # False
    print(cal.book(20, 30))  # True
