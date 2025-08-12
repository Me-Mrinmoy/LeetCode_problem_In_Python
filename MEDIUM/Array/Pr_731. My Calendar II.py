class MyCalendarTwo:
    def __init__(self):
        self.bookings = []  # all booked intervals
        self.overlaps = []  # intervals with double bookings

    def book(self, start, end):
        # 1. Check if this booking would cause a triple booking
        for os, oe in self.overlaps:
            if start < oe and end > os:  # overlap exists
                return False

        # 2. Add new overlaps created with existing bookings
        for bs, be in self.bookings:
            if start < be and end > bs:  # overlap exists
                self.overlaps.append((max(start, bs), min(end, be)))

        # 3. Add the booking
        self.bookings.append((start, end))
        return True


# Example usage
if __name__ == "__main__":
    cal = MyCalendarTwo()
    print(cal.book(10, 20))  # True
    print(cal.book(50, 60))  # True
    print(cal.book(10, 40))  # True
    print(cal.book(5, 15))   # False
    print(cal.book(5, 10))   # True
    print(cal.book(25, 55))  # True
