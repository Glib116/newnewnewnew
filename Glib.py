from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, 
                             QListWidget, QInputDialog, QHBoxLayout, QVBoxLayout,
                             QFormLayout, QLineEdit, QTextEdit)

app = QApplication([])

app.setStyleSheet("""
                  
                  QWidget {
                      background-color: green;
                  }
                  QPushButton {
                      background-color: blue;
                      border: 5px solid black;
                      color: yellow;
                      border-radius: 10px;
                      font-family: Montserrat;
                      font-size: 22px;
                      font-weight: bold;
                      
                  }
                  QInputDialog {
                      background-color: blue;
                      color: white;
                      font-family: Montserrat;
                      font-size: 16px;
                      border: 5px solid black;
                      border-radius: 10px;
                  }
                  QLabel {
                      font-family: Montserrat;
                      font-size: 20px;
                      color: red;
                      font-weight: bold;
                  }
                  QListWidget {
                      background-color: white;
                      color: black;
                      font-family: Montserrat;
                      font-size: 16px;
                      border: 3px solid black;
                      border-radius: 10px;
                      font-weight: bold;
                  }
                  QLineEdit {
                      background-color: white;
                      color: black;
                      font-family: Montserrat;
                      font-size: 16px;
                      border: 1px solid black;
                      border-radius: 10px;
                  }
                  QTextEdit {
                      background-color: gray;
                      color: black;
                      font-family: Montserrat;
                      font-size: 22px;
                      font-weight: bold;
                      border: 6px solid black;
                      border-radius: 10px;
                      
                  }
                  
                  """)

# Список для зберігання заміток
notes = []

# Створюємо головне вікно програми
notes_win = QWidget()  # Вікно для взаємодії з користувачем
notes_win.setWindowTitle('Smart Notes')  # Установлюємо заголовок вікна
notes_win.resize(800, 600)  # Задаємо розмір вікна 800x600 пікселів

# Виджет для відображення списку заміток
list_notes = QListWidget()  # Список, де відображатимуться назви заміток
list_notes_label = QLabel('Список заміток:')  # Текстова мітка для списку заміток

# Кнопки для роботи із замітками
button_note_create = QPushButton('Створити замітку')  # Кнопка створення нової замітки
button_note_del = QPushButton('Видалити замітку')  # Кнопка видалення вибраної замітки
button_note_save = QPushButton('Зберегти замітку')  # Кнопка збереження змін до замітки

# Поле для введення тегів
field_tag = QLineEdit()  # Текстове поле для введення тегу
field_tag.setPlaceholderText('Введіть тег...')  # Текст-підказка всередині поля

# Текстове поле для введення тексту замітки
field_text = QTextEdit()  # Багаторядкове текстове поле для запису вмісту замітки

# Кнопки для роботи з тегами
button_tag_add = QPushButton('Додати тег')  # Кнопка для додавання нового тегу
button_tag_del = QPushButton('Вдалити тег')  # Кнопка для видалення вибраного тегу
button_tag_search = QPushButton('Пошук тегів')  # Кнопка для пошуку заміток за тегами

# Виджет для відображення списку тегів
list_tags = QListWidget()  # Список, де відображатимуться теги
list_tags_label = QLabel('Список тегів')  # Текстова мітка для списку тегів

# Головний макет вікна
layout_notes = QHBoxLayout()  # Горизонтальний макет для організації елементів

# Перша колонка (текст замітки)
col1 = QVBoxLayout()  # Вертикальний макет для організації елементів у колонці
col1.addWidget(field_text)  # Додаємо текстове поле до першої колонки

# Друга колонка (список заміток, кнопки, список тегів)
col2 = QVBoxLayout()  # Вертикальний макет для другої колонки
col2.addWidget(list_notes_label)  # Додаємо мітку для списку заміток
col2.addWidget(list_notes)  # Додаємо список заміток

# Рядок з кнопками для управління замітками
row1 = QHBoxLayout()  # Горизонтальний макет для кнопок
row1.addWidget(button_note_create)  # Додаємо кнопку створення замітки
row1.addWidget(button_note_del)  # Додаємо кнопку видалення замітки

# Рядок для кнопки збереження замітки
row2 = QHBoxLayout()  # Горизонтальний макет
row2.addWidget(button_note_save)  # Додаємо кнопку збереження замітки

# Додаємо кнопки до другої колонки
col2.addLayout(row1)  # Додаємо рядок із кнопками створення та видалення
col2.addLayout(row2)  # Додаємо рядок із кнопкою збереження

# Додаємо список тегів до другої колонки
col2.addWidget(list_tags_label)  # Додаємо мітку для списку тегів
col2.addWidget(list_tags)  # Додаємо список тегів
col2.addWidget(field_tag)  # Додаємо текстове поле для введення тегу

# Рядок з кнопками для управління тегами
row3 = QHBoxLayout()  # Горизонтальний макет
row3.addWidget(button_tag_add)  # Додаємо кнопку додавання тегу
row3.addWidget(button_tag_del)  # Додаємо кнопку видалення тегу

# Рядок для кнопки пошуку тегів
row4 = QHBoxLayout()  # Горизонтальний макет
row4.addWidget(button_tag_search)  # Додаємо кнопку пошуку тегів

# Додаємо кнопки для роботи з тегами до другої колонки
col2.addLayout(row3)  # Додаємо рядок із кнопками додавання та видалення тегів
col2.addLayout(row4)  # Додаємо рядок із кнопкою пошуку тегів

# Додаємо обидві колонки до головного макета
layout_notes.addLayout(col1, stretch=2)  # Додаємо першу колонку з текстовим полем (з більшим пріоритетом)
layout_notes.addLayout(col2, stretch=1)  # Додаємо другу колонку (з меншою шириною)

# Установлюємо головний макет для вікна
notes_win.setLayout(layout_notes)  # Задаємо головний макет для вікна



notes_win.show()

    
app.exec_()


