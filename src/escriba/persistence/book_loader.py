from pathlib import Path
from escriba.core.book import Book
from escriba.persistence.chapter_loader import ChapterLoader


class BookLoader:
    """
    CUpload a Book from a Directory
    """

    def __init__(self):
        self.chapter_loader = ChapterLoader()

    def load(self, book_dir: Path) -> Book:
        """
        Re-builds a Book from a directory

        :param book_dir: Path to Book's directory
        :return: Book re-builded
        """

        book = Book(title=book_dir.name)

        for chapter_file in sorted(book_dir.glob("*.md")):
            chapter = self.chapter_loader.load(chapter_file)
            book.add_chapter(chapter)

        return book