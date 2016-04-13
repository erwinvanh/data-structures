# python2

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(raw_input())
    self._data = [int(s) for s in raw_input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print len(self._swaps)
    for swap in self._swaps:
      print swap[0], swap[1]

  def LeftChild(self, i):
      return 2 * i

  def RightChild(self, i):
      return 2 * i + 1

  def SiftDown(self, i):
# Correct for zero-based indexing.
# Indexes are 0 through len - 1
# elements are 1 through len
# children of element 2 (is index 1) are elements 4 (index 3) and 5 (index 4)
      maxIndex = i
      leftChild = self.LeftChild(i)
      rightChild = self.RightChild(i)

      if leftChild <= len(self._data):
          if self._data[leftChild - 1] < self._data[maxIndex - 1]:
              maxIndex = leftChild

      if rightChild <= len(self._data):
          if self._data[rightChild - 1] < self._data[maxIndex - 1]:
              maxIndex = rightChild

      if maxIndex != i:
          self._swaps.append((i - 1, maxIndex - 1))
          self._data[i - 1], self._data[maxIndex - 1] = self._data[maxIndex - 1], self._data[i - 1]
          self.SiftDown(maxIndex)

  def GenerateSwaps(self):
      
    for i in range( len(self._data) / 2, 0, -1 ):
        self.SiftDown(i)

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
