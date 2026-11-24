"""One-Star Review of Something Essential — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a deadpan one-star review, 160 characters or fewer, of an everyday essential.
"""
import os

LINE = "One star. The sun shows up every morning uninvited, glares at me through the window, and refuses to take a day off."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
