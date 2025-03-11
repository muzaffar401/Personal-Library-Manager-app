# Personal Library Manager

## 📖 Overview
The **Personal Library Manager** is a Python-based application that helps users organize, manage, and track their personal book collection. Users can interact with it using either a **Streamlit web UI** or a **Command-Line Interface (CLI)**.

## 🚀 Features
- **Add Books:** Store book details such as title, author, year, genre, and content.
- **Remove Books:** Delete books from the library using their unique ID.
- **Search Books:** Find books by title, author, or unique ID.
- **Update Books:** Modify book details.
- **Display All Books:** View all stored books.
- **Statistics:** View a pie chart (in Streamlit) and a summary (in CLI) showing read vs. unread books.
- **Download Content:** Export book content as a `.txt` file.
- **Persistent Storage:** Uses a JSON file to save library data.

---

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

---

## 🎨 UI Options
### 1️⃣ **Run as a Web Application (Streamlit)**
To use the book manager with an interactive web UI:
```sh
streamlit run main.py
```

### 2️⃣ **Run as a CLI Application**
You can also interact with the application directly via the command line:

#### **Add a Book**
```sh
python app.py add
```
It will prompt for book details such as title, author, year, genre, and content.

#### **Remove a Book**
```sh
python app.py remove
```
Enter the book ID to delete it from the library.

#### **Search for a Book**
```sh
python app.py search
```
Enter the title, author, or book ID to find matching books.

#### **Update a Book**
```sh
python app.py update
```
Modify book details by entering its ID.

#### **Display All Books**
```sh
python app.py display
```
Shows a list of all books stored in the library.

#### **View Statistics**
```sh
python app.py stats
```
Displays the total number of books and the percentage of books read.

---

## 📂 Project Structure
```
📁 Personal Library Manager
├── 📄 main.py  # Main Python application Streamlit
├── 📄 app.py  # Main Python application CLI
├── 📄 library.json        # JSON file storing book data
├── 📄 README.md           # Project documentation
```

---

## 📊 Statistics
- The **CLI** displays a **total count of books** and the **percentage of read books**.
- The **Streamlit UI** shows a **pie chart** of read vs. unread books.

---

## 📌 Future Enhancements
- Implement book categorization.
- Integrate a cloud database for better data storage.
- Add book cover images.

---

## 🎯 Conclusion
The **Personal Library Manager** is a flexible application that provides both a **graphical user interface** and a **command-line interface** to help users efficiently manage their book collection.

---

💡 Built with ❤️ using **Streamlit & Python**
