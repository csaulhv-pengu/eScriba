from escriba.core.chapter import Chapter

class Book:
    def __init__(self, title:str):
        self.title = title
        self.chapters: list[Chapter] = []
    
    def add_chapter(self, chapter:Chapter):
        self.chapters.append(chapter)