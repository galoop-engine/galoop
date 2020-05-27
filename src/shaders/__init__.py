from OpenGL.GL import *
import numpy as np
# a ==> attrib
# v ==> varrying
vertex_src = """
# version 330
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
uniform mat4 model; // combined translation and rotation
uniform mat4 projection;
out vec3 v_color;
out vec2 v_texture;
void main()
{
    gl_Position = projection * model * vec4(a_position, 1.0);
    v_texture = a_texture;
}
"""

fragment_src = """
# version 330
in vec3 v_color;
in vec2 v_texture;
out vec4 out_color;
uniform sampler2D s_texture;
void main()
{
    out_color = texture(s_texture, v_texture);// * vec4(v_color, 1.0f);
}
"""
