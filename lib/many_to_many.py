import datetime
class Author:
    all = []
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) and 1<= len(value) <=125 :
            raise TypeError("Name must be a string and must be between 1 and 125 characters")
        
    
    
        
    def sign_contract(self,book,date, royalties):
        return  Contract(self,book,date,royalties) #creates the relation
       
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def total_royalties(self):
        royalties = [contract.royalties for contract in Contract.all if contract.author == self]
        return sum(royalties)

    def __repr__(self):
        return f"Author: {self.name}"
    
   
   


class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]
    
    def sign_contract(self,author,date,royalties):
        return Contract(author,self,date,royalties)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def __repr__(self):
        return f"Book title : {self.title}"
    


class Contract:
    all = []
    def __init__(self, author, book,date,royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise TypeError("Author must be from Author class")
        if isinstance(book, Book):
            self.book = book
        else:
            raise TypeError("Book must be from Book class")
        
        if isinstance(date, str):
            self.date = date
            
        else:
            raise TypeError("Date must be a string")
        if isinstance(royalties, int):
            self.royalties = royalties 
        else:
            raise TypeError("Royalties must be a number.")
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls,date):
            return[contract for contract in cls.all if contract.date == date]
    def __repr__(self):
        return f"A contract for the book {self.book.title} {self.author.name}"

if __name__ == "__main__":
        author = Author("Sandra Brown")
        book1 = Book("The crush")
        book2 = Book("Summer Nights")
        book3 = Book("Brave Heart")
    
        c1 =Contract(author, book1, "01/01/2001", 10)
        c2 =Contract(author, book2, "01/01/2001", 20)
        c3 =Contract(author, book3, "01/01/2001", 30)

        print(Contract.contracts_by_date("02/01/2001"))