from pathlib import Path
from escriba.core.chapter import Chapter

class MarkdownChapterWriter:
    """
    To save a chapter as Markdown (.md) file
    """

    def save(self, chapter: Chapter, directory: Path) -> Path:
        """
        Docstring for save
        
        :param chapter: Chapter to be saved
        :type chapter: Chapter
        :param directory: Directory where file will be saved
        :type directory: Path
        :return: Path of created file
        :rtype: Path
        """

        directory.mkdir(parents=True, exist_ok=True)

        # File creation (using name of the chapter)
        filename = f"{chapter.title}.md"
        file_path = directory / filename

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"# {chapter.title}\n\n")
            for index, scene in enumerate(chapter.scenes, start=1):
                file.write(f"## Escena {index}\n")
                file.write(scene.text.strip() + "\n\n")
        return file_path