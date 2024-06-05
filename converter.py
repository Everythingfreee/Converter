import tkinter as tk
from tkinter import messagebox

def convert_to_numbers():
    sentence = input_text.get()
    numbers = [ord(char) for char in sentence]
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, ', '.join(map(str, numbers)))

def convert_to_characters():
    numbers_input = input_text.get()
    numbers_list = numbers_input.split(',')
    characters = ''.join(chr(int(number.strip())) for number in numbers_list)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, characters)

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(output_text.get(1.0, tk.END).strip())
    window.update()  # Now it stays on the clipboard after the window is closed
    messagebox.showinfo("Copy to Clipboard", "Text copied to clipboard.")

def paste_from_clipboard():
    input_text.delete(0, tk.END)
    input_text.insert(0, window.clipboard_get())

# Create the main window
window = tk.Tk()
window.title("Character Converter")

# Create a frame to center the widgets
frame = tk.Frame(window)
frame.pack(expand=True)

# Create paste button
paste_button = tk.Button(frame, text="Paste", command=paste_from_clipboard)
paste_button.grid(row=0, column=0, pady=10, padx=5, columnspan=2)

# Create input fields
input_text = tk.Entry(frame, width=30)
input_text.grid(row=1, column=0, pady=10, padx=5, columnspan=2)
input_text.bind("<Button-3>", lambda event: input_text.event_generate("<<Menu>>"))

# Create buttons
to_numbers_button = tk.Button(frame, text="Convert to Numbers", command=convert_to_numbers)
to_numbers_button.grid(row=2, column=0, padx=5, pady=5)

to_characters_button = tk.Button(frame, text="Convert to Characters", command=convert_to_characters)
to_characters_button.grid(row=2, column=1, padx=5, pady=5)

# Create output fields
output_text = tk.Text(frame, width=30, height=10)
output_text.grid(row=3, column=0, columnspan=2, pady=10)
output_text.bind("<Button-3>", lambda event: output_text.event_generate("<<Menu>>"))

# Set text direction using Unicode control characters
output_text.insert(tk.END, "\u202B")  # Right-to-Left Embedding (RLE)

# Create copy button
copy_button = tk.Button(frame, text="Copy Output", command=copy_to_clipboard)
copy_button.grid(row=4, column=0, columnspan=2, pady=5)

# Center the frame in the window
window.update_idletasks()
window.geometry(f"{frame.winfo_width()}x{frame.winfo_height()}+"
                f"{(window.winfo_screenwidth() // 2) - (frame.winfo_width() // 2)}+"
                f"{(window.winfo_screenheight() // 2) - (frame.winfo_height() // 2)}")

# Start the main event loop
window.mainloop()
