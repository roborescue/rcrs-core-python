
class InputStream:
    def __init__(self, data) -> None:
        self.data = data
        self.index = 0
    
    def read(self, count):
        data_list = bytearray()
        for i in range(count):
            data_list.append(self.data[self.index + i])
        self.index += count
        return data_list




class OutputStream:
    def __init__(self):
        self.byte_array = []

    def write(self, data_string):
        self.byte_array.extend(list(data_string))

    def getvalue(self):
        return ''.join(self.byte_array)
