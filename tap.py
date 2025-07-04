# tap.py
__version__ = "1.0"
__author__ = "Princess Ayeni, T. (ShieldStack Africa)"

import os
import hashlib
import argparse

def hash_file(filepath):
    """Generate SHA256 hash for a given file."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        return f"ERROR: {e}"

def scan_directory(path):
    """Scan directory and return dictionary of file paths and hashes."""
    file_hashes = {}
    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            file_hashes[full_path] = hash_file(full_path)
    return file_hashes

def save_hash_report(file_hashes, output_path):
    """Save hashes to a file."""
    with open(output_path, 'w') as f:
        for filepath, hash in file_hashes.items():
            f.write(f"{filepath}|{hash}\n")
    print(f"[+] Baseline saved to {output_path}")

def load_hash_report(baseline_path):
    """Load a saved hash report file."""
    baseline_hashes = {}
    with open(baseline_path, 'r') as f:
        for line in f:
            if '|' in line:
                filepath, hash = line.strip().split('|')
                baseline_hashes[filepath] = hash
    return baseline_hashes

def compare_hashes(old, new):
    """Compare old vs new hashes and detect changes."""
    print("\n[+] Comparing file hashes for integrity...\n")

    old_files = set(old.keys())
    new_files = set(new.keys())

    added = new_files - old_files
    deleted = old_files - new_files
    common = old_files & new_files

    changed = []

    for file in common:
        if old[file] != new[file]:
            changed.append(file)

    if added:
        print("🟢 Added files:")
        for f in added:
            print(f"  + {f}")

    if deleted:
        print("🔴 Deleted files:")
        for f in deleted:
            print(f"  - {f}")

    if changed:
        print("🟡 Changed files:")
        for f in changed:
            print(f"  * {f}")

    if not added and not deleted and not changed:
        print("✅ No changes detected.")

if __name__ == "__main__":
        print("\n" + "═" * 60)
    print("      TAP - FILE INTEGRITY CHECKER v1.0")
    print("      Developed by Princess Ayeni, T.")
    print("      Powered by ShieldStack Africa")
    print("═" * 60 + "\n")

    parser = argparse.ArgumentParser(
        description="TAP - File Integrity Checker v1.0 | ShieldStack Africa | Developed by Princess Ayeni, T."
    )
    parser.add_argument('--scan', help='Directory to scan')
    parser.add_argument('--output', help='Save baseline hash report to file')
    parser.add_argument('--compare', help='Compare current scan to a saved hash report')

    args = parser.parse_args()

    if args.scan and args.output:
        hashes = scan_directory(args.scan)
        save_hash_report(hashes, args.output)

    elif args.scan and args.compare:
        baseline = load_hash_report(args.compare)
        current = scan_directory(args.scan)
        compare_hashes(baseline, current)

    else:
        parser.print_help()
