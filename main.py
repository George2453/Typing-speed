import tkinter as tk
import time


class TypingTest:
    def __init__(self, master):  
        self.master = master
        master.title("\nПечатайте ваш текст")

        # create text entry widget and label for displaying result
        self.text_entry = tk.Entry(master, width= 100)
        self.text_entry.pack(pady=10)
        self.result_label = tk.Label(master, text="\nПосле того, как вы напечатаете текст нажмите Enter")
        self.result_label.pack(pady=10)

        # bind Enter key to check_result function
        self.text_entry.bind("<Return>", self.check_result)

        # set initial values for variables
        self.start_time = None
        self.end_time = None
        self.text_length = None
        self.char_count = 0

    def check_result(self, event):
        # get user input and calculate length and time taken
        user_input = self.text_entry.get()
        words = user_input.split()
        self.text_length = len(user_input)
        self.end_time = time.time()
        time_taken = self.end_time - self.start_time

        # calculate speed in words per minute and characters per minute
        speed = int(len(words) / (time_taken / 60))
        self.char_count += self.text_length
        char_speed = int(self.char_count / (time_taken / 60))

        # display result in label
        result_text = f"\n{speed} слов/мин.\n \nили\n\n {char_speed} сим/мин."
        self.result_label.config(text=result_text)


    def start_test(self):
        # set start time and focus on text entry widget
        self.start_time = time.time()
        self.text_entry.focus()

root = tk.Tk()
typing_test = TypingTest(root)
root.geometry("700x350")
typing_test.start_test()
root.mainloop()
