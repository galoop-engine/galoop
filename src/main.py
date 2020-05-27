from window import Window
import glfw

if __name__ == "__main__":
    window = Window()
    while not glfw.window_should_close(window.window):
        window.update()


# terminate the glfw process
glfw.terminate()
