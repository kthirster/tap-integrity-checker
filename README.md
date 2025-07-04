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
###  Download the Tool

From GitHub:

- Click the green `Code` button
- Select `Download ZIP`
- Unzip it on your computer


Run TAP to Create a Baseline Hash

Create a test folder and add some files:
```bash
mkdir test-files
echo "Hello Princess" > test-files/file1.txt
echo "Security is power" > test-files/file2.txt
```
TAP runs on Python 3.8+
Check with:
```bash
python --version
```
This tool is part of the ShieldStack Africa Security Toolkit
Built with love by Princess Ayeni, T.
