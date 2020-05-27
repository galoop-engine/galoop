import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import pyrr
from PIL import Image
from shape import Shape, Cube


class Window:
    # glfw callback functions
    def window_resize(self, window, width, height):
        glViewport(0, 0, width, height)
        projection = pyrr.matrix44.create_perspective_projection_matrix(45, width/height, 0.1, 100)

        # update all shapes project matricies
        for shape in self.shapes:
            glUniformMatrix4fv(shape.proj_loc, 1, GL_FALSE, projection)


    def __init__(self):
        # initializing glfw library
        if not glfw.init():
            raise Exception("glfw can not be initialized!")

        # creating the window
        self.window= glfw.create_window(1280, 720, "My OpenGL window", None, None)

        # check if self.window was created
        if not self.window:
            glfw.terminate()
            raise Exception("glfw self.windowcan not be created!")

        # set window's position
        glfw.set_window_pos(self.window, 400, 200)

        # set the callback function for self.windowresize
        glfw.set_window_size_callback(self.window, self.window_resize)

        # make the context current
        glfw.make_context_current(self.window)

        self.shapes = [
            Cube(texture_src="textures/test.png")
            ]

    # the main application loop
    def update(self):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        for shape in self.shapes:
            shape.render()

        glfw.swap_buffers(self.window)
