from typing import List, Tuple

pages: List[str] = [
    "List Overview",
    "Add / Edit List",
    "Shopping List (Items)",
    "Item Detail / Edit",
    "Integration Settings"
]

flow: List[Tuple[str, str]] = [
    ("List Overview", "Add / Edit List"),
    ("List Overview", "Shopping List (Items)"),
    ("Shopping List (Items)", "Item Detail / Edit"),
    ("List Overview", "Integration Settings")
]

def print_overview() -> None:
    print("=== Prototype Pages ===")
    for i, page in enumerate(pages, 1):
        print(f"{i}. {page}")
    print(f"\nTotal pages: {len(pages)}")

    print("\n=== Navigation Flow ===")
    for src, dst in flow:
        print(f"{src}  -->  {dst}")

if __name__ == "__main__":
    print_overview()
