#!/usr/bin/env python3

from libs import file
from libs.personalConfig import config
from libs.personalLogger import logger

pathTVShows = config["DEFAULT"]["pathTVShows"]

listaArquivos = file.list_files(pathTVShows, ".nfo")
for arquivo in listaArquivos:
    logger.info("Removendo o arquivo: " + arquivo)
    file.remove_file(arquivo)

listaArquivos = file.list_files(pathTVShows, ".nfo-orig")
for arquivo in listaArquivos:
    logger.info("Removendo o arquivo: " + arquivo)
    file.remove_file(arquivo)

listaArquivos = file.list_files(pathTVShows, ".DS_Store")
for arquivo in listaArquivos:
    logger.info("Removendo o arquivo: " + arquivo)
    file.remove_file(arquivo)
