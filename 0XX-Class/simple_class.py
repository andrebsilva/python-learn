class Test:
    
    def __set_first_name(self, first_name):
        self.first_name = first_name
    
    def __set_last_name(self, last_name):
        self.last_name = last_name
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_complete_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __init__(self, first_name, last_name):
        self.__set_first_name(first_name)
        self.__set_last_name(last_name)
