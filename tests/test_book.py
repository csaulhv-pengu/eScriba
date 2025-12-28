from escriba.core.book import Book
from escriba.core.chapter import Chapter
from escriba.core.scene import Scene

def test_book_can_add_chapter():
    # Arrange
    book = Book(title="Primer Libro")
    chapter = Chapter(title="Capitulo 1")
    scene = Scene(text="Esta es la primera escena")

    # Act
    book.add_chapter(chapter=chapter)
    chapter.add_scene(scene=scene)

    # Assert
    assert len(book.chapters) == 1
    assert book.chapters[0] is chapter
    
    assert len(chapter.scenes) == 1
    assert chapter.scenes[0] is scene
    assert chapter.scenes[0].text == "Esta es la primera escena"