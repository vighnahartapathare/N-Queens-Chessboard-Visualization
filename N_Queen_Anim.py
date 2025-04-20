import turtle
import time

# Function to draw the chessboard
def draw_board(size):
    turtle.speed(0)
    turtle.tracer(0)  # Turn off animation for faster drawing
    turtle.penup()
    turtle.bgcolor("#000000")  # Set black background
    start_x = -200
    start_y = 200
    square_size = 400 // size

    for row in range(size):
        for col in range(size):
            x = start_x + col * square_size
            y = start_y - row * square_size
            turtle.goto(x, y)
            # Real chessboard colors
            if (row + col) % 2 == 0:
                turtle.fillcolor("#94B4C1")  # light square
            else:
                turtle.fillcolor("#213448")  # dark square
            turtle.begin_fill()
            for _ in range(4):
                turtle.pendown()
                turtle.forward(square_size)
                turtle.right(90)
            turtle.end_fill()
            turtle.penup()
    turtle.update()  # Show the board all at once

# Function to draw a queen at a specific position
def draw_queen(row, col, size):
    square_size = 400 // size
    start_x = -200
    start_y = 200
    x = start_x + col * square_size + square_size // 2
    y = start_y - row * square_size - square_size // 2
    turtle.goto(x, y - square_size // 4)  # Adjust for better vertical alignment
    turtle.color("#F7374F")
    turtle.write("Q", align="center", font=("Arial", square_size // 2, "normal"))
    turtle.update()
    time.sleep(0.4)  # Delay for animation

# Function to check if a position is safe for a queen
def is_safe(board, row, col, size):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

# Recursive function to solve the N-Queens problem
def solve_nqueens(board, row, size):
    if row == size:
        for r in range(size):
            draw_queen(r, board[r], size)
        return True  # Stop after first solution

    for col in range(size):
        if is_safe(board, row, col, size):
            board[row] = col
            if solve_nqueens(board, row + 1, size):
                return True
            board[row] = -1
    return False

# Main function
def main():
    turtle.hideturtle()
    size = 8  # You can change this to any board size (e.g., 4, 6, 10)
    board = [-1] * size
    draw_board(size)
    if not solve_nqueens(board, 0, size):
        print("No solution exists")
    turtle.done()

if __name__ == "__main__":
    main()
