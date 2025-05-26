import tkinter as tk
from tkinter import messagebox
events = []

def save_event():
    event_name = event_entry.get()
    priority = priority_entry.get()
    
    if not event_name or not priority:
        messagebox.showwarning("Input Error", "Please enter both event and priority.")
        return
    
    events.append((event_name, priority))
    display_events()
    event_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)

def display_events():
    result_text.delete("1.0", tk.END)
    for event, priority in events:
        result_text.insert(tk.END, f"{event} - {priority}\n")

# GUI setup
root = tk.Tk()
root.title("Event ManagMENT")

tk.Label(root, text="Event").grid(row=0, column=0)
event_entry = tk.Entry(root)
event_entry.grid(row=0, column=1)

tk.Label(root, text="Priority").grid(row=1, column=0)
priority_entry = tk.Entry(root)
priority_entry.grid(row=1, column=1)

save_button = tk.Button(root, text="Save", command=save_event)
save_button.grid(row=2, column=0, columnspan=2)

result_text = tk.Text(root, height=15, width=30)
result_text.grid(row=3, column=0, columnspan=2)

root.mainloop()
