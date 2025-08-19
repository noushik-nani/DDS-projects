# expression_calculator.py
# Stack-Based Expression Calculator (Infix to Postfix + Evaluation)

class ExpressionCalculator:
    def __init__(self):
        # Operator precedence (higher = executed first)
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.history = []  # Store calculation history
        print("🧮 Welcome to the Expression Calculator!")

    def display_info(self):
        print("\n" + "━" * 50)
        print("📘 Supported Operators:")
        print("   + : Addition")
        print("   - : Subtraction")
        print("   * : Multiplication")
        print("   / : Division")
        print("   ^ : Exponentiation (power)")
        print("   ( ) : Parentheses for grouping")
        print("👉 Example: 3 + 4 * (2 - 1)")
        print("━" * 50)

    def tokenize(self, expr):
        """Convert string expression to list of tokens (numbers and operators)."""
        tokens = []
        number = ""
        for char in expr:
            if char.isdigit() or char == '.':
                number += char
            else:
                if number:
                    tokens.append(float(number) if '.' in number else int(number))
                    number = ""
                if char in '()+-*/^':
                    tokens.append(char)
                elif char != ' ':
                    return None  # Invalid character
        if number:
            tokens.append(float(number) if '.' in number else int(number))
        return tokens

    def infix_to_postfix(self, tokens):
        """Convert infix tokens to postfix using stack."""
        if not tokens:
            return None

        output = []
        stack = []

        for token in tokens:
            # Operand: add to output
            if isinstance(token, (int, float)):
                output.append(token)

            # Left parenthesis: push to stack
            elif token == '(':
                stack.append(token)

            # Right parenthesis: pop until '('
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if not stack:
                    return None  # Mismatched parentheses
                stack.pop()  # Remove '('

            # Operator
            elif token in self.precedence:
                # Pop higher or equal precedence operators
                while (stack and stack[-1] != '(' and
                       stack[-1] in self.precedence and
                       self.precedence[stack[-1]] >= self.precedence[token]):
                    output.append(stack.pop())
                stack.append(token)

            else:
                return None  # Invalid token

        # Pop all remaining operators
        while stack:
            if stack[-1] in '()':
                return None  # Mismatched parentheses
            output.append(stack.pop())

        return output

    def evaluate_postfix(self, postfix):
        """Evaluate postfix expression using stack."""
        if not postfix:
            return None

        stack = []
        for token in postfix:
            if isinstance(token, (int, float)):
                stack.append(token)
            elif token in '+-*/^':
                if len(stack) < 2:
                    return None  # Invalid expression
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    if b == 0:
                        return None  # Division by zero
                    result = a / b
                elif token == '^':
                    result = a ** b
                stack.append(result)
            else:
                return None  # Invalid token
        return stack[0] if len(stack) == 1 else None

    def show_conversion_steps(self, tokens):
        """Show step-by-step infix to postfix conversion."""
        if not tokens:
            print("❌ No tokens to process.")
            return

        print(f"\n🔄 Converting to postfix...")
        output = []
        stack = []

        for token in tokens:
            print(f"  Token: {token}", end=" → ")

            if isinstance(token, (int, float)):
                output.append(token)
                print(f"Output: {output}")

            elif token == '(':
                stack.append(token)
                print(f"Stack: {stack}")

            elif token == ')':
                temp = []
                while stack and stack[-1] != '(':
                    op = stack.pop()
                    output.append(op)
                    temp.append(op)
                stack.pop() if stack else None
                print(f"Popped {temp} to output → Output: {output}")

            elif token in self.precedence:
                popped = []
                while (stack and stack[-1] != '(' and
                       stack[-1] in self.precedence and
                       self.precedence[stack[-1]] >= self.precedence[token]):
                    popped.append(stack.pop())
                stack.append(token)
                if popped:
                    output.extend(popped)
                    print(f"Popped {popped} to output → Output: {output}, Stack: {stack}")
                else:
                    print(f"Stack: {stack}")

        while stack:
            op = stack.pop()
            output.append(op)
        print(f"✅ Final Postfix: {' '.join(str(t) for t in output)}")
        return output

    def add_expression(self):
        print("\n➕ Enter a mathematical expression")
        self.display_info()
        expr = input("\nEnter infix expression: ").strip()
        if not expr:
            print("⚠️  Expression cannot be empty.")
            return

        tokens = self.tokenize(expr)
        if tokens is None:
            print("❌ Invalid expression. Use only numbers, + - * / ^ ( ) and spaces.")
            return

        postfix = self.infix_to_postfix(tokens)
        if postfix is None:
            print("❌ Invalid syntax (check parentheses or operators).")
            return

        result = self.evaluate_postfix(postfix)
        if result is None:
            print("❌ Evaluation failed (division by zero or invalid format).")
            return

        # Save to history
        infix_str = expr
        postfix_str = ' '.join(str(t) for t in postfix)
        entry = {
            "infix": infix_str,
            "postfix": postfix_str,
            "result": result
        }
        self.history.append(entry)
        print(f"✅ Expression added. Result: {result}")

    def convert_to_postfix(self):
        if not self.history:
            print("\n📜 No expressions in history.")
            return
        latest = self.history[-1]
        print(f"\n🔍 Converting: {latest['infix']}")
        tokens = self.tokenize(latest['infix'])
        self.show_conversion_steps(tokens)

    def evaluate_expression(self):
        if not self.history:
            print("\n📜 No expressions to evaluate.")
            return
        latest = self.history[-1]
        print(f"\n🧪 Evaluating: {latest['infix']} = {latest['result']}")

    def view_history(self):
        print("\n" + "━" * 70)
        print("📜 CALCULATION HISTORY")
        print("━" * 70)
        if not self.history:
            print("📭 No calculations yet.")
        for i, entry in enumerate(self.history, 1):
            print(f"{i}. Infix: {entry['infix']}")
            print(f"   → Postfix: {entry['postfix']}")
            print(f"   → Result: {entry['result']}")
        print("━" * 70)

    def menu(self):
        while True:
            print("\n" + "═" * 50)
            print("🧮 EXPRESSION CALCULATOR")
            print("═" * 50)
            print("1. ➕ Enter Expression")
            print("2. 🔍 Convert to Postfix (Step-by-step)")
            print("3. 🧪 Evaluate Expression")
            print("4. 📜 View History")
            print("5. 🚪 Exit")

            choice = input("\n👉 Choose an option (1-5): ").strip()

            if choice == '1':
                self.add_expression()
            elif choice == '2':
                self.convert_to_postfix()
            elif choice == '3':
                self.evaluate_expression()
            elif choice == '4':
                self.view_history()
            elif choice == '5':
                print("👋 Thank you for using the Expression Calculator!")
                break
            else:
                print("❌ Invalid choice. Please select 1–5.")


# -----------------------------
# 🚀 Run the Program
# -----------------------------

if __name__ == "__main__":
    calc = ExpressionCalculator()
    calc.menu()
