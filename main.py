from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Translate Function
def translate_text():
    try:
        text = input_text.get("1.0", END).strip()

        src = source_lang.get()
        dest = target_lang.get()

        if text == "":
            messagebox.showwarning("Warning", "Please enter text")
            return

        translated = GoogleTranslator(source=src, target=dest).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Main Window
root = Tk()
root.title("Language Translation Tool")
root.geometry("700x500")
root.config(bg="#dff6ff")

# Title
title = Label(root,
              text="Language Translation Tool",
              font=("Arial", 20, "bold"),
              bg="#dff6ff",
              fg="darkblue")

title.pack(pady=10)

# Input Label
input_label = Label(root,
                    text="Enter Text",
                    font=("Arial", 12, "bold"),
                    bg="#dff6ff")

input_label.pack()

# Input Box
input_text = Text(root,
                  height=8,
                  width=70,
                  font=("Arial", 11))

input_text.pack(pady=5)

# Language Frame
frame = Frame(root, bg="#dff6ff")
frame.pack(pady=10)

languages = [
    "english",
    "tamil",
    "hindi",
    "telugu",
    "malayalam",
    "french",
    "german",
    "spanish"
]

# Source Language
source_label = Label(frame,
                     text="Source Language",
                     font=("Arial", 11, "bold"),
                     bg="#dff6ff")

source_label.grid(row=0, column=0, padx=20)

source_lang = ttk.Combobox(frame,
                           values=languages,
                           width=15)

source_lang.grid(row=1, column=0)
source_lang.set("english")

# Target Language
target_label = Label(frame,
                     text="Target Language",
                     font=("Arial", 11, "bold"),
                     bg="#dff6ff")

target_label.grid(row=0, column=1, padx=20)

target_lang = ttk.Combobox(frame,
                           values=languages,
                           width=15)

target_lang.grid(row=1, column=1)
target_lang.set("tamil")

# Translate Button
translate_btn = Button(root,
                       text="Translate",
                       font=("Arial", 12, "bold"),
                       bg="green",
                       fg="white",
                       padx=10,
                       pady=5,
                       command=translate_text)

translate_btn.pack(pady=15)

# Output Label
output_label = Label(root,
                     text="Translated Text",
                     font=("Arial", 12, "bold"),
                     bg="#dff6ff")

output_label.pack()

# Output Box
output_text = Text(root,
                   height=8,
                   width=70,
                   font=("Arial", 11))

output_text.pack(pady=5)

# Run App
root.mainloop()