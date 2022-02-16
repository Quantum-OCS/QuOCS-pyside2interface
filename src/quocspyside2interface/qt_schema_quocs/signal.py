""" Put header here """


class Signal:
    def __init__(self):
        self.cache = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if instance not in self.cache:
            self.cache[instance] = BoundSignal()
        return self.cache[instance]


class BoundSignal:
    def __init__(self):
        self._subscribers = []

    def emit(self, *args):
        for sub in self._subscribers:
            sub(*args)

    def connect(self, listener):
        self._subscribers.append(listener)

    def disconnect(self):
        self._subscribers.pop(-1)
