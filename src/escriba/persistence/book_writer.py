from pathlib import Path
from escriba.core.book import Book
from escriba.persistence.markdown_writer import MarkdownChapterWriter


class BookWriter:
    """
    In charge of saving each Book as a Directory.
    Each chapter is saved as a Markdown file inside Book's Directory.
    """

    def __init__(self):
        self.chapter_writer = MarkdownChapterWriter()

    def save(self, book: Book, directory: Path) -> Path:
        """
        Saves a book in a Directory

        :param book: Book to be saved
        :param directory: Based Directory (project)
        :return: Path of Book's directory
        """

        book_dir = directory / book.title
        book_dir.mkdir(parents=True, exist_ok=True)

        for chapter in book.chapters:
            self.chapter_writer.save(chapter, book_dir)

        return book_dir
