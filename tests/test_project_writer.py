from escriba.core.project import Project
from escriba.core.book import Book
from escriba.core.chapter import Chapter
from escriba.core.scene import Scene
from escriba.persistence.project_writer import ProjectWriter


def test_project_is_saved_with_books_and_chapters(tmp_path):
    # Arrange
    project = Project(name="Mi Proyecto")

    book = Book(title="Primer Libro")
    chapter = Chapter(title="Capítulo 1")
    chapter.add_scene(Scene(text="Primera escena"))
    book.add_chapter(chapter)

    project.add_book(book)

    writer = ProjectWriter()

    # Act
    project_dir = writer.save(project, tmp_path)

    # Assert
    assert project_dir.exists()
    assert project_dir.is_dir()

    book_dir = project_dir / "Primer Libro"
    assert book_dir.exists()
    assert book_dir.is_dir()

    chapter_file = book_dir / "Capítulo 1.md"
    assert chapter_file.exists()
