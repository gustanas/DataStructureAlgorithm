class Heap(object):

	def __init__(self):
		self.buffer = []
	
	def printHeap(self):
		print self.buffer

	def insert(self, value):
		self.buffer.append(value)
		self.bubble_up(len(self.buffer) - 1)

	def bubble_up(self, index):
		if index <= 0:
			return
		parent = index/2
		if self.buffer[index] <= self.buffer[parent]:
			self.buffer[index], self.buffer[parent] = self.buffer[parent], self.buffer[index]
			self.bubble_up(parent)
		return

	def extract_min(self):
		if len(self.buffer) <= 0:
			return None
		min_value =  self.buffer[0]
		last = self.buffer.pop()
		if len(self.buffer) > 0:
			self.buffer[0] = last
			self.heapify(0)
		return min_value

	def heapify(self, index):
		if index < 0 or index >= len(self.buffer):
			return
		
		min_index = index
		for i in range(2):
			child_index = index * 2 + i
			if child_index >= len(self.buffer):
				break
			if self.buffer[child_index] <= self.buffer[min_index]:
				min_index =  child_index

		
		if min_index != index:
			self.buffer[index], self.buffer[min_index] = self.buffer[min_index], self.buffer[index]
			self.heapify(min_index)

	
