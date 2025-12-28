from pathlib import Path
from escriba.core.chapter import Chapter
from escriba.core.scene import Scene


class ChapterLoader:
    """
    Re-build a Chapter from a .md file
    """

    def load(self, chapter_file: Path) -> Chapter:
        title = chapter_file.stem

        raw_text = chapter_file.read_text(encoding="utf-8")

        # Processing .md content
        scene_lines = []

        for line in raw_text.splitlines():
            line = line.strip()

            # Ignoraing headers
            if line.startswith("#"):
                continue

            # Ignoring empty lines
            if not line:
                continue

            scene_lines.append(line)

        # Re-building clean text
        scene_text = "\n".join(scene_lines)

        scene = Scene(text=scene_text)

        chapter = Chapter(title=title)
        chapter.add_scene(scene)

        return chapter
