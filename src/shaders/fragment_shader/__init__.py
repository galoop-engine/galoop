from OpenGL.GL import *
import numpy as np
# a ==> attrib
# v ==> varrying
vertex_shader = """
# version 330

layout(location=0) in vec3 a_Position;
layout(location=1) in vec3 a_Color;

out vec3 v_Color;

void main(){
    gl_Position = vec4(a_Position, 1.0);
    v_Color = a_Color;
}
"""

fragment_shader = """
# version 330

in vec3 v_Color;

out vec4 out_color;

void main(){
    out_color = vec4(v_Color, 1.0);
}
"""
