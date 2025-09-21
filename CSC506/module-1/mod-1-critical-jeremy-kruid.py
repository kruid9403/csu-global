def search(query, data):
    for item in data:
        print(f"Searching for '{query}' in '{item}'")
        if query.lower() == item.lower():
            return item
    return "Not Found"

print(f"Found: {search("Jeremy Kruid", ["Alice Smith", "Jeremy Kruid", "Bob Johnson"])}")