__author__ = 'Syn'



class Dreamer_Arch:
    def __init__(self):
        self._sockets = {}

    def add_socket(self, descriptor):
        self._sockets[descriptor.id] = descriptor

    def rem_socket(self, descriptor):
        del self._sockets[descriptor.id]

    def sockets(self):
        return self._sockets
