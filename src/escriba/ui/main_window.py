from PySide6.QtWidgets import(
    QMainWindow,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QSplitter
)

from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("eScriba")
        self.setMinimumSize(1000,700)

        self._setup_ui()

    def _setup_ui(self):
        splitter = QSplitter(Qt.Horizontal)

        project_tree = QTreeWidget()
        project_tree.setHeaderLabel("Project")

        editor = QTextEdit()
        editor.setPlaceholderText("Start writing...")

        splitter.addWidget(project_tree)
        splitter.addWidget(editor)
        splitter.setSizes([250, 750])

        self.setCentralWidget(splitter)