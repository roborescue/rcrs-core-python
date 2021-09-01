

class Edge():
    def __init__(self, start_x, start_y, end_x, end_y, _neighbour):
        self.start = [start_x, start_y]
        self.end = [end_x, end_y]
        self.line = [[start_x, start_y], [end_x, end_y]]
        self.neighbour = _neighbour

    def get_start_x(self):
        return self.start[0]

    def get_start_y(self):
        return self.start[1]

    def get_end_x(self):
        return self.end[0]

    def get_end_y(self):
        return self.end[1]

    def is_passable(self):
        return self.neighbour != None
    
    def get_neighbour(self):
        return self.neighbour


    def to_string(self):
        return "Edge from " + self.start + " to " + self.end + " , neighbour= " + self.neighbour 
    
