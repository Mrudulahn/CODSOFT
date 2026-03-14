import tkinter as tk
import math

# Game settings
PLAYER = "X"
AI = "O"

board = [" " for _ in range(9)]
player_score = 0
ai_score = 0

root = tk.Tk()
root.title("Tic Tac Toe AI")
root.geometry("400x500")
root.configure(bg="#1e1e2f")

buttons = []

# ---------------- WIN CHECK ----------------

def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board

# ---------------- MINIMAX AI ----------------

def minimax(board_state, is_maximizing):

    if check_winner(AI):
        return 1
    if check_winner(PLAYER):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board_state[i] == " ":
                board_state[i] = AI
                score = minimax(board_state, False)
                board_state[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board_state[i] == " ":
                board_state[i] = PLAYER
                score = minimax(board_state, True)
                board_state[i] = " "
                best_score = min(score, best_score)

        return best_score

# ---------------- AI MOVE ----------------

def ai_move():
    best_score = -math.inf
    best_move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = AI
    buttons[best_move]["text"] = AI

    check_game()

# ---------------- PLAYER MOVE ----------------

def player_move(i):
    if board[i] == " ":
        board[i] = PLAYER
        buttons[i]["text"] = PLAYER

        if not check_game():
            ai_move()

# ---------------- GAME STATUS ----------------

def check_game():
    global player_score, ai_score

    if check_winner(PLAYER):
        status_label.config(text="You Win 🎉")
        player_score += 1
        update_score()
        disable_buttons()
        return True

    if check_winner(AI):
        status_label.config(text="AI Wins 🤖")
        ai_score += 1
        update_score()
        disable_buttons()
        return True

    if is_draw():
        status_label.config(text="Draw 🤝")
        disable_buttons()
        return True

    return False

# ---------------- UI FUNCTIONS ----------------

def disable_buttons():
    for button in buttons:
        button.config(state="disabled")

def reset_board():
    global board
    board = [" " for _ in range(9)]

    for button in buttons:
        button.config(text=" ", state="normal")

    status_label.config(text="Your Turn")

def update_score():
    score_label.config(text=f"Player: {player_score}   AI: {ai_score}")

# ---------------- UI DESIGN ----------------

title = tk.Label(root, text="Tic Tac Toe AI",
                 font=("Arial",20,"bold"),
                 bg="#1e1e2f",
                 fg="white")
title.pack(pady=10)

score_label = tk.Label(root,
                       text="Player: 0   AI: 0",
                       font=("Arial",14),
                       bg="#1e1e2f",
                       fg="white")
score_label.pack()

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=20)

for i in range(9):
    button = tk.Button(frame,
                       text=" ",
                       font=("Arial",28,"bold"),
                       width=5,
                       height=2,
                       bg="#2d2d44",
                       fg="white",
                       activebackground="#44446a",
                       command=lambda i=i: player_move(i))

    button.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(button)

status_label = tk.Label(root,
                        text="Your Turn",
                        font=("Arial",14),
                        bg="#1e1e2f",
                        fg="lightgreen")
status_label.pack(pady=10)

restart_btn = tk.Button(root,
                        text="Restart Game",
                        font=("Arial",12,"bold"),
                        bg="#ff5757",
                        fg="white",
                        command=reset_board)

restart_btn.pack(pady=10)

root.mainloop()