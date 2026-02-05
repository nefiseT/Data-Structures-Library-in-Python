"""Queue implementation using array (circular buffer)

FIFO: First In First Out
"""

class QueueArray:
	def __init__(self, capacity=5):
		self.capacity = capacity
		self.queuee = [None] * capacity
		self.front = 0 
		self.rear = 0
		self.size = 0

	def enqueue(self, value):
		if self.size == self.capacity:
			raise IndexError("queue is full")
		self.queue[self.rear] = value
		self.rear = (self.rear + 1) % self.capacity
		self.size -= 1
		return value

	def dequeue(self):
		if self.is_empty():
			raise IndexError(" queue is empty")
		value = self.queue[self.front)
		self.front = (self.front + 1) % self.capacity
		self.size -= 1
		return value

	def is_empty(self):
		return self.size == 0

if __name__ == "__main__":
	q = QueueArray()
	q.enqueue(10)
	q.enqueue(26)
	print(q.dequeue())