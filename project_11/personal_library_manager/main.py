import json
class BOOK_COLLECTION:
    def __init__(self):
        self.book_list=[]
        self.storage_file="book_data.json"
        self.load_file()
    def load_file(self):
        try:
            with open(self.storage_file,"r") as file:
                self.book_list=json.load(file)
        except(FileNotFoundError,json.JSONDecodeError):
            self.book_list=[]
    def save_file(self):
        with open(self.storage_file,"w") as file:
            json.dump(self.book_list,file,indent=4)
    def create_new_book(self):
        book_title:str=input("Enter a book title : ")
        book_author:str=input("Enter a book author : ")
        publication_year:int=int(input("Enter a book publication year : "))
        book_genre:str=input("Enter a book genre : ")
        read:str=input("Have you read this book ? (yes/no) : ").strip().lower()=="yes"
        new_book={
            "title":book_title,
            "author":book_author,
            "publication_year":publication_year,
            "book_genre":book_genre,
            "read":read
        }
        self.book_list.append(new_book)
        self.save_file()
        print("Book added sucessfully.")
    def delete_book(self):
        book_title:str=input("Enter a book title you want to remove or delete : ")
        for book in self.book_list:
            if book["title"].lower()==book_title.lower():
                self.book_list.remove(book)
                self.save_file()
                print("Book remove sucessfully")
                return
        print("Book no found!")
    # find Books
    def find_book(self):
        print("Search by : \n1. Title \n2. Author ")
        choise:int=int(input("Enter your choise : "))
        search_term=input("Enter search term : ")
        if choise ==1:
            found_books=[book
             for book in self.book_list 
             if search_term in book["title"].lower()
               ]
        elif choise == 2:
            found_books=[
                book
                for book in self.book_list
                if search_term in book["author"].lower()
            ]
        if found_books:
            print("\nMatching Books : ")
            for i, book in enumerate(found_books,1):
                status="Read" if book["read"] else "Unread"
                print(f"{i}. {book['title']} by {book['author']} ({book['publication_year']} - {book['book_genre']} - {status})")
        else:
            print("No match book found.\n")

    def update_book(self):
        """Modify the details of an existing book in the collection."""
        book_title=input("Enter a book title you want to edit : ")
        for book in self.book_list:
            if book['title'].lower()==book_title.lower():
                print("Leave blank to keep existing value.")
                book['title']=input(f"New title ({book['title']}) : ") or book['title']
                book['author']=input(f"New author ({book['author']}) : ") or book['author']
                book['publication_year']=int(input(f"New publication_year ({book['publication_year']})")) or book['publication_year']
                book['book_genre']=input(f"New genre ({book['book_genre']})") or book['book_genre']
                book['read']=(input(f"Have you read this book? (yes/no)").strip().lower()=="yes")
                self.save_file()
                print("Book update sucessfully!\n")
                return
        print("Book not found!\n")

    def show_all_books(self):
        if not self.book_list:
            print("Your Book collection is empty.")
            return
        print("Your Book Collection")
        for i,book in enumerate(self.book_list,1):
            reading_status="Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['publication_year']} - ({book['book_genre']}) - {reading_status})")
        print()
    
    def show_redaing_progress(self):
        total_book=len(self.book_list)
        complete_book=sum(1 for book in self.book_list if book ["read"])
        completeion_rate=(
            (complete_book/total_book*100) if total_book >0 else 0
        )
        print(f"Total books in collection : {total_book}")
        print(f"Reading progress : {completeion_rate:.2f}%")

    def main(self):
        while True:
             print("📚 Welcome to Your Book Collection Manager! 📚")
             print("1. Add a new book")
             print("2. Remove a book")
             print("3. Find a book")
             print("4. Update a book")
             print("5. Show all books")
             print("6. Show Reading Progress")
             print("7. Exist")
             choise:int=int(input("please enter your choise (1 to 7 ) : "))
             if choise == 1:
                 self.create_new_book()
             elif choise == 2:
                 self.delete_book()
             elif choise == 3:
                 self.find_book()
             elif choise== 4:
                 self.update_book()
             elif choise == 5:
                 self.show_all_books()
             elif choise == 6:
                 self.show_redaing_progress()
             elif choise ==7:
                 self.save_file()
                 print("Thank you for using Book Collection Manager . Goodbye!")
                 break
             else:
                 print("Invalid choise! Please try again with a valid number.")

                 
if __name__=='__main__':
    BOOK_COLLECTION().main()

