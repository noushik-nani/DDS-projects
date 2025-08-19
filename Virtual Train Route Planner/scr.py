# train_route_planner.py
# Virtual Train Route Planner using Doubly and Circular Linked Lists

class StationNode:
    """Node representing a train station."""
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None


class TrainRoute:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.is_circular = False
        print("🚆 Welcome to the Virtual Train Route Planner!")

    def add_station(self, name):
        """Add a new station to the end of the route."""
        if not name.strip():
            print("⚠️  Station name cannot be empty.")
            return

        # Avoid duplicates
        if self._find_station(name):
            print(f"❌ '{name}' already exists in the route.")
            return

        new_node = StationNode(name.strip())

        if not self.head:
            self.head = self.tail = self.current = new_node
            print(f"✅ Added: {name} (starting point)")
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            print(f"✅ Added: {name}")

        # Reconnect circular if needed
        if self.is_circular:
            self._make_circular()

    def _find_station(self, name):
        """Check if station exists."""
        curr = self.head
        while curr:
            if curr.name.lower() == name.lower():
                return curr
            curr = curr.next
            if curr == self.head:  # Circular break
                break
        return None

    def _make_circular(self):
        """Make the route circular by linking tail to head."""
        if self.head and self.tail:
            self.tail.next = self.head
            self.head.prev = self.tail

    def _break_circular(self):
        """Break circular link (for linear mode)."""
        if self.tail:
            self.tail.next = None
        if self.head:
            self.head.prev = None

    def toggle_circular(self):
        """Toggle between linear and circular route mode."""
        self.is_circular = not self.is_circular
        if self.is_circular:
            self._make_circular()
            print("🔁 Circular mode: ON. Route will loop.")
        else:
            self._break_circular()
            print("🔁 Circular mode: OFF. Linear route.")

    def move_next(self):
        """Move to the next station."""
        if not self.current:
            print("❌ No stations in the route.")
            return

        if not self.current.next:
            if self.is_circular:
                self.current = self.head
                print(f"🚂 Arrived at: {self.current.name} (Looped back!)")
            else:
                print("🔚 End of the line. No next station.")
        else:
            self.current = self.current.next
            print(f"🚂 Arrived at: {self.current.name}")

    def move_prev(self):
        """Move to the previous station."""
        if not self.current:
            print("❌ No stations in the route.")
            return

        if not self.current.prev:
            if self.is_circular:
                self.current = self.tail
                print(f"🚂 Arrived at: {self.current.name} (Looped back from start!)")
            else:
                print("🏁 You're at the first station.")
        else:
            self.current = self.current.prev
            print(f"🚂 Arrived at: {self.current.name}")

    def view_route(self):
        """Display the full route."""
        if not self.head:
            print("\n🛤️  No stations added yet.")
            return

        print("\n" + "━" * 60)
        print("🗺️  FULL TRAIN ROUTE")
        print("━" * 60)

        stations = []
        curr = self.head
        if not curr:
            print("📭 Empty route.")
            return

        while True:
            stations.append(curr.name)
            curr = curr.next
            if curr == self.head and self.is_circular:
                break  # Full loop
            if curr is None:
                break

        # Build route string
        route_str = " ➔ ".join(stations)
        if self.is_circular:
            route_str += " ➔ " + stations[0] + " (loop)"

        print(f"🛣️  Route: {route_str}")
        print(f"🔁 Mode: {'Circular' if self.is_circular else 'Linear'}")
        print("━" * 60)

    def current_station(self):
        """Show current train position."""
        if self.current:
            print(f"\n📍 Currently at: **{self.current.name}**")
        else:
            print("\n❌ Train not initialized — no stations.")

    def menu(self):
        while True:
            print("\n" + "═" * 50)
            print("🚆 VIRTUAL TRAIN ROUTE PLANNER")
            print("═" * 50)
            print("1. ➕ Add Station")
            print("2. 🔁 Toggle Circular Route Mode")
            print("3. ⏩ Move to Next Station")
            print("4. ⏪ Move to Previous Station")
            print("5. 🗺️  View Full Route")
            print("6. 📍 Current Station")
            print("7. 🚪 Exit")

            choice = input("\n👉 Choose an option (1-7): ").strip()

            if choice == '1':
                name = input("Enter station name: ").strip()
                self.add_station(name)
            elif choice == '2':
                self.toggle_circular()
            elif choice == '3':
                self.move_next()
            elif choice == '4':
                self.move_prev()
            elif choice == '5':
                self.view_route()
            elif choice == '6':
                self.current_station()
            elif choice == '7':
                print("👋 Thank you for riding the Virtual Train! Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please select 1–7.")


# -----------------------------
# 🚀 Run the Program
# -----------------------------

if __name__ == "__main__":
    route = TrainRoute()
    route.menu()
