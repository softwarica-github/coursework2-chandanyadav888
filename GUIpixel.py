import tkinter as tk
from tkinter import filedialog, messagebox
import secret_pixel

class SecretPixelGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("SecretPixel - Steganography Tool")

        self.label = tk.Label(master, text="Select an operation:")
        self.label.pack()

        self.hide_button = tk.Button(master, text="Hide File", command=self.hide_file)
        self.hide_button.pack()

        self.extract_button = tk.Button(master, text="Extract File", command=self.extract_file)
        self.extract_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def hide_file(self):
        host_file = filedialog.askopenfilename(title="Select Host Image")
        if host_file:
            secret_file = filedialog.askopenfilename(title="Select Secret File")
            if secret_file:
                output_file = filedialog.asksaveasfilename(title="Save Output Image As")
                if output_file:
                    public_key = filedialog.askopenfilename(title="Select Public Key")
                    if public_key:
                        try:
                            secret_pixel.hide_file_in_png(host_file, secret_file, output_file, public_key)
                            messagebox.showinfo("Success", "File hidden successfully!")
                        except Exception as e:
                            messagebox.showerror("Error", str(e))

    def extract_file(self):
        carrier_file = filedialog.askopenfilename(title="Select Carrier Image")
        if carrier_file:
            output_file = filedialog.asksaveasfilename(title="Save Extracted File As")
            if output_file:
                private_key = filedialog.askopenfilename(title="Select Private Key")
                if private_key:
                    try:
                        secret_pixel.extract_file_from_png(carrier_file, output_file, private_key)
                        messagebox.showinfo("Success", "File extracted successfully!")
                    except Exception as e:
                        messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = SecretPixelGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
