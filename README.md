# 🧙 SGA Cipher Tool (Source Code)

A standalone **desktop application** for encrypting and decrypting messages using a mix of:

* **Caesar Cipher** (shift-based encryption)
* **Minecraft’s Standard Galactic Alphabet (SGA)** with a seed-based map

Built by **Cosmic**, packaged into a portable `.exe`.
No Python installation required — just download and run.

---

## 📂 Project Structure

```
minecraft-sga-cipher/
│
├── backend/                # Core encryption/decryption logic
│   ├── __init__.py
│   └── cipher.py           # Caesar + SGA + seed mapping
│
├── gui/                    # Graphical User Interface
│   ├── __init__.py
│   └── app.py              # Tkinter-based GUI
│
├── tests/                  # Unit tests (optional, dev use only)
│   └── test_cipher.py
│
├── main.py                 # Entry point (runs GUI)
├── setup.py                # Packaging for pip install
├── requirements.txt        # Dependencies (minimal)
├── README.md               # This file (dev-only documentation)
└── .gitignore              # Ignore build/dist/__pycache__
```

---

## 🚀 Development Setup

1. Clone the repo (private):

   ```bash
   git clone <private_repo_url>
   cd minecraft-sga-cipher
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate     # Linux/macOS
   .\env\Scripts\activate      # Windows
   ```

3. Install requirements:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app in dev mode:

   ```bash
   python main.py
   ```

---

## 🏗️ Building the Application

To package into a standalone `.exe`:

```bash
pyinstaller --onefile --noconsole --name "SGA-Cipher" --icon=assets/icon.ico main.py
```

* Output `.exe` → `dist/SGA-Cipher.exe`
* Clean build folders before rebuild:

  ```bash
  rmdir /s /q build dist
  ```

---

## 🔑 Security Notes

* The **SGA seed mapping** is generated from the user-provided seed.
* Seeds must be at least **8 characters**.
* The GUI enforces a **10 failed attempts lockout** to reduce brute force attempts.

---

## 👤 Author

Developed by **Cosmic**

* Public release repo: *(binary-only, no source)*
* Private repo (this one): contains full source code for personal/development use
