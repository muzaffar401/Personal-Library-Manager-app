import json  # Import the json module to work with JSON data
import uuid  # Import the uuid module to generate unique IDs
import argparse  # Import the argparse module to handle command-line arguments

# File to store library data
LIBRARY_FILE = "library.json"

# Load library from file
def load_library():
    try:
        # Open the library file in read mode
        with open(LIBRARY_FILE, "r") as file:
            # Load the JSON data from the file and convert it to a Python list
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file does not exist or is empty/invalid, return an empty list
        return []

# Save library to file
def save_library(library):
    # Open the library file in write mode
    with open(LIBRARY_FILE, "w") as file:
        # Convert the library list to JSON and write it to the file with indentation for readability
        json.dump(library, file, indent=4)

# Generate a 3-digit unique ID
def generate_id():
    # Generate a UUID, convert it to an integer, and take the first 3 digits as the ID
    return str(uuid.uuid4().int)[:3]

# Function to get non-empty input
def get_non_empty_input(prompt):
    while True:
        # Prompt the user for input and strip any leading/trailing whitespace
        value = input(prompt).strip()
        if value:  # If the input is not empty
            return value  # Return the valid input
        # If the input is empty, show an error message and prompt again
        print("Error: This field cannot be blank. Please try again.")

# Function to get valid year input
def get_valid_year(prompt):
    while True:
        # Prompt the user for input and strip any leading/trailing whitespace
        year = input(prompt).strip()
        if year and year.isdigit():  # Check if the input is a valid number
            return int(year)  # Convert the input to an integer and return it
        # If the input is invalid, show an error message and prompt again
        print("Error: Publication year must be a valid number. Please try again.")

# Add a new book
def add_book():
    # Get the book title from the user (non-empty)
    title = get_non_empty_input("Enter the title of the book: ")
    # Get the book author from the user (non-empty)
    author = get_non_empty_input("Enter the author of the book: ")
    # Get the publication year from the user (valid number)
    year = get_valid_year("Enter the publication year of the book: ")
    # Get the book genre from the user (non-empty)
    genre = get_non_empty_input("Enter the genre of the book: ")
    # Get the book content from the user (non-empty)
    content = get_non_empty_input("Enter the content of the book: ")
    # Ask if the user has read the book and convert the response to a boolean
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"

    # Load the existing library
    library = load_library()
    # Generate a unique ID for the new book
    book_id = generate_id()
    # Add the new book to the library
    library.append({
        "id": book_id,
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "content": content,
        "read": read_status
    })
    # Save the updated library to the file
    save_library(library)
    # Notify the user that the book has been added successfully
    print(f"Book added successfully! ID: {book_id}")

# Remove a book
def remove_book():
    # Get the ID of the book to remove from the user
    book_id = input("Enter the ID of the book to remove: ")
    # Load the existing library
    library = load_library()
    # Track the initial number of books in the library
    initial_count = len(library)
    # Filter out the book with the given ID
    library = [book for book in library if book["id"] != book_id]
    # Check if a book was actually removed
    if len(library) < initial_count:
        # Save the updated library to the file
        save_library(library)
        # Notify the user that the book has been removed successfully
        print("Book removed successfully!")
    else:
        # If no book was removed, notify the user that the book was not found
        print("Book not found!")

# Search for a book
def search_book():
    # Get the search term from the user (title, author, or ID)
    search_term = input("Enter the title, author, or ID to search: ").strip()
    if not search_term:  # If the search term is blank
        # Notify the user that no book was found
        print("Book not found!")
        return

    # Load the existing library
    library = load_library()
    # Search for books that match the search term in title, author, or ID
    results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower() or search_term == book["id"]]
    if results:
        # If matching books are found, display their details
        for book in results:
            print(f"""
            Title: {book['title']}
            Author: {book['author']}
            Year: {book['year']}
            Genre: {book['genre']}
            Read: {'✅ Read' if book['read'] else '❌ Unread'}
            ID: {book['id']}
            Content: {book['content']}
            """)
    else:
        # If no matching books are found, notify the user
        print("No matching books found!")

# Update a book
def update_book():
    # Get the ID of the book to update from the user
    book_id = input("Enter the ID of the book to update: ")
    # Load the existing library
    library = load_library()
    # Find the book with the given ID
    book = next((book for book in library if book["id"] == book_id), None)
    if book:
        # If the book is found, display its current details and prompt for updates
        print(f"Current Title: {book['title']}")
        title = get_non_empty_input("Enter the new title (or press Enter to keep current): ") or book["title"]
        print(f"Current Author: {book['author']}")
        author = get_non_empty_input("Enter the new author (or press Enter to keep current): ") or book["author"]
        print(f"Current Year: {book['year']}")
        year = get_valid_year("Enter the new publication year (or press Enter to keep current): ") or book["year"]
        print(f"Current Genre: {book['genre']}")
        genre = get_non_empty_input("Enter the new genre (or press Enter to keep current): ") or book["genre"]
        print(f"Current Content: {book['content']}")
        content = get_non_empty_input("Enter the new content (or press Enter to keep current): ") or book["content"]
        print(f"Current Read Status: {'Read' if book['read'] else 'Unread'}")
        read_status = input("Mark as read? (yes/no): ").lower() == "yes"

        # Update the book's details
        book.update({
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "content": content,
            "read": read_status
        })
        # Save the updated library to the file
        save_library(library)
        # Notify the user that the book has been updated successfully
        print("Book updated successfully!")
    else:
        # If the book is not found, notify the user
        print("Book not found!")

# Display all books
def display_all_books():
    # Load the existing library
    library = load_library()
    if library:
        # If the library is not empty, display details of all books
        for book in library:
            print(f"""
            Title: {book['title']}
            Author: {book['author']}
            Year: {book['year']}
            Genre: {book['genre']}
            Read: {'✅ Read' if book['read'] else '❌ Unread'}
            ID: {book['id']}
            Content: {book['content']}
            """)
    else:
        # If the library is empty, notify the user
        print("Your library is empty!")

# Display library statistics
def display_statistics():
    # Load the existing library
    library = load_library()
    # Calculate the total number of books
    total_books = len(library)
    # Calculate the number of read books
    read_books = sum(1 for book in library if book["read"])

    # Calculate the percentage of read books
    if total_books > 0:
        read_percentage = (read_books / total_books) * 100
    else:
        read_percentage = 0

    # Display the total number of books and the percentage of read books
    print(f"Total books: {total_books}")
    print(f"Percentage read: {read_percentage:.1f}%")

# Main function to handle CLI
def main():
    # Create an argument parser to handle command-line arguments
    parser = argparse.ArgumentParser(description="Personal Library Manager")
    # Add subparsers for different commands (add, remove, search, update, display, stats)
    subparsers = parser.add_subparsers(dest="command")

    # Add a book command
    add_parser = subparsers.add_parser("add", help="Add a new book")

    # Remove a book command
    remove_parser = subparsers.add_parser("remove", help="Remove a book")

    # Search for a book command
    search_parser = subparsers.add_parser("search", help="Search for a book")

    # Update a book command
    update_parser = subparsers.add_parser("update", help="Update a book")

    # Display all books command
    display_parser = subparsers.add_parser("display", help="Display all books")

    # Display statistics command
    stats_parser = subparsers.add_parser("stats", help="Display library statistics")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Execute the corresponding function based on the command
    if args.command == "add":
        add_book()
    elif args.command == "remove":
        remove_book()
    elif args.command == "search":
        search_book()
    elif args.command == "update":
        update_book()
    elif args.command == "display":
        display_all_books()
    elif args.command == "stats":
        display_statistics()
    else:
        # If no valid command is provided, display the help message
        parser.print_help()

# Entry point of the program
if __name__ == "__main__":
    main()