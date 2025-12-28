from escriba.core.scene import Scene
from escriba.core.chapter import Chapter


def test_chapter_can_add_scene():
    # Arrange
    scene_text = "Esta es la primera escena"
    scene = Scene(text=scene_text)
    chapter = Chapter(title="Capítulo 1")

    # Act
    chapter.add_scene(scene)

    # Assert
    assert len(chapter.scenes) == 1
    assert chapter.scenes[0] is scene
    assert chapter.scenes[0].text == scene_text