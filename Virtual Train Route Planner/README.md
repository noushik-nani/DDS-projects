# 🚆 Virtual Train Route Planner

## 📌 Overview

A **command-line train navigation system** that allows users to traverse stations forward and backward, 
simulate loop routes, and navigate in real-time. Designed using:

Doubly Linked List → For bidirectional navigation (forward/backward)
Circular Linked List → To model loop routes (e.g., metro rings)
Station tracking → With current position and route display
Ideal for learning linked list variations and their real-world applications in
transportation systems.

---

## 🛠 Features
- Add train stations to a route
- Navigate forward and backward (using doubly linked list)
- Enable loop mode (circular route) — last station connects to first
- Display current station and full route
- Move to next/previous station with realistic feedback
- Toggle between linear and circular route modes
- Interactive menu with route visualization

  ---

  ## 📂 Data Structures Used
- **Node** with name and position
- **Boolean flag** is_circular
- **Loop Route**->Tail node points back to head

---
## 🚀 How to Run
```bash
# Clone the repository
git clone https://github.com/your-username/virtual-train-planner.git
cd virtual-train-planner/src

# Run the program
python train_route_planner.py
