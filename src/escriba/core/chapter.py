from escriba.core.scene import Scene

class Chapter:
    def __init__(self, title: str):
        self.title = title
        self.scenes: list[Scene] = []

    def add_scene(self, scene:Scene):
        self.scenes.append(scene)