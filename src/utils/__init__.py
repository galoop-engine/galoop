from os import system, name


def cls():
    # defines a function that will clear the screen on call
    # if the operating system is equal to that of windows == "nt"
    if name == 'nt':
        # then clear my screen with the "cls" command
        system('cls')
    # else if the operating system falls on any other platform
    # EX: [ macOS, Linux ]
    else:
        # then clear with the "clear" command

        system('clear')


def load_model(self, name, default=False, file_path=None):
    if file_path is not None:
        return self.loader.loadModel(Filename.fromOsSpecific(os.path.abspath(path[0]) + file_path).getFullpath())
    elif default is not False:
        return self.loader.loadModel("models/{_}".format(_=name))
    else:
        return self.loader.loadModel(
            Filename.fromOsSpecific(
                os.path.abspath(path[0]) +
                "\\assets\\{_}.glb".format(_=name)
            ).getFullpath()
        )
