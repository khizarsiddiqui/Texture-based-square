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
import glutils

import glfw.GLFW as glfw

import OpenGL
from OpenGL.GL import *

import numpy, math, sys, os

# VERTEX SHADER
#version 330 core

# in vec3 aVert;

# uniform mat4 uMVMatrix;
# uniform mat4 uPMatrix;

# out vec4 vCol;

# void main()
# {
# // apply transformations
#     gl_Position = uPMatrix * uMVMatrix * vec4(aVert, 1.0);
# // set color
# {   vCol = vec4(1.0, 0.0, 0.0, 1.0);
# }

# # FRAGMENT SHADER
# #version 330 core
# in vec4 vCol;

# out vec4 fragColor;
# void main() {
# // use vertex color
#    fragColor = vCol;
# }

# VERTEX BUFFERS
# DISPLAYING OPENGL 

# code
# creating opengl window
class RenderWindow:
# GLFW Rendering window class
    def __init__(self):
# save current working directory
        cwd = os.getcwd()
# initialize glfw
        glfw.glfwInit()
# restore cwd
        os.chdir(cwd)
# version hints
        glfw.glfwWindowHint(glfw.GLFW_CONTEXT_VERSION_MAJOR, 3)
        glfw.glfwWindowHint(glfw.GLFW_CONTEXT_VERSION_MINOR, 3)
        glfw.glfwWindowHint(glfw.GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE)
        glfw.glfwWindowHint(glfw.GLFW_OPENGL_PROFILE,
        glfw.GLFW_OPENGL_CORE_PROFILE)
# make a window
        self.width, self.height = 640, 480
        self.aspect = self.width/float(self.height)
        self.win = glfw.glfwCreateWindow(self.width, self.height,
                                        b'simpleglfw')
# make the context current
        glfw.glfwMakeContextCurrent(self.win)
# initialize GL
        glViewport(0, 0, self.width, self.height)
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.5, 0.5, 0.5, 1.0)

# set window callbacks
        glfw.glfwSetMouseButtonCallback(self.win, self.onMouseButton)
        glfw.glfwSetKeyCallback(self.win, self.onKeyboard)
        glfw.glfwSetWindowSizeCallback(self.win, self.onSize)

# keyboard callback
    def onKeyboard(self, win, key, scancode, action, mods):
#print 'keyboard: ', win, key, scancode, action, mods
        if action == glfw.GLFW_PRESS:
# ESC to quit
                if key == glfw.GLFW_KEY_ESCAPE:
                        self.exitNow = True
                else:
# toggle cut
                        self.scene.showCircle = not self.scene.showCircle

# window-resizing event
    def onSize(self, win, width, height):
#print 'onsize: ', win, width, height
        self.width = width
        self.height = height
        self.aspect = width/float(height)
        glViewport(0, 0, self.width, self.height)

# main loop (GLFW does not provide a default program loop.)
    def run(self):
# initializer timer
        glfw.glfwSetTime(0)
        t = 0.0
        while not glfw.glfwWindowShouldClose(self.win) and not self.exitNow:
# update every x seconds
                currT = glfw.glfwGetTime()
                if currT - t > 0.1:
# update time
                        t = currT
# clear
                        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
# build projection matrix
                        pMatrix = glutils.perspective(45.0, self.aspect, 0.1, 100.0)
                        
                        mvMatrix = glutils.lookAt([0.0, 0.0, -2.0], [0.0, 0.0, 0.0],
                                                  [0.0, 1.0, 0.0])
# render
                        self.scene.render(pMatrix, mvMatrix)
# step
                        self.scene.step()
                        glfw.glfwSwapBuffers(self.win)
# poll for and process events
                        glfw.glfwPollEvents()
# end
        glfw.glfwTerminate()
# the scene class
class Scene:
# OpenGL 3D scene class
# initialization
    def __init__(self):
# create shader
        self.program = glutils.loadShaders(strVS, strFS)
        glUseProgram(self.program)
        
        self.pMatrixUniform = glGetUniformLocation(self.program, b'uPMatrix')
        self.mvMatrixUniform = glGetUniformLocation(self.program, b'uMVMatrix')
# texture
        self.tex2D = glGetUniformLocation(self.program, b'tex2D')

# defining 3d Geometry
