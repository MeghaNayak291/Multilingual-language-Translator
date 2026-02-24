import tkinter as tk
from tkinter import ttk, messagebox
from translate import Translator

# Language dictionary (Language Name : Code)
languages = {
    "English": "en",
    "Kannada": "kn",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Russian": "ru"
}

# Translate function
def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    
    if text == "":
        messagebox.showwarning("Warning", "Please enter some text!")
        return
    
    source_lang = languages[source_combo.get()]
    target_lang = languages[target_combo.get()]
    
    try:
        translator = Translator(from_lang=source_lang, to_lang=target_lang)
        translated = translator.translate(text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Window
root = tk.Tk()
root.title("🌍 Universal Language Translator")
root.geometry("700x500")
root.resizable(False, False)

# Source Language
tk.Label(root, text="From:", font=("Arial", 12)).pack(pady=5)
source_combo = ttk.Combobox(root, values=list(languages.keys()), state="readonly")
source_combo.pack()
source_combo.set("English")

# Target Language
tk.Label(root, text="To:", font=("Arial", 12)).pack(pady=5)
target_combo = ttk.Combobox(root, values=list(languages.keys()), state="readonly")
target_combo.pack()
target_combo.set("Kannada")

# Input Text
tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack(pady=5)
input_text = tk.Text(root, height=5, width=70)
input_text.pack()

# Translate Button
tk.Button(root, text="Translate", font=("Arial", 12), command=translate_text).pack(pady=10)

# Output Text
tk.Label(root, text="Translated Text:", font=("Arial", 12)).pack(pady=5)
output_text = tk.Text(root, height=5, width=70)
output_text.pack()

root.mainloop()