from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        removed_value = self._data[0]
        del self._data[0]
        return removed_value

    def search(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexError("ivalid index")
        return self._data[index]
