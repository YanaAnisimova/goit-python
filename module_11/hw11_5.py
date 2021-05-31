class Client:
    def __init__(self, client_list, discount):
        self.client_list = client_list
        self.discount = discount
        self.current_client = 0

    def __next__(self):
        if self.current_client < len(self.client_list):
            self.current_client += 1
            return self.client_list[self.current_client-1]
        self.current_client = 0
        raise StopIteration

    def __iter__(self):
        return self
