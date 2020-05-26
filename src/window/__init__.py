import glfw
from OpenGL.GL import *
import numpy as np

from shaders.fragment_shader import *
from OpenGL.GL.shaders import compileProgram, compileShader

from shape import Shape

class Window:
    """
        Instantiates a GLFW Window with the properties passed in
        * width --> the width of the window being created
            =>  if the width is not set then the width will
                default to 1280
        * height --> the height of the window being created
            =>  if the width is not set then the width will
                default to 1280
        * title --> the title of the window created
           =>   if the user did not pass in a title.
                The Engine will set the title to Galoop Engine
    """
    def resize(self, window, width, height):
        # Top, Left, Width, Height
        glViewport(0, 0, width, height)

    def __init__(self, width=1280, height=720, title="Galoop Engine"):
        print('initalizing')
        if not glfw.init():
            raise Exception("GLFW cam mot be initalized!")

        self.instance = glfw.create_window(width, height, title, None, None)
        # self.resize()
        # if for some reason this instance was not able to be created
        # throw exception
        if not self.instance:
            glfw.terminate()
            raise Exception("glfw window could not be created!")

        # move the window instance
        glfw.set_window_pos(self.instance, 400, 200)
        glfw.set_window_size_callback(self.instance, self.resize)
        # this is a Buffer
        glfw.make_context_current(self.instance)

        self.vertices = [
            -0.4, -0.4, 0.0, 1.0, 0.0, 0.0,
             0.4, -0.4, 0.0, 0.0, 1.0, 0.0,
            -0.4,  0.4, 0.0, 0.0, 0.0, 1.0,
             0.4,  0.4, 0.0, 1.0, 1.0, 1.0,
             0.0,  0.8, 0.0, 1.0, 1.0, 1.0,
        ]
        self.shape = Shape(buffer=self.vertices)
        # set the newly created instance to current
        # if there are more instances inside the stack this one will
        # move to the top

    def update(self):


        # openGL doesnt work with pythons list class so
        # convert the verticies list to self.vertices array

        glClearColor(.8, 0.12, 0.14, 1)

        while not glfw.window_should_close(self.instance):
            glfw.poll_events()
            # Clear the Buffer
            glClear(GL_COLOR_BUFFER_BIT)
            self.shape.render()
            # glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

            glfw.swap_buffers(self.instance)


# terminate the glfw process
glfw.terminate()
