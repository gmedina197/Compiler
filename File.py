class File:
    def __init__(self, path="example.txt"):
        self.path = path
        self.buffer = []

    def read(self):
        with open(self.path, "r") as f:
            self.buffer = f.readlines()
        return self.buffer
