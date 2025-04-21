class ArrSeq:
    def __init__(self):
        self.A = []
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        yield from self.A

    def build(self, X):
        self.A = [a for a in X]
        self.size = len(self.A)

    def get_at(self, i):
        return self.A[i]

    def set_at(self, i, x):
        self.A[i] = x

    def _copy_from_forward(self, n, i, j, A):
        for k in range(n):
            A[j + k] = self.A[i + k]    # i, j is where self.A, A started

    def _copy_from_backward(self, n, i, j, A):
        for k in range(n-1, -1, -1):
            A[j + k] = self.A[i + k]    # i, j is where self.A, A started

    def insert_at(self, i, x):
        n = len(self)           # resize
        A = [None] * (n+1)
        self._copy_from_forward(i, 0, 0, A)
        A[i] = x
        self._copy_from_forward(n - i, i, i+1, A)

    def delete_at(self, i):
        n = len(self)
        A = [None] * (n + 1)       # resize
        self._copy_from_forward(i, 0, 0, A)
        self._copy_from_forward(n - i - 1, i+1, i, A)

    def insert_first(self, x):  self.insert_at(0, x)
    def insert_last(self, x):  self.insert_at(len(self), x)
    def delete_first(self):  self.delete_at(0)
    def delete_last(self):  self.delete_at(len(self) - 1)


