# python2
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeHeight:
	def read(self):
		self.n = int(sys.stdin.readline())
		self.parent = list(map(int, sys.stdin.readline().split()))

	def compute_height(self):
		heights = {}
		maxHeight = 0
		loopcount = 0
		for vertex in range(self.n):
			height = 0
			i = vertex
			while i != -1:
				height += 1
				loopcount += 1
				i = self.parent[i]
				# Check if parent is in dictionary, if so add that height to the height
				if i in heights:
					height += heights[i]
					i = -1
			maxHeight = max(maxHeight, height);
			heights[vertex] = height
		return maxHeight;

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
