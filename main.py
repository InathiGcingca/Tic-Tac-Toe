from tkinter import *
from tkinter import messagebox




#Disables all buttons
def disable_all_buttons(n):
    for i in range(3):
        for j in range(3):
            n[i][j].config(state=DISABLED)

#Create a function that clicks and displays an X or O.
def clicked(b,r,c):
   #player
   global click, count



   if b[r][c]["text"] == " " and click == True:
       b[r][c]["text"] = "X"
       click = False
       count += 1
       check_if_win(b, count)



   elif b[r][c]["text"] == " " and click == False:
       b[r][c]["text"] = "O"
       click = True
       count += 1
       check_if_win(b, count)

   else:
       messagebox.showerror("Tic Tac Toe", "Hey that box has already been selected\nPick another box")
       

#Check players winning status
def check_if_win(button, c):
    global winner
    winner = False

    for i in range(3):
        if button[0][i]["text"] == "X" and  button[1][i]["text"] == "X" and button[2][i]["text"] == "X" :
            button[0][i].config(bg="red")
            button[1][i].config(bg="red")
            button[2][i].config(bg="red")
            winner = True
            messagebox.showinfo("Winner",f"{button[1][i]["text"]} is the Winner!")
            disable_all_buttons(button)
            break

        elif button[i][0]["text"] == "X" and  button[i][1]["text"] == "X" and button[i][2]["text"] == "X" :
            button[i][0].config(bg="red")
            button[i][1].config(bg="red")
            button[i][2].config(bg="red")
            winner = True
            messagebox.showinfo("Winner",f"{button[i][1]["text"]} is the Winner!")
            disable_all_buttons(button)
            break

        elif button[0][i]["text"] == "O" and  button[1][i]["text"] == "O" and  button[2][i]["text"] == "O" :
            button[0][i].config(bg="red")
            button[1][i].config(bg="red")
            button[2][i].config(bg="red")
            winner = True
            messagebox.showinfo("Winner", f"{button[1][i]["text"]} is the Winner!")
            disable_all_buttons(button)
            break

        elif button[i][0]["text"] == "O" and button[i][1]["text"] == "O" and button[i][2]["text"] == "O":
            button[i][0].config(bg="red")
            button[i][1].config(bg="red")
            button[i][2].config(bg="red")
            winner = True
            messagebox.showinfo("Winner", f"{button[i][1]["text"]} is the Winner!")
            disable_all_buttons(button)
            break

        elif button[0][0]["text"] == "X" and  button[1][1]["text"] == "X" and  button[2][2]["text"] == "X":
            button[0][0].config(bg="red")
            button[1][1].config(bg="red")
            button[2][2].config(bg="red")
            winner = True
            messagebox.showinfo("Winner", f"{button[0][0]["text"]} is the Winner!")
            disable_all_buttons(button)
            break

        elif button[0][0]["text"] == "O" and  button[1][1]["text"] == "O" and  button[2][2]["text"] == "O":
            button[0][0].config(bg="red")
            button[1][1].config(bg="red")
            button[2][2].config(bg="red")
            winner = True
            messagebox.showinfo("Winner", f"{button[0][0]["text"]} is the Winner!")
            disable_all_buttons(button)
            break

        elif button[0][2]["text"] == "X" and button[1][1]["text"] == "X" and button[2][0]["text"] == "X":
            button[0][2].config(bg="red")
            button[1][1].config(bg="red")
            button[2][0].config(bg="red")
            winner = True
            messagebox.showinfo("Winner", f"{button[1][1]["text"]} is the Winner!")
            disable_all_buttons(button)
            break

        elif button[0][2]["text"] == "O" and button[1][1]["text"] == "O" and button[2][0]["text"] == "O":
            button[0][2].config(bg="red")
            button[1][1].config(bg="red")
            button[2][0].config(bg="red")
            winner = True
            messagebox.showinfo("Winner", f"{button[1][1]["text"]} is the Winner!")
            disable_all_buttons(button)
            break

        elif winner == False and c == 9:
            messagebox.showinfo("Tie", "It's a Tie")
            disable_all_buttons(button)
            break




   





# Design window
# Creating the Canvas
root = Tk()
# Title of the window
root.title("Tic Tac Toe")



#Button

b = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]


#Create reset
def reset():
   global b
   global click, count
   click = True
   count = 0

   for i in range(3):
       for j in range(3):
           b[i][j] = Button(
               root,
               text=" ",
               font=("Helvetica", 20),
               height=3,
               width=6,
               command= lambda r = i, c = j : clicked(b,r,c)
           )
           b[i][j].grid(row= i , column= j)


#Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset )

reset()

root.mainloop()
