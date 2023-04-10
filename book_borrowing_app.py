import streamlit as st

# Daftar buku
books = {
    "B0001": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available": 5},
    "B0002": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "available": 3},
    "B0003": {"title": "1984", "author": "George Orwell", "available": 2},
    "B0004": {"title": "Pride and Prejudice", "author": "Jane Austen", "available": 7},
    "B0005": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "available": 4},
}

# Fungsi untuk meminjam buku
def borrow_book(book_id):
    if book_id in books:
        if books[book_id]["available"] > 0:
            books[book_id]["available"] -= 1
            st.success("Buku telah berhasil dipinjam.")
        else:
            st.warning("Maaf, buku tidak tersedia saat ini.")
    else:
        st.error("Maaf, ID buku tidak ditemukan.")

# Fungsi untuk mengembalikan buku
def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] += 1
        st.success("Buku telah berhasil dikembalikan.")
    else:
        st.error("Maaf, ID buku tidak ditemukan.")

# Tampilan aplikasi
st.title("Aplikasi Peminjaman Buku")
st.write("Selamat datang di aplikasi peminjaman buku. Silakan pilih opsi di bawah ini.")

option = st.selectbox("Pilihan", ["", "Pinjam Buku", "Kembalikan Buku"])

if option == "Pinjam Buku":
    book_id = st.text_input("Masukkan ID Buku")
    if st.button("Pinjam"):
        borrow_book(book_id)

if option == "Kembalikan Buku":
    book_id = st.text_input("Masukkan ID Buku")
    if st.button("Kembalikan"):
        return_book(book_id)

st.write("Daftar Buku:")
for book_id, book_info in books.items():
    st.write(f"{book_id} - {book_info['title']} oleh {book_info['author']}. Tersedia: {book_info['available']}")
