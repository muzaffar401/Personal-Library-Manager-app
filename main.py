import streamlit as st
import matplotlib.pyplot as plt
import json
import uuid

# File to store library data
LIBRARY_FILE = "library.json"

# Load library from file
def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Generate a 3-digit unique ID
def generate_id():
    return str(uuid.uuid4().int)[:3]

# Load library data
library = load_library()

# Custom CSS for the book-like UI
st.markdown("""
    <style>
        .book-cover {
            border: 2px solid #8B4513;
            padding: 20px;
            border-radius: 10px;
            background-color: #F5DEB3;
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
            font-family: 'Georgia', serif;
            color: #4B3621;
            text-align: center;
            margin-bottom: 20px;
            position: relative;
        }
        .book-cover h4 {
            font-size: 24px;
            margin-bottom: 10px;
            font-weight: bold;
        }
        .book-cover p {
            font-size: 16px;
            margin: 5px 0;
        }
        .book-cover .read-status {
            font-size: 18px;
            margin-top: 15px;
        }
        .book-cover .download-button {
            margin-top: 20px;
            background-color: #8B4513;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        .book-cover .download-button:hover {
            background-color: #A0522D;
        }
        .book-cover::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(0, 0, 0, 0.1));
            border-radius: 10px;
            pointer-events: none;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("📚 Personal Library Manager")
menu = ["Add a Book", "Remove a Book", "Search for a Book", "Update a Book", "Display All Books", "Statistics"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add a Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=1000, max_value=9999, step=1)
    genre = st.text_input("Genre")
    content = st.text_area("Book Content (Supports Markdown)")
    read_status = st.checkbox("Have you read this book?")
    
    if st.button("Add Book"):
        if not title or not author or not genre or not content or not year:
             st.error("All fields are required!")
        else:
            book_id = generate_id()  # Generate unique 3-digit ID
            library.append({"id": book_id, "title": title, "author": author, "year": year, "genre": genre, "content": content, "read": read_status})
            save_library(library)
            st.success(f"Book added successfully! ID: {book_id}")

elif choice == "Remove a Book":
    st.subheader("🗑️ Remove a Book")
    book_ids = {book['id']: book for book in library}
    book_to_remove = st.selectbox("Select a book ID to remove", list(book_ids.keys()))
    
    if st.button("Remove Book"):
        library = [book for book in library if book["id"] != book_to_remove]
        save_library(library)
        st.success("Book removed successfully!")

elif choice == "Search for a Book":
    st.subheader("🔍 Search for a Book")
    search_term = st.text_input("Enter title, author, or ID")
    
    if st.button("Search"):
        if not search_term:
            st.error("Please enter a search term!")
        else:
            results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower() or search_term == book["id"]]
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
                    """, unsafe_allow_html=True)
            else:
                st.warning("No matching books found!")

elif choice == "Update a Book":
    st.subheader("✏️ Update a Book")
    book_id = st.text_input("Enter Book ID to update")
    book = next((book for book in library if book["id"] == book_id), None)
    
    if book:
        with st.form("update_form"):
            new_title = st.text_input("Title", book["title"])
            new_author = st.text_input("Author", book["author"])
            new_year = st.number_input("Publication Year", min_value=1000, max_value=9999, step=1, value=book["year"])
            new_genre = st.text_input("Genre", book["genre"])
            new_content = st.text_area("Book Content (Supports Markdown)", book["content"])
            new_read_status = st.checkbox("Have you read this book?", book["read"])
            submit_button = st.form_submit_button("Update Book")
            
            if submit_button:
                if not new_title or not new_author or not new_genre or not new_content:
                    st.error("All fields are required!")
                else:
                    book.update({"title": new_title, "author": new_author, "year": new_year, "genre": new_genre, "content": new_content, "read": new_read_status})
                    save_library(library)
                    st.success("Book updated successfully!")
    elif book_id:
        st.warning("Book not found!")

elif choice == "Display All Books":
    st.subheader("📖 Your Library")
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
            """, unsafe_allow_html=True)
    else:
        st.info("Your library is empty!")

if choice == "Statistics":
    st.subheader("📊 Library Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    unread_books = total_books - read_books
    
    st.write(f"**Total books:** {total_books}")
    st.write(f"**Read books:** {read_books}")
    st.write(f"**Unread books:** {unread_books}")
    
    if total_books > 0:
        fig, ax = plt.subplots()
        ax.pie([read_books, unread_books], labels=["Read", "Unread"], autopct='%1.1f%%', colors=['#8B4513', '#F5DEB3'], startangle=90)
        ax.axis("equal")  # Equal aspect ratio ensures the pie chart is circular.
        st.pyplot(fig)
    else:
        st.info("No books in the library to display statistics.")