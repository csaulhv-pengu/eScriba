from escriba.persistence.project_writer import ProjectWriter
from escriba.persistence.project_loader import ProjectLoader
from escriba.core.project import Project
from escriba.core.book import Book
from escriba.core.chapter import Chapter
from escriba.core.scene import Scene


def test_project_can_be_saved_and_loaded(tmp_path):
    # Arrange (crear proyecto original)
    project = Project(name="Proyecto Test")

    book = Book(title="Libro Uno")
    chapter = Chapter(title="Capítulo 1")
    chapter.add_scene(Scene(text="Texto de la escena"))
    book.add_chapter(chapter)
    project.add_book(book)

    writer = ProjectWriter()
    loader = ProjectLoader()

    # Act (guardar y luego cargar)
    project_dir = writer.save(project, tmp_path)
    loaded_project = loader.load(project_dir)

    # Assert
    assert loaded_project.name == project.name
    assert len(loaded_project.books) == 1

    loaded_book = loaded_project.books[0]
    assert loaded_book.title == book.title
    assert len(loaded_book.chapters) == 1

    loaded_chapter = loaded_book.chapters[0]
    assert loaded_chapter.title == chapter.title
    assert loaded_chapter.scenes[0].text == "Texto de la escena"