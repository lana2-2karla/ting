from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
         self._data.append(value)    

    def dequeue(self):
        return self._data.popleft()

    def search(self, index):
        if index < 0:
            raise IndexError('invalid index')
        return self._data[index]

# ref: https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/