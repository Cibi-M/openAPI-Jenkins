import json
import sys
import difflib
from pathlib import Path

def load_json(file_path):
    try:
        with open(file_path) as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error loading {file_path}: {e}")
        sys.exit(1)

def compare_json(file1, file2):
    data1 = load_json(file1)
    data2 = load_json(file2)

    if data1 == data2:
        print("✅ Validation Passed: Both JSON files are identical.")
        sys.exit(0)
    else:
        print("❌ Validation Failed: JSON files differ.")
        diff = difflib.unified_diff(
            json.dumps(data1, indent=2, sort_keys=True).splitlines(),
            json.dumps(data2, indent=2, sort_keys=True).splitlines(),
            fromfile=file1,
            tofile=file2,
            lineterm=""
        )
        for line in diff:
            print(line)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate_with_readme.py <file1> <file2>")
        sys.exit(1)

    file1, file2 = sys.argv[1], sys.argv[2]
    if not Path(file1).exists() or not Path(file2).exists():
        print("❌ One or both JSON files do not exist.")
        sys.exit(1)

    compare_json(file1, file2)
