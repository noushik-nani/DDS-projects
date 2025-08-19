# library_system.py
# E-Library Book Management with Linked List and Stack (Undo)

class BookNode:
    """Node for the linked list representing a book."""
    def __init__(self, title, author):
        self.book = {
            "title": title,
            "author": author,
            "available": True
        }
        self.next = None


class LinkedList:
    """Singly linked list to manage book inventory."""
    def __init__(self):
        self.head = None

    def add_book(self, title, author):
        new_node = BookNode(title, author)
        new_node.next = self.head
        self.head = new_node
        return f"✅ '{title}' added to inventory."

    def find_book(self, title):
        """Return node and previous node for modification."""
        curr = self.head
        prev = None
        while curr:
            if curr.book["title"].lower() == title.lower():
                return curr, prev
            prev = curr
            curr = curr.next
        return None, None

    def remove_book(self, title):
        node, prev = self.find_book(title)
        if not node:
            return f"❌ '{title}' not found."
        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next
        return f"🗑️  '{title}' removed from inventory."

    def display_all(self):
        if not self.head:
            print("📚 No books in the library.")
            return
        print(f"{'Title':<25} {'Author':<20} {'Status':<12}")
        print("-" * 60)
        curr = self.head
        while curr:
            status = "Available" if curr.book["available"] else "Borrowed"
            print(f"{curr.book['title']:<25} {curr.book['author']:<20} {status:<12}")
            curr = curr.next
        print("-" * 60)

    def search(self, keyword):
        """Search by title or author (case-insensitive)."""
        results = []
        curr = self.head
        while curr:
            if (keyword.lower() in curr.book["title"].lower() or
                keyword.lower() in curr.book["author"].lower()):
                results.append(curr.book)
            curr = curr.next
        return results


class ActionStack:
    """Stack to support undo functionality."""
    def __init__(self):
        self.stack = []  # Each entry: ("borrow"|"return", title)

    def push(self, action, title):
        self.stack.append((action, title))

    def pop(self):
        return self.stack.pop() if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0


# -----------------------------
# 📚 Main Library System
# -----------------------------

class LibrarySystem:
    def __init__(self):
        self.inventory = LinkedList()
        self.undo_stack = ActionStack()
        print("📚 Welcome to the E-Library Management System!")

    def add_book(self):
        print("\n➕ Add a New Book")
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        if not title or not author:
            print("⚠️  Title and author are required.")
            return
        print(self.inventory.add_book(title, author))

    def borrow_book(self):
        title = input("\nEnter the title to borrow: ").strip()
        if not title:
            print("⚠️  Please enter a title.")
            return

        node, _ = self.inventory.find_book(title)
        if not node:
            print(f"❌ '{title}' does not exist in the library.")
            return
        if not node.book["available"]:
            print(f"❌ '{title}' is already borrowed.")
            return

        node.book["available"] = False
        self.undo_stack.push("borrow", title)
        print(f"✅ You borrowed '{title}'.")

    def return_book(self):
        title = input("\nEnter the title to return: ").strip()
        if not title:
            print("⚠️  Please enter a title.")
            return

        node, _ = self.inventory.find_book(title)
        if not node:
            print(f"❌ '{title}' does not exist in the library.")
            return
        if node.book["available"]:
            print(f"❌ '{title}' is already available.")
            return

        node.book["available"] = True
        self.undo_stack.push("return", title)
        print(f"✅ '{title}' has been returned.")

    def undo_last_action(self):
        action = self.undo_stack.pop()
        if not action:
            print("🔙 No actions to undo.")
            return

        act_type, title = action
        node, _ = self.inventory.find_book(title)
        if not node:
            print(f"⚠️  Book '{title}' not found during undo.")
            return

        if act_type == "borrow":
            node.book["available"] = True
            print(f"🔙 Undo: '{title}' is back on the shelf.")
        elif act_type == "return":
            node.book["available"] = False
            print(f"🔙 Undo: You re-borrowed '{title}'.")

    def search_books(self):
        keyword = input("\nEnter title or author to search: ").strip()
        if not keyword:
            print("⚠️  Please enter a keyword.")
            return

        results = self.inventory.search(keyword)
        if not results:
            print(f"🔍 No books found matching '{keyword}'.")
            return

        print(f"\n🔎 Search Results for '{keyword}':")
        print(f"{'Title':<25} {'Author':<20} {'Status':<12}")
        print("-" * 60)
        for book in results:
            status = "Available" if book["available"] else "Borrowed"
            print(f"{book['title']:<25} {book['author']:<20} {status:<12}")
        print("-" * 60)

    def view_all_books(self):
        print("\n" + "="*60)
        print("📖 FULL INVENTORY")
        print("="*60)
        self.inventory.display_all()

    def menu(self):
        while True:
            print("\n" + "═" * 40)
            print("📚 E-Library Management System")
            print("═" * 40)
            print("1. ➕ Add Book")
            print("2. 📖 Borrow Book")
            print("3. 🔄 Return Book")
            print("4. 🔙 Undo Last Action")
            print("5. 🔍 Search Books")
            print("6. 👀 View All Books")
            print("7. 🚪 Exit")

            choice = input("\n👉 Choose an option (1-7): ").strip()

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.undo_last_action()
            elif choice == '5':
                self.search_books()
            elif choice == '6':
                self.view_all_books()
            elif choice == '7':
                print("👋 Thank you for using the E-Library System. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please select 1–7.")


# -----------------------------
# 🚀 Run the Program
# -----------------------------

if __name__ == "__main__":
    library = LibrarySystem()
    library.menu()
