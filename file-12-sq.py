# first commit
# concepts introduced in this project:
# • Using the GLFW windowing library for OpenGL
# • Using GLSL to write vertex and fragment shaders
# • Performing texture mapping
# • Using 3D transformations
# Geometric Primitives and 3D Transformation
# import OpenGL
# from OpenGL.GL import *

# import numpy, math, sys, os
# import glutils

import glfw.GLFW as glfw

import OpenGL
from OpenGL.GL import *

import numpy, math, sys, os

# VERTEX SHADER
#version 330 core

in vec3 aVert;

uniform mat4 uMVMatrix;
uniform mat4 uPMatrix;

out vec4 vCol;

void main()
{
// apply transformations
    gl_Position = uPMatrix * uMVMatrix * vec4(aVert, 1.0);
// set color
{   vCol = vec4(1.0, 0.0, 0.0, 1.0);
}

# FRAGMENT SHADER
#version 330 core
in vec4 vCol;

out vec4 fragColor;
void main() {
// use vertex color
   fragColor = vCol;
}

# VERTEX BUFFERS
# DISPLAYING OPENGL (will be continued)