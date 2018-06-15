import sys  # NOQA
import os
import shutil
import pickle
from docx import Document
import PyPDF2
from bs4 import BeautifulSoup
from whoosh import fields, index
from whoosh.analysis import SimpleAnalyzer, StopFilter

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
from searchEngine.seconfig import SearchEngineConfig
import time

WHOOSH_SCHEMA = fields.Schema(title=fields.TEXT(stored=True),
                              path=fields.ID(stored=True, unique=True),
                              content=fields.TEXT(analyzer=SimpleAnalyzer() | StopFilter(), stored=False))
FILE_INDEXED_LIST = []


# Creates a list of all the files in the lookup directory
def list_all_files():
    file_name_list = []
    for path, subdirs, files in os.walk(SearchEngineConfig.DOCUMENT_LOOKUP_DIRECTORY):
        for name in files:
            extension = os.path.splitext(name)[1]
            if extension in SearchEngineConfig.SUPPORTED_EXTENSIONS:
                file_name_list.append(str(os.path.join(path, name)))
    return file_name_list


# Get text from a word document
def get_text_from_word_document(filename):
    doc = Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


# Check for any deleted file
def check_deleted_files():
    global FILE_INDEXED_LIST
    deleted_file_list = []
    for file in FILE_INDEXED_LIST:
        if not os.path.isfile(file):
            deleted_file_list.append(file)
    return deleted_file_list


# Delete old index and create a new one
def create_fresh_index():
    if os.path.exists(".indexdir"):
        shutil.rmtree(".indexdir", ignore_errors=True)
    return create_index()


# Parsing pdf files
def read_pdf(filename):
    content = ""
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for x in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(x)
        content += (pageObj.extractText())
    return content


# Get the information about an file
def get_file_attribute(new_files):
    global FILE_INDEXED_LIST
    files_info_list = []
    for file in new_files:
        extension = os.path.splitext(file)[1]
        if extension == ".txt":
            files_info_list += ([(file, os.path.basename(file), open(file).read())])
        elif extension == ".html" or extension == ".htm":
            markup = open(file)
            soup = BeautifulSoup(markup.read(), "lxml")
            markup.close()
            files_info_list += ([(file, os.path.basename(file), soup.get_text())])
        elif extension == ".docx":
            files_info_list += ([(file, os.path.basename(file), get_text_from_word_document(file))])
        elif extension == ".pdf":
            files_info_list += ([(file, os.path.basename(file), read_pdf(file))])
        FILE_INDEXED_LIST.append(file)
    return files_info_list


# Update docs that have been modified and their new index has to be updated
def update_indexed_document(path):
    global FILE_INDEXED_LIST
    print("Updating the Index.....")
    start = time.time()
    if not os.path.exists(".indexdir"):
        print("No indexer Found try creating one first")
        return
    else:
        ix = index.open_dir(".indexdir")
        writer = ix.writer()
        writer.add_document(path=path, title=os.path.basename(path), content=open(path).read())
        writer.commit(optimize=True)
    end = time.time()
    print("Indexing completed in " + str(end - start) + " seconds")


# This method has the intelligent method of looking up for new and deleted files
def update_existing_index():
    global FILE_INDEXED_LIST
    all_file_list = list_all_files()
    new_files = list(set(all_file_list) - set(FILE_INDEXED_LIST))
    print("Updating the Index.....")
    start = time.time()
    if not os.path.exists(".indexdir"):
        print("No indexer Found try creating one first")
        return
    else:
        deleted_file_list = check_deleted_files()
        if len(new_files) == 0:
            print("Existing index found, updating 0 new files , removing " + str(
                len(deleted_file_list)) + " deleted files")
            if len(deleted_file_list) != 0:
                ix = index.open_dir(".indexdir")
                writer = ix.writer()
                for deleted_file in deleted_file_list:
                    writer.delete_by_term('path', deleted_file)
                    FILE_INDEXED_LIST.remove(deleted_file)
                writer.commit(optimize=True)
                with open('.index_file_list.txt', 'wb') as fp:
                    pickle.dump(FILE_INDEXED_LIST, fp)
            else:
                return
        else:
            print("Existing index found, updating " + str(len(new_files)) + " new files, removing " + str(
                len(deleted_file_list)) + " deleted files")
            ix = index.open_dir(".indexdir")
            writer = ix.writer()
            for info in get_file_attribute(new_files):
                writer.add_document(path=info[0], title=info[1], content=info[2])
            if len(deleted_file_list) != 0:
                for deleted_file in deleted_file_list:
                    writer.delete_by_term('path', deleted_file)
                    FILE_INDEXED_LIST.remove(deleted_file)
            writer.commit(optimize=True)
            with open('.index_file_list.txt', 'wb') as fp:
                pickle.dump(FILE_INDEXED_LIST, fp)
    end = time.time()
    print("Indexing completed in " + str(end - start) + " seconds")
    return ix


# This method scans all the files that are there in the lookup directory
def get_all_txt_files():
    files_info_list = []
    count=0
    global FILE_INDEXED_LIST
    for path, subdirs, files in os.walk(SearchEngineConfig.DOCUMENT_LOOKUP_DIRECTORY):
        for name in files:
            try:
                extension = os.path.splitext(name)[1]
                if extension in SearchEngineConfig.SUPPORTED_EXTENSIONS:
                    count+=1
                    if extension == ".txt":
                        file_info_list = [
                        ((os.path.join(path, name)), name, open(os.path.join(path, name)).read())]
                        files_info_list += (file_info_list)
                    elif extension == ".html" or extension == ".htm":
                        markup = open(os.path.join(path, name))
                        soup = BeautifulSoup(markup.read(), "lxml")
                        markup.close()
                        file_info_list = [
                        ((os.path.join(path, name)), name, soup.get_text())]
                        files_info_list += (file_info_list)
                    elif extension == ".docx":
                        file_info_list = [
                        ((os.path.join(path, name)), name, get_text_from_word_document(os.path.join(path, name)))]
                        files_info_list += (file_info_list)
                    elif extension == ".pdf":
                        file_info_list = [
                        ((os.path.join(path, name)), name, read_pdf(os.path.join(path, name)))]
                        files_info_list += (file_info_list)
                    FILE_INDEXED_LIST.append(os.path.join(path, name))
            except:
                count-=1
                continue
    print("Indexing "+ str(count)+" files")
    return files_info_list


# The method is used to take in the text from files and create the index
def create_index():
    start = time.time()
    print("Indexing in progress....")
    global FILE_INDEXED_LIST
    if not os.path.exists(".indexdir"):
        try:
            os.mkdir(".indexdir")
            ix = index.create_in(".indexdir", WHOOSH_SCHEMA)
            writer = ix.writer()
            for info in get_all_txt_files():
                writer.add_document(path=info[0], title=info[1], content=info[2])
            writer.commit(optimize=True)
            with open('.index_file_list.txt', 'wb') as fp:
                pickle.dump(FILE_INDEXED_LIST, fp)
        except Exception as ex:
            print("Index was not created successfully due to " + str(ex))
            shutil.rmtree(".indexdir", ignore_errors=True)
            return
    else:
        print("Existing index found")
        ix = index.open_dir(".indexdir")
        with open('.index_file_list.txt', 'rb') as fp:
            FILE_INDEXED_LIST = pickle.load(fp)
    end = time.time()
    print("Indexing completed in " + str(end - start) + " seconds")
    return ix
