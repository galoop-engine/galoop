import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import pyrr
from PIL import Image

from shape import Shape, Cube
import sys

import bimpy


class Window:
    # glfw callback functions
    def window_resize(self, window, width, height):
        glViewport(0, 0, width, height)
        projection = pyrr.matrix44.create_perspective_projection_matrix(45, width/height, 0.1, 100)

        # update all shapes project matricies
        for shape in self.shapes:
            glUniformMatrix4fv(shape.proj_loc, 1, GL_FALSE, projection)


    def __init__(self, window_title="Galoop Engine!", pos=(400,200), size=(1280, 720)):
        # initializing glfw library
  

        if not glfw.init():
            raise Exception("glfw can not be initialized!")

        # creating the window
        self.window = glfw.create_window(size[0], size[1], window_title, None, None)

        # check if self.window was created
        if not self.window:
            glfw.terminate()
            raise Exception("glfw self.windowcan not be created!")

        # set window's position
        glfw.set_window_pos(self.window, pos[0], pos[1])

        # set the callback function for self.windowresize
        glfw.set_window_size_callback(self.window, self.window_resize)

        # self.logger = bimpy.Context()
        # self.logger.init(200, 200, "Logger")
        # make the context current
        glfw.make_context_current(self.window)
        # BUG 
        # When more than one shader is applied 
        # only the most recent shader is applied

        # initalize Logger

        self.shapes = [
            Cube(texture_src="textures/test.png", position=[0, 0,-4]),
            # Cube(texture_src="textures/test2.png", position=[2, 1,-4])
            ]

    # the main application loop
    def update(self):


        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        
        for shape in self.shapes:
            shape.render()


        glfw.swap_buffers(self.window)

