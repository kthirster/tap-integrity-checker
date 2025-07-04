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


Open Terminal or Command Prompt

Use cd to navigate to the extracted folder:
```bash
cd path/to/tap-integrity-checker
```
TAP runs on Python 3.8+
Check with:
```bash
python --version
```
Run the Tool 

```bash
python tap.py
```
Create Files & Use the Tool

```bash
mkdir test-files

   ```
 Add some files:

```bash
echo "Hello Princess" > test-files/file1.txt
echo "Security is power" > test-files/file2.txt
```
  Create a baseline:

```bash
python tap.py --scan test-files --output baseline.txt

```

Modify or delete a file:


```bash
echo "Tampered data" > test-files/file1.txt
rm test-files/file2.txt

```
  Compare:


```bash
python tap.py --scan test-files --compare baseline.txt

```




This tool is part of the ShieldStack Africa Security Toolkit
Built with love by Princess Ayeni, T.
