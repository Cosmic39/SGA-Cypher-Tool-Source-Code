import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from backend import encrypt_message, decrypt_message

def main():
    root = tk.Tk()
    root.title("🧙 Minecraft SGA Cipher Tool        Developer: Cosmic")
    root.geometry("600x500")

    # Mode selection
    mode_var = tk.StringVar(value="encrypt")
    mode_frame = ttk.LabelFrame(root, text="Choose Mode")
    mode_frame.pack(fill="x", padx=10, pady=5)

    ttk.Radiobutton(mode_frame, text="Encrypt", variable=mode_var, value="encrypt").pack(side="left", padx=10, pady=5)
    ttk.Radiobutton(mode_frame, text="Decrypt", variable=mode_var, value="decrypt").pack(side="left", padx=10, pady=5)

    # Input panel
    ttk.Label(root, text="Input:").pack(anchor="w", padx=10, pady=2)
    input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=8)
    input_box.pack(padx=10, pady=5)

    # Keys
    keys_frame = ttk.Frame(root)
    keys_frame.pack(padx=10, pady=5, fill="x")

    ttk.Label(keys_frame, text="Caesar Key:").grid(row=0, column=0, padx=5, pady=2, sticky="e")
    key_entry = ttk.Entry(keys_frame, width=10)
    key_entry.grid(row=0, column=1, padx=5, pady=2, sticky="w")

    ttk.Label(keys_frame, text="Seed (min 8 chars):").grid(row=0, column=2, padx=5, pady=2, sticky="e")
    seed_entry = ttk.Entry(keys_frame, width=25)
    seed_entry.grid(row=0, column=3, padx=5, pady=2, sticky="w")

    # Output panel
    ttk.Label(root, text="Output:").pack(anchor="w", padx=10, pady=2)
    output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=8, state="disabled")
    output_box.pack(padx=10, pady=5)

    # Track failed attempts
    failed_attempts = {"count": 0}

    # Function
    def run_cipher():
        text = input_box.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Error", "Please enter text to process.")
            return

        try:
            key = int(key_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Caesar key must be a number.")
            return

        seed = seed_entry.get().strip()
        if len(seed) < 8:
            messagebox.showerror("Error", "Seed must be at least 8 characters long.")
            return

        try:
            if mode_var.get() == "encrypt":
                result = encrypt_message(text, key, seed)
            else:
                result = decrypt_message(text, key, seed)
        except Exception as e:
            failed_attempts["count"] += 1
            if failed_attempts["count"] >= 10:
                messagebox.showerror("Error", "❌ Too many failed attempts! Application will close.")
                root.destroy()
                return
            else:
                messagebox.showerror(
                    "Error",
                    f"Cipher failed: {e}\nFailed attempts: {failed_attempts['count']}/10"
                )
            return

        # Reset failed attempts on success
        failed_attempts["count"] = 0

        output_box.config(state="normal")
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)
        output_box.config(state="disabled")

    # Run button
    ttk.Button(root, text="Run", command=run_cipher).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
