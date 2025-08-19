# 📚 E-Library Book Management

## 📌 Overview

**A command-line** e-library system that allows users to add, borrow, return, and search books, 
with undo functionality for recent actions. Designed as a Data Structures project using:

**Singly Linked List → To manage the book inventory
Stack (LIFO) → To enable undo of the most recent borrow/return action
Search & Filter → By title or author**
Perfect for learning core data structures in a real-world context.

---

## 🛠 Features
- Add books to the library inventory
- Borrow a book (updates availability)
- Return a book
- Undo the last action (borrow/return) using a stack
- Search books by title or author
- Filter and display all available books
- View full inventory with status
- Fully interactive command-line interface

---

## 📂 Data Structures Used
  - **Singly Linked List**(BookNode,LinkedList)
  - **Searching** -> Linear search with keyword matching
  - **Stack**(Python list) →  LIFO for actions
  - **Traverse** linked list

---

## 🚀 How to Run
```bash
# Clone the repository
git clone https://github.com/your-username/e-library-system.git
cd e-library-system/src

# Run the program
python library_system.py
