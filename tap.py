import os
import hashlib
import argparse
import pyfiglet

def calculate_file_hash(filepath):
    """Calculate SHA256 hash of a file"""
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def scan_directory(directory):
    """Scan all files in a directory recursively and return dict of hashes"""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hashes[filepath] = calculate_file_hash(filepath)
    return file_hashes

def save_hashes(hashes, output_file):
    """Save file hashes to a file"""
    with open(output_file, 'w') as f:
        for path, hash in hashes.items():
            f.write(f"{path}::{hash}\n")

def load_hashes(file_path):
    """Load file hashes from a previously saved file"""
    hashes = {}
    with open(file_path, 'r') as f:
        for line in f:
            if "::" in line:
                path, hash = line.strip().split("::")
                hashes[path] = hash
    return hashes

def compare_hashes(old, new):
    print("\n[+] Comparing file hashes for integrity...\n")

    old_paths = set(old.keys())
    new_paths = set(new.keys())

    added = new_paths - old_paths
    deleted = old_paths - new_paths
    changed = {path for path in old_paths & new_paths if old[path] != new[path]}

    if changed:
        print("🟡 Changed files:")
        for path in changed:
            print(f"  * {path}")
    if deleted:
        print("\n🔴 Deleted files:")
        for path in deleted:
            print(f"  - {path}")
    if added:
        print("\n🟢 Added files:")
        for path in added:
            print(f"  + {path}")

    if not changed and not deleted and not added:
        print("✅ No changes detected. All files are intact.")

if __name__ == "__main__":
    # Show banner
    ascii_banner = pyfiglet.figlet_format("TAP v1.0")
    print(ascii_banner)
    print("File Integrity Checker by Princess Ayeni, T. | ShieldStack Africa\n")

    parser = argparse.ArgumentParser(description="TAP - File Integrity Checker")
    parser.add_argument("--scan", help="Path to scan for files")
    parser.add_argument("--output", help="Output file to save hash baseline")
    parser.add_argument("--compare", help="Compare current hashes with this file")

    args = parser.parse_args()

    if args.scan:
        current_hashes = scan_directory(args.scan)

        if args.output:
            save_hashes(current_hashes, args.output)
            print(f"\n✅ Baseline hashes saved to {args.output}")

        if args.compare:
            baseline_hashes = load_hashes(args.compare)
            compare_hashes(baseline_hashes, current_hashes)

    else:
        print("⚠️ Please provide a directory to scan using --scan")
