# Personal Library Manager

## 📖 Overview
The **Personal Library Manager** is a Streamlit-based web application that helps users organize, manage, and track their personal book collection. Users can add, remove, search, update, and display books in their library, as well as view reading statistics.

## 🚀 Features
- **Add Books:** Store book details such as title, author, year, genre, and content.
- **Remove Books:** Delete books from the library using their unique ID.
- **Search Books:** Find books by title, author, or unique ID.
- **Update Books:** Modify book details.
- **Display All Books:** View all stored books with a book-like UI.
- **Statistics:** View a pie chart showing the ratio of read vs. unread books.
- **Download Content:** Export book content as a `.txt` file.
- **Persistent Storage:** Uses a JSON file to save library data.

## 🛠️ Installation & Setup
This project uses **uv** for dependency management. Follow these steps to set up and run the project:

### 1️⃣ Initialize the Project
```sh
uv init
```

### 2️⃣ Install Dependencies
```sh
uv add streamlit matplotlib
```

### 3️⃣ Run the Application
```sh
streamlit run library_manager.py
```

## 📂 Project Structure
```
📁 Personal Library Manager
├── 📄 library_manager.py  # Main Streamlit app
├── 📄 library.json        # JSON file storing book data
├── 📄 README.md           # Project documentation
```

## 🎨 UI Design
The application features a **book-themed** UI with:
- Soft brown and beige color themes.
- Book covers styled with CSS.
- Markdown support for book content.

## 📊 Statistics
- Displays the **total number of books**.
- Shows a **pie chart** of read vs. unread books.

## 📌 Future Enhancements
- Implement book categorization.
- Integrate a cloud database for better data storage.
- Add book cover images.

## 🎯 Conclusion
The **Personal Library Manager** is an easy-to-use application that helps users maintain their book collection efficiently. Its **interactive UI**, **simple storage mechanism**, and **visual statistics** make it a great tool for book lovers.

---
💡 Built with ❤️ using **Streamlit & Python**

