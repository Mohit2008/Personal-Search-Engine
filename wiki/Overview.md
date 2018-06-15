# Overview

This tool is a personalized search engine for your own machine. The basic idea is to build an indexer for files that the user wants to search within a given local drive or directory. The scoring function will use BM25 to generate the rank for each document/file. The interface is simple and similar to Google. When searching for a document/file on your machine LDSE will return a list of relevant document matches (not just matched keywords like in spotlight search/bing search). This system also handles incomplete queries, stemming of repeated words and building full document indexer.


LDSE is designed to operate for various file formats like ".txt",".html",".htm",".docx", and ".pdf". If you do wish to perform a batch indexing you might have to allow some time for this to process as this is a time intensive process. For incremental indexing, we have given support in our application where you can add only the new documents to the existing index without having to re-index the entire set. You can also delete the indexes of files that have been removed from the file system. LDSE has an intelligent way of identifying such changes and can automatically update your indexes when a file is deleted or added.

It is an open source tool that is designed to benefit an individual user for personal local search. It is intended to be simple and easy to use for a user of any age or skill level. Because in today’s society, virtually everyone has a computer with hundred/thousands of files stored on it – improving the existing tool for searching for a specific file would be useful.

This project is implemented in python and packed in wheel format so that it can run on any OS (Mac, Windows, Linux).


## A word about existing tools

Yes, a similar tool exists, but ours makes improvements in several important ways. For example, what windows indexer does is a search for keywords (when you enable that feature on) and doesn’t perform when you have multiple keywords in your query. This is because it does not have a scoring function.

Secondly, Spotlight search on OSX provides fast desktop searching by extracting meta-data in the background and storing the indexed meta-data for future searches. When a query is made, the indexed meta-data is searched for matching files. This indexing of meta-data will not be that helpful in finding relevant documents for queries that are intended towards the text in a document, as it dosen't support full text based indexing. To test this, try creating multiple documents with similar content and then type a query in the Spotlight search - this will not find documents listed according to relevance. All it does is capture keywords that are contained within documents and list them.
 
Our tool intents to improve local search by including an index and ranking function. We believe, and feel the end user will agree, that this difference is important and will drastically improve personalized search on your local machine. I, for one, have been frustrated when trying to find where a file was located on my computer and had no use in finding it after running various searches within Spotlight. Developing a tool as we intend will bring more intelligence to searching for files on your computer.
