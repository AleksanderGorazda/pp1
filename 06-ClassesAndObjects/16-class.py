class Book():
    def __init__(self,title,author,pages_num):
        self.current_page = 0
        self.is_open = False
    def open(self):
        self.is_open = True
    def close(self):
        self.is_open = False
    def read(self):
        if self.is_open = True:
            print('Czytasz stronę', self.current_page)
    def next_page(self):
        if self.is_open = True:
            self.current_page +=1
    def previous_page(self):
        if self.is_open = True:
            self.current_page -=1
        