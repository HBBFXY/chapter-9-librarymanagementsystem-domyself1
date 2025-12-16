class Book:
    """书籍类"""
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        """借书"""
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        """还书"""
        self.is_borrowed = False

    def __str__(self):
        status = "已借出" if self.is_borrowed else "可借"
        return f"《{self.title}》- {self.author} (ISBN:{self.isbn}) 状态：{status}"

class User:
    """用户类"""
    def __init__(self, name, card_id):
        self.name = name
        self.card_id = card_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"用户：{self.name}，借书卡号：{self.card_id}"

class Library:
    """图书馆类"""
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def borrow_book(self, card_id, isbn):
        user = next((u for u in self.users if u.card_id == card_id), None)
        book = self.find_book_by_isbn(isbn)

        if not user:
            print("用户不存在")
            return

        if not book:
            print("图书不存在")
            return

        if book.borrow():
            user.borrow_book(book)
            print(f"{user.name} 成功借阅 {book.title}")
        else:
            print(f"{book.title} 已被借出")

    def return_book(self, card_id, isbn):
        user = next((u for u in self.users if u.card_id == card_id), None)
        book = self.find_book_by_isbn(isbn)

        if user and book:
            book.return_book()
            user.return_book(book)
            print(f"{user.name} 已归还 {book.title}")
        else:
            print("还书失败，信息有误")

    def check_book_status(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if book:
            print(book)
        else:
            print("未找到该书")

if __name__ == "__main__":
    library = Library()

    # 添加图书
    book1 = Book("Python程序设计", "张三", "1001")
    book2 = Book("数据结构", "李四", "1002")
    library.add_book(book1)
    library.add_book(book2)

    # 添加用户
    user1 = User("王五", "U001")
    library.add_user(user1)

    # 查看图书状态
    library.check_book_status("1001")

    # 借书
    library.borrow_book("U001", "1001")

    # 再次查看状态
    library.check_book_status("1001")

    # 还书
    library.return_book("U001", "1001")

    # 最终状态
    library.check_book_status("1001")

