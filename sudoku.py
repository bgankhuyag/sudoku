from tkinter import *

board = [
    [4, 3, 0, 0, 5, 0, 8, 0, 0],
    [9, 8, 0, 0, 6, 1, 0, 0, 5],
    [1, 0, 5, 0, 8, 3, 0, 0, 0],
    [8, 0, 0, 3, 0, 0, 0, 5, 0],
    [0, 1, 0, 0, 2, 0, 0, 6, 0],
    [0, 9, 0, 0, 0, 5, 0, 0, 3],
    [0, 0, 0, 2, 9, 0, 6, 0, 8],
    [6, 0, 0, 1, 3, 0, 0, 2, 4],
    [0, 0, 8, 0, 7, 0, 0, 1, 9]
]

def isPossible(row, index, num):
    for k in range(9):
        if (k != index and board[row][k] == num):
            return False
    for j in range(9):
        if (j != row and board[j][index] == num):
            return False
    blockRow = 3*(row//3)
    blockColumn = 3*(index//3)
    for i in range(3):
        for m in range(3):
            if ((index != blockColumn+m and row != blockRow+i) and board[blockRow+i][blockColumn+m] == num):
                return False
    return True

def solveBoard(row, index):
    solved = False
    if (row == 9):
        solved = True
    elif (board[row][index] == 0):
        for i in range(1, 10):
            if (isPossible(row, index, i)):
                board[row][index] = i
                index+=1
                if (index == 9):
                    row+=1
                    index = 0
                if(solveBoard(row, index)):
                    solved = True
                    break
                else:
                    index-=1
                    if (index < 0):
                        row-=1
                        index = 8
                    board[row][index] = 0
    elif (not isPossible(row, index, board[row][index])):
        return False
    else:
        index+=1
        if (index == 9):
            row+=1
            index = 0
        if(solveBoard(row, index)):
            solved = True
    return solved

def solve():
    if (solveBoard(0, 0)):
        return
    else:
        print("It cannot be solved")

window = Tk()
window.title("Sudoku Solver")
window.geometry('442x379')
window.resizable(False, False)

def check_board(event):
    solve()
    for i in range(9):
        for j in range(9):
            index = (i*9)+j
            v = values[index]
            if (v.get() == '' or board[i][j] != int(v.get())):
                v.configure( background = 'RED')
            else:
                v.configure( background = 'GREEN')

def solve_board(event):
    solve()
    for i in range(9):
        for j in range(9):
            index = (i*9)+j
            v = values[index]
            v.delete(0, END)
            v.insert(END, str(board[i][j]))
            v.configure(background = 'GREEN')

values = []
window.bind("<Return>", check_board)
window.bind("<space>", solve_board)
def limitSizeDay(*args):
    value = sv.get()
    if len(value) > 1: sv.set(value[:1])

for i in range(9):
    for j in range(9):
        txtFrame = Frame(window, background = 'BLACK', borderwidth=1)
        sv = StringVar()
        sv.trace('w', limitSizeDay)
        txt = Entry(txtFrame, width=7, justify="center", textvariable=sv)
        values.append(txt)
        if (board[i][j] != 0):
            txt.insert(END, board[i][j])
            txt.configure(state="disabled")
        txtFrame.grid(column=j, row=i)
        if (j == 2 and i == 2):
            txt.grid(column=j, row=i, padx=(0, 5), pady=(0, 5), ipady=10)
        elif (j == 5 and i == 2):
            txt.grid(column=j, row=i, padx=(0, 5), pady=(0, 5), ipady=10)
        elif (j == 2 and i == 5):
            txt.grid(column=j, row=i, padx=(0, 5), pady=(0, 5), ipady=10)
        elif (j == 5 and i == 5):
            txt.grid(column=j, row=i, padx=(0, 5), pady=(0, 5), ipady=10)
        elif (j == 2):
            txt.grid(column=j, row=i, padx=(0, 5), ipady=10)
        elif (j == 5):
            txt.grid(column=j, row=i, padx=(0, 5), ipady=10)
        elif (i == 2):
            txt.grid(column=j, row=i, pady=(0, 5), ipady=10)
        elif (i==5):
            txt.grid(column=j, row=i, pady=(0, 5), ipady=10)
        else:
            txt.grid(column=j, row=i, ipady=10)
window.mainloop()
