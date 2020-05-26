
class Renderer:
    def __init__(self):
        self.render_queue = Queue()

"""
    the renderer stores all of the shapes
    and renders them on the screen inside the view


    the render_queue
    [node] -> [node] -> [node]
"""
