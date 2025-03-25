import sys
import math
from functools import cmp_to_key

# Point class with added validations and slope comparison
class Point:
    def __init__(self, x, y):
        if x < 0 or y < 0:
            raise ValueError("Coordinates must be non-negative")
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if other is None or not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if self.y < other.y or (self.y == other.y and self.x < other.x):
            return True
        return False

    def slope_to(self, that):
        if self == that:
            return float('-inf')  # degenerate line segment
        if self.x == that.x:
            return float('inf')   # vertical line
        if self.y == that.y:
            return 0.0            # horizontal line
        return (that.y - self.y) / (that.x - self.x)

    def slope_order(self):
        def compare(p1, p2):
            slope1 = self.slope_to(p1)
            slope2 = self.slope_to(p2)
            if math.isclose(slope1, slope2, rel_tol=1e-9):
                return 0
            return -1 if slope1 < slope2 else 1
        return compare


# LineSegment class to represent a line segment between two points
class LineSegment:
    def __init__(self, p, q):
        if p is None or q is None:
            raise ValueError("Argument to LineSegment constructor is None")
        if p == q:
            raise ValueError(f"Both endpoints are the same point: {p}")
        self.p = p
        self.q = q

    def __str__(self):
        return f"{self.p} -> {self.q}"

    def __repr__(self):
        return str(self)


# FastCollinearPoints class to detect collinear points and segments
class FastCollinearPoints:
    def __init__(self, points):
        if points is None:
            raise ValueError("Argument is None")
        # Defensive copy of the list
        self.points = list(points)
        n = len(self.points)
        for p in self.points:
            if p is None:
                raise ValueError("Null point found")

        # Sort points to detect duplicates
        self.points.sort()
        for i in range(1, n):
            if self.points[i] == self.points[i-1]:
                raise ValueError("Duplicate points detected")

        self.segments_list = []
        self._find_segments()

    def _find_segments(self):
        n = len(self.points)
        for i in range(n):
            origin = self.points[i]
            # Create list of remaining points
            others = self.points[:i] + self.points[i+1:]
            # Sort others based on slope order from origin.
            comparator = origin.slope_order()
            others.sort(key=cmp_to_key(comparator))

            j = 0
            while j < len(others):
                collinear = []
                slope_ref = origin.slope_to(others[j])
                # Group together points with the same slope relative to origin.
                while j < len(others) and math.isclose(origin.slope_to(others[j]), slope_ref, rel_tol=1e-9):
                    collinear.append(others[j])
                    j += 1

                # Check if there are at least 3 points with the same slope (4 including origin)
                if len(collinear) >= 3:
                    candidate = [origin] + collinear
                    candidate.sort()
                    # To avoid duplicates, only add segment if origin is the smallest point.
                    if origin == candidate[0]:
                        seg = LineSegment(candidate[0], candidate[-1])
                        self.segments_list.append(seg)

    def number_of_segments(self):
        return len(self.segments_list)

    def segments(self):
        return list(self.segments_list)


# Main function for input parsing and processing
def main():
    try:
        # Read from standard input.
        line = sys.stdin.readline()
        if not line:
            raise ValueError("No input provided")
        n = int(line.strip())
        points = []
        for _ in range(n):
            line = sys.stdin.readline().strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 2:
                raise ValueError("Each point must have exactly two integers")
            x, y = int(parts[0]), int(parts[1])
            points.append(Point(x, y))

        # Find collinear segments
        collinear = FastCollinearPoints(points)
        segments = collinear.segments()

        # Print the results
        if not segments:
            print("No collinear points")
        else:
            for seg in segments:
                print(seg)

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
