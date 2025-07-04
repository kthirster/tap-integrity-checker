import os
import hashlib
import pyfiglet
from termcolor import colored

def calculate_file_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def scan_directory(directory):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hashes[filepath] = calculate_file_hash(filepath)
    return file_hashes

def save_hashes(hashes, output_file):
    with open(output_file, 'w') as f:
        for path, hash in hashes.items():
            f.write(f"{path}::{hash}\n")

def load_hashes(file_path):
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
        print("✅ No changes detected. All files are intact.\n")

def show_menu():
    print("Please choose an option:")
    print("1. 🔍 Scan directory (smart save or compare)")
    print("2. 🔁 Manually compare with custom baseline file")
    print("3. ❌ Exit")

if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("TAP v1.0")
    print(colored(ascii_banner, color="magenta"))
    print(colored("Built by Princess Ayeni, T. | ShieldStack Africa\n", color="magenta"))

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            folder = input("Enter folder path to scan: ").strip()
            baseline_file = "baseline.txt"

            if os.path.exists(baseline_file):
                use_compare = input(
                    f"A baseline file '{baseline_file}' already exists. Do you want to compare instead? (y/n): "
                ).strip().lower()
                if use_compare == "y":
                    current_hashes = scan_directory(folder)
                    baseline_hashes = load_hashes(baseline_file)
                    compare_hashes(baseline_hashes, current_hashes)
                else:
                    current_hashes = scan_directory(folder)
                    save_hashes(current_hashes, baseline_file)
                    print(f"✅ New baseline saved to '{baseline_file}'\n")
            else:
                current_hashes = scan_directory(folder)
                save_hashes(current_hashes, baseline_file)
                print(f"✅ Baseline hashes saved to '{baseline_file}'\n")

        elif choice == "2":
            folder = input("Enter folder path to scan for comparison: ").strip()
            baseline_file = input("Enter saved baseline filename to compare against: ").strip()
            if not os.path.exists(baseline_file):
                print(f"❌ Error: '{baseline_file}' not found!\n")
                continue
            current_hashes = scan_directory(folder)
            baseline_hashes = load_hashes(baseline_file)
            compare_hashes(baseline_hashes, current_hashes)

        elif choice == "3":
            print("\n👋 Goodbye. Stay secure with TAP!")
            break

        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.\n")
