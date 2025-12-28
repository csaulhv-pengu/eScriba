from pathlib import Path
from escriba.core.project import Project
from escriba.persistence.book_loader import BookLoader


class ProjectLoader:
    """
    Re-builds a project from a Directory
    """

    def __init__(self):
        self.book_loader = BookLoader()

    def load(self, project_dir: Path) -> Project:
        """
        Re-builds a Project from the computer storage

        :param project_dir: Root Path of the project
        :return: Re-builded project
        """

        project = Project(name=project_dir.name)

        for book_dir in sorted(p for p in project_dir.iterdir() if p.is_dir()):
            book = self.book_loader.load(book_dir)
            project.add_book(book)

        return project