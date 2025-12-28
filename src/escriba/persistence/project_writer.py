from pathlib import Path
from escriba.core.project import Project
from escriba.persistence.book_writer import BookWriter


class ProjectWriter:
    """
    In charge of Project saving as a Directory
    Each book is saved into this main Directory
    """

    def __init__(self):
        #Reusing book writer
        self.book_writer = BookWriter()

    def save(self, project: Project, directory: Path) -> Path:
        """
        Saving project

        :param project: Project to save
        :param directory: Base directory to save Project
        :return: Path to Project's directory
        """

        project_dir = directory / project.name
        project_dir.mkdir(parents=True, exist_ok=True)

        for book in project.books:
            self.book_writer.save(book, project_dir)

        return project_dir
