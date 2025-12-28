from escriba.core.book import Book
from escriba.core.chapter import Chapter
from escriba.core.scene import Scene
from escriba.persistence.book_writer import BookWriter


def test_book_is_saved_as_folder_with_chapters(tmp_path):
    # Arrange
    book = Book(title="Primer Libro")

    chapter1 = Chapter(title="Capítulo 1")
    chapter1.add_scene(Scene(text="Escena 1 del capítulo 1"))

    chapter2 = Chapter(title="Capítulo 2")
    chapter2.add_scene(Scene(text="Escena 1 del capítulo 2"))

    book.add_chapter(chapter1)
    book.add_chapter(chapter2)

    writer = BookWriter()

    # Act
    book_dir = writer.save(book, tmp_path)

    # Assert
    assert book_dir.exists()
    assert book_dir.is_dir()

    chapter_files = list(book_dir.iterdir())

    assert len(chapter_files) == 2
    assert (book_dir / "Capítulo 1.md").exists()
    assert (book_dir / "Capítulo 2.md").exists()
