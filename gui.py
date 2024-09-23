import numpy as np
from PySide6.QtWidgets import (QApplication, QWidget, QGridLayout, QLineEdit, QVBoxLayout, QPushButton, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from solver import solver
class SudokuGUI(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Sudoku Solver")
        self.setGeometry(300, 300, 400, 400)
        
       
        grid_layout = QGridLayout()
        
      
        self.cells = []
        for row in range(9):
            row_cells = []
            for col in range(9):
                cell = QLineEdit()
                cell.setMaxLength(1) 
                cell.setFixedSize(40, 40)
                cell.setAlignment(Qt.AlignCenter) 
                cell.setFont(QFont("Arial", 16))  
                
                if (row % 3 == 0 and row != 0) and (col % 3 == 0 and col != 0) :
                    cell.setStyleSheet("border-top: 2px solid black; border-left: 2px solid black;")
                elif row % 3 == 0 and row != 0:
                    cell.setStyleSheet("border-top: 2px solid black;")
                elif col % 3 == 0 and col != 0:
                    cell.setStyleSheet("border-left: 2px solid black;")
                
                grid_layout.addWidget(cell, row, col)
                row_cells.append(cell)
            self.cells.append(row_cells)
        
        solve_button = QPushButton("Résoudre")
        solve_button.clicked.connect(self.solve_sudoku)
        
        layout = QVBoxLayout()
        layout.addLayout(grid_layout)
        layout.addWidget(solve_button)
        
        self.setLayout(layout)
    
    def get_grid_values(self):
        grid = np.zeros((9, 9), dtype=int) 
        for row in range(9):
            for col in range(9):
                text = self.cells[row][col].text()
                if text.isdigit():
                    grid[row, col] = int(text)
                else:
                    grid[row, col] = 0 
        return grid
    
    def solve_sudoku(self):
        grid = self.get_grid_values()

        solved = self.solve_algorithm(grid)
        
        if solved is not None:
            self.display_solution(solved)
        else:
            QMessageBox.warning(self, "Erreur", "Le Sudoku ne peut pas être résolu.")
    
    def solve_algorithm(self, grid):
        return solver(grid)
    
    def display_solution(self, solution):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].setText(str(solution[row, col]))

if __name__ == "__main__":
    app = QApplication([])
    window = SudokuGUI()
    window.show()
    app.exec()