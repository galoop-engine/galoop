import numpy as np
from OpenGL.GL import *
from shaders.fragment_shader import *
from OpenGL.GL.shaders import compileProgram, compileShader

class Shape:
    def __init__(self, buffer=[], threads=1, stride=24):
        self.buffer = np.array(buffer, dtype=np.float32)
        # create a shader...
        # compilePorogram => compileShader =>
        self.shader = compileProgram(
            compileShader(
                vertex_shader, GL_VERTEX_SHADER,
            ),
            compileShader(
                fragment_shader, GL_FRAGMENT_SHADER
            )
        )
        self.object = glGenBuffers(threads)
        self.stride = stride
        self.size = self.buffer.nbytes


        glBindBuffer(GL_ARRAY_BUFFER, self.object)
        glBufferData(GL_ARRAY_BUFFER, self.size , self.buffer, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0) # vertices
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.stride, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1) # color
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, self.stride, ctypes.c_void_p(12))

        glUseProgram(self.shader)

    def update_buffer(self, _buffer):
        self.buffer = _buffer

    def render(self):
        _s = self.buffer.nbytes // self.stride
        print(f"{_s}")
        glDrawArrays(GL_TRIANGLE_STRIP, 0, _s  )
