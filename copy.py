import shutil
from pathlib import Path

def organize_milk_files(list_file_path):
    SOURCE_ROOT = Path("/usr/share/projectM/presets/cream-of-the-crop/")
    TARGET_DIR = Path.home() / "milk" / "files"

    if not TARGET_DIR.exists():
        TARGET_DIR.mkdir(parents=True)

    # Read lines, strip whitespace, and filter out empty lines
    with open(list_file_path, "r", encoding="utf-8") as f:
        # We store them in a set for O(1) lookup
        files_to_find = {line.strip() for line in f if line.strip()}

    print(f"Searching for {len(files_to_find)} files...")

    # Recursively find all .milk files in the source directory
    # rglob handles the recursion automatically
    for found_path in SOURCE_ROOT.rglob("*.milk"):
        # Check if the filename exists in our target set
        if found_path.name in files_to_find:
            dest_path = TARGET_DIR / found_path.name

            try:
                shutil.copy2(found_path, dest_path)
                print(f"Successfully copied: {found_path.name}")
                files_to_find.remove(found_path.name)

            except Exception as e:
                print(f"Error copying {found_path.name}: {e}")

    # Report what wasn't found
    if files_to_find:
        print(f"\n--- Missing Files ({len(files_to_find)}) ---")
        for missing in files_to_find:
            print(f"Not found: {missing}")

if __name__ == "__main__":
    # Ensure this points to your text file
    organize_milk_files("milk.txt")