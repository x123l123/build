class Queue:
    def __init__(self):
        self.queue = []
    def queueadd(self, item):
        self.queue.append(item)
    def isEmpty(self):
        return self.queue == []
    def queuedel(self):
        if self.isEmpty():
            return None
        else:
            return self.queue.pop(0)
    def print_queue(self):
        print(self.queue)

queue=Queue()
queue.queueadd(1)
queue.queueadd(2)
queue.queueadd(3)
queue.queueadd(4)
queue.queuedel()
queue.print_queue()