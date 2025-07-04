# TAP – File Integrity Checker v1.0

**Author:** Princess Ayeni, T.  
**Company:** ShieldStack Africa  
**License:** MIT  
**Version:** 1.0  

---

## 🔐 About TAP

TAP (Trust. Audit. Protect.) is a simple SHA256-based file integrity checker.  
It helps detect unauthorized changes by monitoring the hash values of files in any directory.

---

## ⚙️ Features

- 🧾 Generate a hash baseline of files in a folder
- 🔍 Compare current file states to the original baseline
- 📁 Recursive scan (includes subfolders)
- 📤 Export and re-use reports

---

## 💻 How to Use

### 1. Create a baseline hash report:

```bash
python tap.py --scan /your/folder --output baseline.txt
