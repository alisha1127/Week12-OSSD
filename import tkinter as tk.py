import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.count = 0
        self.root = root
        self.root.title("Simple Counter")

        self.label = tk.Label(root, text="Count: 0", font=("Arial", 24))
        self.label.pack(pady=20)

        self.button = tk.Button(root, text="Increase Count", command=self.increase_count, font=("Arial", 16))
        self.button.pack(pady=14)
        
        self.button = tk.Button(root, text="Decrease Count", command=self.decrease_count, font=("Arial", 16))
        self.button.pack(pady=15)
        
        
    def increase_count(self):
        self.count += 1
        self.label.config(text=f"Count: {self.count}")
                
    def decrease_count(self):
        self.count -= 1
        self.label.config(text=f"Count: {self.count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()

