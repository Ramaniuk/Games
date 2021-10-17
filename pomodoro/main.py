import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label['text'] = "Long Break"
        timer_label['fg'] = RED

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    elif reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global check_mark_sign
    minutes = math.floor(count / 60) # "01:35"
    seconds = count % 60 # "01:35"
    if seconds < 10:    # "01:09"
        seconds = "0" + str(seconds)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_mark_sign += ""
        if reps % 2 == 0:
            check_mark_sign += "✓"
            check_mark.config(text=check_mark_sign)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW) #background

canvas = tkinter.Canvas(width=200, height=224,bg=YELLOW,highlightthicknes=0) # get rid of border
tomato_img = tkinter.PhotoImage(file="tomato.png") #read file
canvas.create_image(100, 112, image=tomato_img) #x,y position
timer_text = canvas.create_text(100,130, text="00.00", fill="white", font=(FONT_NAME,35,"bold")) #x,y position of text
canvas.grid(column=1, row=1)

timer_label = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME,38))
timer_label.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", highlightthicknes=0, command=start_timer)
start_button.grid(column=0, row=2)

check_mark = tkinter.Label(bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)

reset_button = tkinter.Button(text="Reset",highlightthicknes=0,command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()