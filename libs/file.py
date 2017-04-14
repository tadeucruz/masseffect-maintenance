import os

from libs.personalLogger import logger


def list_files(path, regex):
    list_files = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if regex in name:
                list_files.append(os.path.join(root, name))
    return list_files


def remove_file(file):
    if (os.path.isfile(file)):
        os.remove(file)
    else:
        logger.info("%s nao existe", file)


def remove_dir(dir):
    if (os.path.isdir(dir)):
        os.rmdir(dir)
    else:
        logger.info("%s nao existe", dir)
