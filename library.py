class library:
    def __init__(self):
         self.bookl=[]

    def add_book(self,book):
         self.bookl.append(book)

    def get_book(self,):
         return self.bookl
    
lib1=library()
lib1.add_book("Programming")
lib1.add_book("Math")
print(lib1.get_book())