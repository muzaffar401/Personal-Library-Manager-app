import streamlit as st  # Import Streamlit for building the web app
import matplotlib.pyplot as plt  # Import Matplotlib for creating visualizations
import json  # Import JSON for handling data storage
import uuid  # Import UUID for generating unique IDs

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

# Load library data
library = load_library()

# Custom CSS for the book-like UI
st.markdown("""
    <style>
        .book-cover {
            border: 2px solid #8B4513;  /* Set border color */
            padding: 20px;  /* Add padding inside the book cover */
            border-radius: 10px;  /* Round the corners */
            background-color: #F5DEB3;  /* Set background color */
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);  /* Add shadow for depth */
            font-family: 'Georgia', serif;  /* Set font family */
            color: #4B3621;  /* Set text color */
            text-align: center;  /* Center-align text */
            margin-bottom: 20px;  /* Add margin at the bottom */
            position: relative;  /* Set position to relative for pseudo-elements */
        }
        .book-cover h4 {
            font-size: 24px;  /* Set font size for the title */
            margin-bottom: 10px;  /* Add margin below the title */
            font-weight: bold;  /* Make the title bold */
        }
        .book-cover p {
            font-size: 16px;  /* Set font size for paragraphs */
            margin: 5px 0;  /* Add margin around paragraphs */
        }
        .book-cover .read-status {
            font-size: 18px;  /* Set font size for read status */
            margin-top: 15px;  /* Add margin above the read status */
        }
        .book-cover .download-button {
            margin-top: 20px;  /* Add margin above the button */
            background-color: #8B4513;  /* Set button background color */
            color: white;  /* Set button text color */
            border: none;  /* Remove button border */
            padding: 10px 20px;  /* Add padding inside the button */
            border-radius: 5px;  /* Round the button corners */
            cursor: pointer;  /* Change cursor to pointer on hover */
            font-size: 16px;  /* Set button font size */
        }
        .book-cover .download-button:hover {
            background-color: #A0522D;  /* Change button color on hover */
        }
        .book-cover::before {
            content: '';  /* Add pseudo-element content */
            position: absolute;  /* Position the pseudo-element absolutely */
            top: 0;  /* Align to the top */
            left: 0;  /* Align to the left */
            right: 0;  /* Align to the right */
            bottom: 0;  /* Align to the bottom */
            background: linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(0, 0, 0, 0.1));  /* Add gradient overlay */
            border-radius: 10px;  /* Round the corners */
            pointer-events: none;  /* Ensure the overlay doesn't block clicks */
        }
    </style>
""", unsafe_allow_html=True)  # Allow unsafe HTML for custom CSS

# Streamlit UI
st.title("📚 Personal Library Manager")  # Set the title of the app
menu = ["Add a Book", "Remove a Book", "Search for a Book", "Update a Book", "Display All Books", "Statistics"]  # Define menu options
choice = st.sidebar.selectbox("Menu", menu)  # Create a sidebar menu for navigation

if choice == "Add a Book":
    st.subheader("➕ Add a New Book")  # Display a subheader for the "Add a Book" section
    title = st.text_input("Title")  # Input field for the book title
    author = st.text_input("Author")  # Input field for the book author
    year = st.number_input("Publication Year", min_value=1000, max_value=9999, step=1)  # Input field for the publication year
    genre = st.text_input("Genre")  # Input field for the book genre
    content = st.text_area("Book Content (Supports Markdown)")  # Text area for the book content
    read_status = st.checkbox("Have you read this book?")  # Checkbox for read status
    
    if st.button("Add Book"):  # Button to add the book
        if not title or not author or not genre or not content or not year:
             st.error("All fields are required!")  # Show error if any field is empty
        else:
            book_id = generate_id()  # Generate a unique 3-digit ID
            library.append({"id": book_id, "title": title, "author": author, "year": year, "genre": genre, "content": content, "read": read_status})  # Add the book to the library
            save_library(library)  # Save the updated library to the file
            st.success(f"Book added successfully! ID: {book_id}")  # Show success message

elif choice == "Remove a Book":
    st.subheader("🗑️ Remove a Book")  # Display a subheader for the "Remove a Book" section
    book_ids = {book['id']: book for book in library}  # Create a dictionary of book IDs and their details
    book_to_remove = st.selectbox("Select a book ID to remove", list(book_ids.keys()))  # Dropdown to select a book ID to remove
    
    if st.button("Remove Book"):  # Button to remove the book
        library = [book for book in library if book["id"] != book_to_remove]  # Filter out the book to remove
        save_library(library)  # Save the updated library to the file
        st.success("Book removed successfully!")  # Show success message

elif choice == "Search for a Book":
    st.subheader("🔍 Search for a Book")  # Display a subheader for the "Search for a Book" section
    search_term = st.text_input("Enter title, author, or ID")  # Input field for the search term
    
    if st.button("Search"):  # Button to search for the book
        if not search_term:
            st.error("Please enter a search term!")  # Show error if the search term is empty
        else:
            results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower() or search_term == book["id"]]  # Search for matching books
            if results:
                for book in results:
                    st.markdown(f"""
                    <div class="book-cover">
                        <h4>{book['title']}</h4>
                        <p><strong>Author:</strong> {book['author']}</p>
                        <p><strong>Year:</strong> {book['year']}</p>
                        <p><strong>Genre:</strong> {book['genre']}</p>
                        <p class="read-status"><strong>Read:</strong> {'✅ Read' if book['read'] else '❌ Unread'}</p>
                        <p><strong>ID:</strong> {book['id']}</p>
                        <div>{book['content']}</div>
                        <a href="data:text/plain;charset=utf-8,{book['content']}" download="{book['title']}.txt">
                            <button class="download-button">Download</button>
                        </a>
                    </div>
                    """, unsafe_allow_html=True)  # Display the book details with custom CSS
            else:
                st.warning("No matching books found!")  # Show warning if no books are found

elif choice == "Update a Book":
    st.subheader("✏️ Update a Book")  # Display a subheader for the "Update a Book" section
    book_id = st.text_input("Enter Book ID to update")  # Input field for the book ID to update
    book = next((book for book in library if book["id"] == book_id), None)  # Find the book by ID
    
    if book:
        with st.form("update_form"):  # Create a form for updating the book
            new_title = st.text_input("Title", book["title"])  # Input field for the new title
            new_author = st.text_input("Author", book["author"])  # Input field for the new author
            new_year = st.number_input("Publication Year", min_value=1000, max_value=9999, step=1, value=book["year"])  # Input field for the new publication year
            new_genre = st.text_input("Genre", book["genre"])  # Input field for the new genre
            new_content = st.text_area("Book Content (Supports Markdown)", book["content"])  # Text area for the new content
            new_read_status = st.checkbox("Have you read this book?", book["read"])  # Checkbox for the new read status
            submit_button = st.form_submit_button("Update Book")  # Button to submit the form
            
            if submit_button:
                if not new_title or not new_author or not new_genre or not new_content:
                    st.error("All fields are required!")  # Show error if any field is empty
                else:
                    book.update({"title": new_title, "author": new_author, "year": new_year, "genre": new_genre, "content": new_content, "read": new_read_status})  # Update the book details
                    save_library(library)  # Save the updated library to the file
                    st.success("Book updated successfully!")  # Show success message
    elif book_id:
        st.warning("Book not found!")  # Show warning if the book is not found

elif choice == "Display All Books":
    st.subheader("📖 Your Library")  # Display a subheader for the "Display All Books" section
    if library:
        for book in library:
            st.markdown(f"""
            <div class="book-cover">
                <h4>{book['title']}</h4>
                <p><strong>Author:</strong> {book['author']}</p>
                <p><strong>Year:</strong> {book['year']}</p>
                <p><strong>Genre:</strong> {book['genre']}</p>
                <p class="read-status"><strong>Read:</strong> {'✅ Read' if book['read'] else '❌ Unread'}</p>
                <p><strong>ID:</strong> {book['id']}</p>
                <div>{book['content']}</div>
                <a href="data:text/plain;charset=utf-8,{book['content']}" download="{book['title']}.txt">
                    <button class="download-button">Download</button>
                </a>
            </div>
            """, unsafe_allow_html=True)  # Display all books with custom CSS
    else:
        st.info("Your library is empty!")  # Show info if the library is empty

if choice == "Statistics":
    st.subheader("📊 Library Statistics")  # Display a subheader for the "Statistics" section
    total_books = len(library)  # Calculate the total number of books
    read_books = sum(1 for book in library if book["read"])  # Calculate the number of read books
    unread_books = total_books - read_books  # Calculate the number of unread books
    
    st.write(f"**Total books:** {total_books}")  # Display the total number of books
    st.write(f"**Read books:** {read_books}")  # Display the number of read books
    st.write(f"**Unread books:** {unread_books}")  # Display the number of unread books
    
    if total_books > 0:
        fig, ax = plt.subplots()  # Create a Matplotlib figure and axis
        ax.pie([read_books, unread_books], labels=["Read", "Unread"], autopct='%1.1f%%', colors=['#8B4513', '#F5DEB3'], startangle=90)  # Create a pie chart
        ax.axis("equal")  # Ensure the pie chart is circular
        st.pyplot(fig)  # Display the pie chart in the app
    else:
        st.info("No books in the library to display statistics.")  # Show info if the library is empty