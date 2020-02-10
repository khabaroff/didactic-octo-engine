from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

# menu markup

menu_buttons = {
    "books": "Книги"
}

menu_markup = ReplyKeyboardMarkup(True, True)
menu_markup.row(menu_buttons['books'])

# books

books = {
    "book_1": {
        "name": "kniga 1",
        "path": "books/01.pdf"
    },
    "book_2": {
        "name": "kniga 2",
        "path": "books/02.pdf"
    },
    "book_3": {
        "name": "kniga 3",
        "path": "books/03.pdf"
    }
}

book_paths = [books[book_name]["path"] for book_name in books]

# books markup

books_markup = InlineKeyboardMarkup()

for book_name in books:
    name = books[book_name]["name"]
    path = books[book_name]["path"]
    book_button = InlineKeyboardButton(text=name, callback_data=path)
    books_markup.add(book_button)

# messages

messages = {
    'start': 'Добро пожаловать!',
    "books": "Выберите книгу",
    "take_it": "Приятного прочтения"
}