# Log file reader program
from pathlib import Path

filename = input("Enter log filename (for example sample.log): ")
path = Path(filename)

try:
    with path.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    print(f"Total log entries: {len(lines)}")
    keyword = input("Enter keyword to find (or press Enter to show all): ").strip().lower()

    for line_number, line in enumerate(lines, start=1):
        if not keyword or keyword in line.lower():
            print(f"{line_number}: {line.rstrip()}")
except FileNotFoundError:
    print("File not found. Check the filename and try again.")
