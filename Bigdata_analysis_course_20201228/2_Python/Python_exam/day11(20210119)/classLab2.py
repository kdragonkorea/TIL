class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # def getBookInfo():
    #     print(f'책이름: {self.title}')
    #     print(f'저자: {self.author}')
    #     print(f'가격: {self.price}')
    #     print('--'*10)
    def getBookInfo(self):
        info = self.title + ',' +
        return

st1 = Book("파이썬정복", "김상형", 22000)
st2 = Book("파이썬1", "김상형1", 22000)
st3 = Book("파이썬2", "김상형2", 22000)

st1.getBookInfo()
st2.getBookInfo()
st3.getBookInfo()