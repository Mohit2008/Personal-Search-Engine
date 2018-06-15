import sys  # NOQA
import os
from werkzeug.wsgi import responder
from whoosh.qparser import QueryParser
import json

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
from searchEngine.indexer import index

ix = index.create_index()

# Do the query using the woosh index
def do_search(query):
    qp = QueryParser("content", schema=ix.schema)
    q = qp.parse(query)
    response = {}
    with ix.searcher() as s:
        corrected = s.correct_query(q, query)
        if corrected.query != q:
            print("Did you mean:", corrected.string)
            response[0] = [corrected.string]
        else:
            results = s.search(q)
            found = results.scored_length()
            print(results)
            response = generate_file_stats_with_size(results)
    return json.dumps(response)

# Get some additional about the file
def generate_file_stats_with_size(results):
    response = {}
    results_length = results.scored_length()
    for i, result in enumerate(results):
        path = results.fields(i)['path']
        info = os.stat(path)
        print(str(i + 1) + ") File Name: " + results.fields(i)['title'], " , File Location: " + path,
                       " , File Size: " + str(info.st_size))
        response[i] = [results.fields(i)['path'], results.fields(i)['title'], str(info.st_size), results_length]
    return response
