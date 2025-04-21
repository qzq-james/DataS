from Array_static import ArrSeq


class DArraySeq(ArrSeq):
    def __init__(self, r=2):
        super().__init__()
        self.size = 0
        self.r = r      # resize arr two times bigger
        self._rsize(0)

    def __len__(self): return self.size

    def __iter__(self):
        for i in range(len(self)):
            yield self.A[i]

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def _compute_bound(self):       # bound for judging allocate is needed
        self.upper = len(self.A)
        self.lower = len(self.A) // (self.r * self.r)

    def _rsize(self, n):
        if self.lower < n < self.upper:
            return
        m = max(1, n) * self.r
        A = [None] * m
        self._copy_from_forward(self.size, 0, 0, A)
        self.A = A
        self._compute_bound()

    def insert_last(self, x):
        self._rsize(self.size + 1)
        self.A[self.size] = x
        self.size += 1

    def delete_last(self):
        self.A[self.size - 1] = None
        self.size -= 1
        self._rsize(self.size)

    def insert_at(self, i, x):
        self.insert_last(None)
        self._copy_from_forward(self.size - (i + 1), i, i + 1, self.A)
        self.A[i] = x

    def delete_at(self, i):
        x = self.A[i]
        self._copy_from_forward(self.size - (i + 1), i + 1, i, self.A)
        self.delete_last()
        return x

    def insert_first(self, x): self.insert_at(0, x)
    def delete_first(self): return self.delete_at(0)
