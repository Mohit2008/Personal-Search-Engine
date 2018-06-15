import os
from os import path

here = path.abspath(path.dirname(__file__))


class SearchEngineConfig:
    DOCUMENT_LOOKUP_DIRECTORY = path.join(here, os.pardir, 'documents-dir')
    SUPPORTED_EXTENSIONS = [".txt",".html",".htm",".docx",".pdf"]
