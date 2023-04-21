import tkinter as tk

root = tk.Tk()
root.title("Table Generator")
root.configure(bg='#00E0CF')

# Logo
logo = tk.PhotoImage(file="download.png")
root.iconphoto(False, logo)

def generate_table():
    num1 = int(tea_spinbox.get())
    num2 = int(idli_spinbox.get())
    table_data = ""
    for i in range(1, num1+1):
        p = num2 * i
        table_data += f"{num2} x {i} = {p}\n"

    output.config(text=table_data)

# Frame - Data
frame = tk.Frame(root)
frame.pack()

# Frame 1
user_info_frame = tk.LabelFrame(frame, text="TABLE GENERATOR")
user_info_frame.grid(row=0, column=0)

page_title = tk.Label(user_info_frame, text="WELCOME TO TABLE GENERATOR", font=('Verdana', 30))
page_title.grid(row=0, column=0)

address_info = tk.Label(user_info_frame, text="It was used to generate the table\nExample: '2 x 2 = 4'")
address_info.grid(row=1, column=0)

# Frame 2
body_info_frame1 = tk.LabelFrame(frame, text="Items List")
body_info_frame1.grid(row=1, column=0, sticky="news")

# 1
tea = tk.Label(body_info_frame1, text="Enter your table range: ")
tea.grid(row=0, column=0)

tea_spinbox = tk.Spinbox(body_info_frame1, from_=0, to=20)
tea_spinbox.grid(row=0, column=2, padx=(0,0), pady=(0,0))

# 2
idli = tk.Label(body_info_frame1, text="Enter your table multiple number: ")
idli.grid(row=0, column=4, padx=(150,0), pady=(0,0))

idli_spinbox = tk.Spinbox(body_info_frame1, from_=0, to=20)
idli_spinbox.grid(row=0, column=6)

# Frame 3
body_info_frame2 = tk.LabelFrame(frame, text="Items List")
body_info_frame2.grid(row=3, column=0, sticky="news")

total_cost = tk.Label(body_info_frame2, text="Total: ")
total_cost.grid(row=0, column=0)

output = tk.Label(body_info_frame2, text="", font=('Verdana', 14), justify='left')
output.grid(row=1, column=0)

# Button
button = tk.Button(body_info_frame1, text="Enter Data", command=generate_table, bg='#00E0CF')
button.grid(row=3, column=6)

root.mainloop()
