class Book():
    def __init__(self,title,author,pages_num):
        self.current_page = 0
        self.is_open = False
        self.title = title
        self.author = author
        self.pages_num = pages_num
    def open(self):
        self.is_open = True
    def close(self):
        self.is_open = False
    def read(self):
        if self.is_open == True:
            print('Czytasz stronę', self.current_page)
        else:
            print('Książka jest zamknięta')
    def next_page(self):
        if self.is_open == True:
            self.current_page +=1
    def previous_page(self):
        if self.is_open == True:
            self.current_page -=1
    def book_status(self):
        print('Tytuł:',self.title,'\nAutor:',self.author,'\nLiczba stron:',self.pages_num,'\nBieżąca strona:',self.current_page)
        