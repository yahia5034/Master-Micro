import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PySide2.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import math
from sympy import symbols, sympify, lambdify
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Plotter")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Function Input
        self.function_label = QLabel("Enter a function of x:")
        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText("e.g., 5*x^3 + 2*x")

        # Min/Max Input
        self.min_label = QLabel("Enter the minimum value of x:")
        self.min_input = QLineEdit()
        self.max_label = QLabel("Enter the maximum value of x:")
        self.max_input = QLineEdit()

        # Plot Button
        self.plot_button = QPushButton("Plot")
        self.plot_button.clicked.connect(self.plot)

        # Matplotlib Figure
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Add Widgets to Layout
        self.layout.addWidget(self.function_label)
        self.layout.addWidget(self.function_input)
        self.layout.addWidget(self.min_label)
        self.layout.addWidget(self.min_input)
        self.layout.addWidget(self.max_label)
        self.layout.addWidget(self.max_input)
        self.layout.addWidget(self.plot_button)
        self.layout.addWidget(self.canvas)



    # ...

    def plot(self):
        function = self.function_input.text()
        xmin = self.min_input.text()
        xmax = self.max_input.text()

        try:
            xmin = int(xmin)
            xmax = int(xmax)

            x = symbols('x')  # Create a symbolic variable for x
            expr = sympify(function)  # Convert the user-entered function to a sympy expression

            # Create a lambda function that can be used to evaluate the sympy expression
            eval_expr = lambdify(x, expr, 'numpy')

            x_vals = np.linspace(xmin, xmax, 1000)  # Generate an array of x values

            # Evaluate the expression for each x value
            y_vals = eval_expr(x_vals)

            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x_vals, y_vals)
            ax.set_xlabel('x')
            ax.set_ylabel('f(x)')
            self.canvas.draw()

        except Exception as e:
            print("An error occurred:", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
