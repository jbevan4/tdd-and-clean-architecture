class ConnectionHandler():
    def __init__(self, data_source):
        self.data_source = data_source
        data_source.connect()

    def set_up(self):
        self.data_source.set_up(cache=True, max_connections=256)
