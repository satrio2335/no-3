class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Order {item} added to the queue")

    def dequeue(self):
        if len(self.queue) > 0:
            order = self.queue.pop(0)
            print(f"Order {order} removed from the queue")
            return order
        else:
            print("The queue is empty")
            return None

# Example usage
q = Queue()
q.enqueue("Order 1")
q.enqueue("Order 2")
q.dequeue()
q.dequeue()
q.dequeue()
