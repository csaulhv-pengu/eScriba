from escriba.core.book import Book
from escriba.core.chapter import Chapter
from escriba.storage.book_repository import BookRepository


def test_can_save_and_load_book_with_chapters(tmp_path):
    # Arrange
    book = Book(title="Libro Persistido")
    book.add_chapter(Chapter(title="Capítulo 1"))
    book.add_chapter(Chapter(title="Capítulo 2"))

    repo = BookRepository(base_path=tmp_path)

    # Act
    repo.save(book)
    loaded_book = repo.load("Libro Persistido")

    # Assert
    assert loaded_book.title == book.title
    assert len(loaded_book.chapters) == 2
    assert loaded_book.chapters[0].title == "Capítulo 1"
    assert loaded_book.chapters[1].title == "Capítulo 2"