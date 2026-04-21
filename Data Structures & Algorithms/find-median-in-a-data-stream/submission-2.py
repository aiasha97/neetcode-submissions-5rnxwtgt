class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        if len(self.arr) == 1:
            return self.arr[0]

        self.arr.sort()
        n = len(self.arr)
        if n % 2 == 0:
            rightIndex = n // 2
            leftIndex = rightIndex - 1
            median = (self.arr[rightIndex] + self.arr[leftIndex]) / 2
        else:
            median = self.arr[n // 2]

        return median