from pathlib import Path
from escriba.core.chapter import Chapter
from escriba.core.scene import Scene
from escriba.persistence.markdown_writer import MarkdownChapterWriter


def test_chapter_is_saved_as_markdown(tmp_path):
    # Arrange
    chapter = Chapter(title="Capítulo 1")
    chapter.add_scene(Scene(text="Primera escena"))
    chapter.add_scene(Scene(text="Segunda escena"))

    writer = MarkdownChapterWriter()

    # Act
    file_path = writer.save(chapter, tmp_path)

    # Assert
    assert file_path.exists()

    content = file_path.read_text(encoding="utf-8")

    assert "# Capítulo 1" in content
    assert "## Escena 1" in content
    assert "Primera escena" in content
    assert "## Escena 2" in content
