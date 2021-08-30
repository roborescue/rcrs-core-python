

class Edge():
    def __init__(self, start_x, start_y, end_x, end_y, _neighbor):
        self.start = [start_x, start_y]
        self.end = [end_x, end_y]
        self.line = [[start_x, start_y], [end_x, end_y]]
        self.neighbor = _neighbor

    def get_start_x(self):
        return self.start[0]

    def get_start_y(self):
        return self.start[1]

    def get_end_x(self):
        return self.end[0]

    def get_end_y(self):
        return self.end[1]

    def get_neighbor(self):
        return self.neighbor
