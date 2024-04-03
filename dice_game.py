import tkinter as tk
from PIL import Image, ImageTk
import random
# important pip adding
class DiceApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Rolling App")

        self.label = tk.Label(master)
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.roll_button = tk.Button(master, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()
        # here my dice gif imgaes and random
        self.dice_images = [ImageTk.PhotoImage(Image.open(f"dice_{i}.gif")) for i in range(1, 7)]
    #throw dices
    def roll_dice(self):
        result = random.randint(1, 6)
        self.label.configure(image=self.dice_images[result - 1])
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(result))

def main():
    root = tk.Tk()
    app = DiceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
