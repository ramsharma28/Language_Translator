import tkinter as tk
from googletrans import Translator, LANGUAGES
from translate import Translator as FallbackTranslator

class TranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.root.configure(bg="#ADD8E6")  # Set background color

        # Create and place widgets
        self.label1 = tk.Label(root, text="Enter text:", bg="#4CAF50", fg="white")
        self.label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.text_input = tk.Text(root, height=5, width=40)
        self.text_input.grid(row=1, column=0, padx=10, pady=10)

        self.label2 = tk.Label(root, text="From language:", bg="#4CAF50", fg="white")
        self.label2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.from_lang_var = tk.StringVar()
        self.from_lang_dropdown = tk.OptionMenu(root, self.from_lang_var, *LANGUAGES.values())
        self.from_lang_var.set("English")
        self.from_lang_dropdown.grid(row=3, column=0, padx=10, pady=10)

        self.label3 = tk.Label(root, text="To language:", bg="#4CAF50", fg="white")
        self.label3.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.to_lang_var = tk.StringVar()
        self.to_lang_dropdown = tk.OptionMenu(root, self.to_lang_var, *LANGUAGES.values())
        self.to_lang_var.set("Select a Language")
        self.to_lang_dropdown.grid(row=5, column=0, padx=10, pady=10)

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text, bg="#4CAF50", fg="white")
        self.translate_button.grid(row=6, column=0, padx=10, pady=20)

        self.translated_text = tk.Label(root, text="", wraplength=400, justify="center", bg="lightgrey", padx=10, pady=10)
        self.translated_text.grid(row=7, column=0, padx=10, pady=10, sticky="w")

    def translate_text(self):
        try:
            text = self.text_input.get("1.0", "end-1c")
            from_lang = self.from_lang_var.get()
            to_lang = self.to_lang_var.get()

            translator = Translator()
            translated = translator.translate(text, src=from_lang, dest=to_lang)

            self.translated_text.config(text=translated.text)

        except AttributeError:
            try:
                fallback_translator = FallbackTranslator(to_lang)
                translated_text = fallback_translator.translate(text)
                self.translated_text.config(text=translated_text)

            except Exception as e:
                print("Error occurred:", e)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslationApp(root)
    root.mainloop()