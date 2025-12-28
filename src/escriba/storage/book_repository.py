import yaml
from pathlib import Path
from escriba.core.book import Book
from escriba.core.chapter import Chapter


class BookRepository:
    def __init__(self, base_path: Path) -> None:
        self.base_path = base_path

    def save(self, book: Book) -> None:
        data = {
            "title": book.title,
            "chapters": [
                {"title": chapter.title}
                for chapter in book.chapters
            ],
        }

        path = self.base_path / f"{book.title}.yaml"
        with open(path, "w") as f:
            yaml.safe_dump(data, f)

    def load(self, title: str) -> Book:
        path = self.base_path / f"{title}.yaml"
        with open(path) as f:
            data = yaml.safe_load(f)

        book = Book(title=data["title"])
        for ch in data.get("chapters", []):
            book.add_chapter(Chapter(title=ch["title"]))

        return book