from escriba.core.project import Project
from escriba.core.book import Book
from escriba.core.chapter import Chapter
from escriba.core.scene import Scene

def test_project_can_add_book():
    # Arrange
    project = Project(name="Primer proyecto")
    book = Book(title="Primer libro")
    chapter = Chapter(title="Capitulo 1")
    scene = Scene(text="Esta es la primera escena")

    # Act
    project.add_book(book)
    book.add_chapter(chapter)
    chapter.add_scene(scene)

    # Assert
    assert len(project.books) == 1
    assert project.books[0] is book

    assert len(book.chapters) == 1
    assert book.chapters[0] is chapter

    assert len(chapter.scenes) == 1
    assert chapter.scenes[0] is scene
    assert chapter.scenes[0].text == "Esta es la primera escena"