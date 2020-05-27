import glfw
import numpy as np
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import pyrr
from PIL import Image
from utils.logger import Logger

from shaders import vertex_src, fragment_src
from enum import Enum

class BufferType:
    TRIANGLE = [

    ]
    QUAD = [

    ]
    CUBE = (
            [ #    X     Y     Z      U    V
                 -0.5, -0.5,  0.5,   0.0, 0.0,
                  0.5, -0.5,  0.5,   1.0, 0.0,
                  0.5,  0.5,  0.5,   1.0, 1.0,
                 -0.5,  0.5,  0.5,   0.0, 1.0,

                 -0.5, -0.5, -0.5,   0.0, 0.0,
                  0.5, -0.5, -0.5,   1.0, 0.0,
                  0.5,  0.5, -0.5,   1.0, 1.0,
                 -0.5,  0.5, -0.5,   0.0, 1.0,

                  0.5, -0.5, -0.5,   0.0, 0.0,
                  0.5,  0.5, -0.5,   1.0, 0.0,
                  0.5,  0.5,  0.5,   1.0, 1.0,
                  0.5, -0.5,  0.5,   0.0, 1.0,

                 -0.5,  0.5, -0.5,   0.0, 0.0,
                 -0.5, -0.5, -0.5,   1.0, 0.0,
                 -0.5, -0.5,  0.5,   1.0, 1.0,
                 -0.5,  0.5,  0.5,   0.0, 1.0,

                 -0.5, -0.5, -0.5,   0.0, 0.0,
                  0.5, -0.5, -0.5,   1.0, 0.0,
                  0.5, -0.5,  0.5,   1.0, 1.0,
                 -0.5, -0.5,  0.5,   0.0, 1.0,

                  0.5,  0.5, -0.5,   0.0, 0.0,
                 -0.5,  0.5, -0.5,   1.0, 0.0,
                 -0.5,  0.5,  0.5,   1.0, 1.0,
                  0.5,  0.5,  0.5,   0.0, 1.0
            ],
            [
                0,  1,  2,  2,  3,  0,
                4,  5,  6,  6,  7,  4,
                8,  9, 10, 10, 11,  8,
                12, 13, 14, 14, 15, 12,
                16, 17, 18, 18, 19, 16,
                20, 21, 22, 22, 23, 20
        ])

class Shape:

    #    (v_buffer, i_buffer, threads, stride)

    def __init__(self, vertex_buffer, index_buffer, texture_src=None, position=[0,0,-5]):
        # Debugging REMOVE
        self.logger = Logger()
        self.indices = index_buffer
        vertices = np.array(vertex_buffer, dtype=np.float32)
        self.indices = np.array(self.indices, dtype=np.uint32)

        self.position = position
        shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

        # Vertex Buffer Object
        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        # Element Buffer Object
        EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices.itemsize * 5, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices.itemsize * 5, ctypes.c_void_p(12))

        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)

        # Set the texture wrapping parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        # Set texture filtering parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # load image
        image = None
        if texture_src is not None:
            image = Image.open(texture_src)
        if image is not None:
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
            img_data = image.convert("RGBA").tobytes()
            # img_data = np.array(image.getdata(), np.uint8) # second way of getting the raw image data
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

        glUseProgram(shader)
        glClearColor(0, 0.1, 0.1, 1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280/720, 0.1, 100)

        self.model_loc = glGetUniformLocation(shader, "model")
        print(self.model_loc)
        self.proj_loc = glGetUniformLocation(shader, "projection")
        print(self.proj_loc)

        glUniformMatrix4fv(self.proj_loc, 1, GL_FALSE, projection)


    def render(self):
        # create a rotation constant rotation.
        rot_x = pyrr.Matrix44.from_x_rotation(0.45 * glfw.get_time())
        rot_y = pyrr.Matrix44.from_y_rotation(0.45 * glfw.get_time())

        # create a translation matrix
        translation = pyrr.matrix44.create_from_translation(self.position)
        # create a rotation matrix
        rotation = pyrr.matrix44.multiply(rot_x, rot_y)
        # create a scale matrix
        scale = pyrr.matrix44.create_from_scale([1,1,1])

        # apply all the created matricies to the model matrix
        model = pyrr.matrix44.multiply( rotation, translation)
        model = pyrr.matrix44.multiply(model, scale)

        # upload the model matrix to the model_location of the shader
        glUniformMatrix4fv(self.model_loc, 1, GL_FALSE, model)

        # render the shape
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)

    def set_position(self, position):
        self.position = position

class Cube(Shape):
    """
        texture_src:
        position: [x, y, z]
        rotation: [x, y, z]
    """
    def __init__(self, texture_src=None, position=[0,0,-10]):
        super().__init__(
            vertex_buffer= BufferType.CUBE[0],
            index_buffer= BufferType.CUBE[1],
            texture_src=texture_src,
            position=position
        )
        # self.get_buffer()
        # print(self.get_buffers())

    def render(self):
        super().render()
        # print("ugh...")


class Quad(Shape):
    # rect: a list of tuples
    # [
    #   (x, y, z),  -> V1
    #   (x, y, z),  -> V2
    #   (x, y, z)   -> V3
    #   (x, y, z)   -> V4
    # ]
    # color: tuple of rgb values
    # (r, g, b)
    def __init__(self, rect=[], color=(), texture_map=[]):
        # add LOGGER logic to tell the user that the
        # shape doesnt have the:
        # correct number of args
        # the correct number of rect-args ==> 4
        # warn if the numbers in color are greater than 1.0

        __v_buffer = [
            rect[0][0], rect[0][1],  rect[0][2],  color[0], color[1], color[2], texture_map[0][0], texture_map[0][1],
            rect[1][0], rect[1][1],  rect[1][2],  color[0], color[1], color[2], texture_map[1][0], texture_map[1][1],
            rect[2][0], rect[2][1],  rect[2][2],  color[0], color[1], color[2], texture_map[2][0], texture_map[2][1],
            rect[3][0], rect[3][1],  rect[3][2],  color[0], color[1], color[2], texture_map[3][0], texture_map[3][1],
        ]
        __i_buffer = [
            0, 1, 2,
            2, 3, 0
        ]
        super().__init__(__v_buffer, __i_buffer)

class Triangle(Shape):

    def __init__(self, triangle=[], color=(), texture_map=[]):
        __v_buffer = [
            triangle[0][0], triangle[0][1],  triangle[0][2],    color[0], color[1], color[2], texture_map[0][0], texture_map[0][1],
            triangle[1][0], triangle[1][1],  triangle[1][2],    color[0], color[1], color[2], texture_map[1][0], texture_map[1][1],
            triangle[2][0], triangle[2][1],  triangle[2][2],    color[0], color[1], color[2], texture_map[2][0], texture_map[2][1],
        ]
        #  the triangle will render in order 0, 1, 2 of found
        #  vertices in the vertex buffer
        #
        #    0 . . . . .1                     1                   1
        #      .        .                   . .                 .  .
        #        .      .                 .   .               .      .
        #          .    .               .     .             .          .
        #            .  .             .       .           .             .
        #               2           0 . . . . 2         0 . . . . . . . . 2
        __i_buffer = [
            0, 1, 2
         ]
        super().__init__(__v_buffer, __i_buffer)
