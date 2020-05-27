from window import Window
import glfw

if __name__ == "__main__":
    windows = [
         Window(window_title="Main"),   
         Window(window_title="Logger", size=(500, 200))
         ]
    # make the context current

    for w in windows:
        while not glfw.window_should_close(w.window):
            w.update()

# terminate the glfw process

glfw.terminate()

