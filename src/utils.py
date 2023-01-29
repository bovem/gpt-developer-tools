import os

def file_path(string):
    if os.path.isfile(string):
        return string
    else:
        raise Exception("{} is not a path to file".format(string))