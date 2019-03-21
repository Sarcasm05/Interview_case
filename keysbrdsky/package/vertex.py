from collections import namedtuple


class Vertex(namedtuple('Vertex', 'start, end, cost')):
    __slots__ = ()

    def __new__(cls, start, end, cost):
        self = super(Vertex, cls).__new__(cls, hash(start), hash(end), cost)
        self._hash = hash(self.start) * hash(self.end)
        return self


    def __hash__(self):
        return self._hash

    @property
    def distance(self):
        return self.end - self.start

    def __str__(self):
        return 'from %s to %s distance of = %d' % (self.start, self.end, self.distance)
