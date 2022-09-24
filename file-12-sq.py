# first commit
# concepts introduced in this project:
# • Using the GLFW windowing library for OpenGL
# • Using GLSL to write vertex and fragment shaders
# • Performing texture mapping
# • Using 3D transformations
# Geometric Primitives and 3D Transformation
# vertex shader
#version 330 core
in vec3 aVert;
uniform mat4 uMVMatrix;
uniform mat4 uPMatrix;
out vec4 vCol;

void main() 
{
# apply transformations
    gl_Position = uPMatrix * uMVMatrix * vec4(aVert, 1.0);
# set color
    vCol = vec4(1.0, 0.0, 0.0, 1.0);
}
