## Local Desktop Search Engine

## Team members and contact information

Mohit	Khanna,	mohit.khanna2008@gmail.com	(Project Coordinator)

Brad Ballard, ballard6@gmail.com

Anupana	Agrahari, anupama_agrahari@yahoo.com

## What is the function of the tool?

The tool is a personalized search engine for your own machine. The basic idea is to build an indexer for files that the user wants to search within a given local drive or directory. The scoring function will use BM25 to generate the rank for each document/file. The interface will be simple and similar to Google. When searching for a document/file on your machine it will return a list of relevant document matches (not just matched keywords like in spotlight search). This project will be implemented in python and packed in wheel format so that it can run on any OS.

## Who will benefit from such a tool?

It is an open source tool that is designed to benefit an individual user for personal local search. It is intended to be simple and easy to use for a user of any age or skill level. Because in today’s society, virtually everyone has a computer with hundred/thousands of files stored on it – improving the existing tool for searching for a specific file would be useful.

## Does this kind of tool already exist? If similar tools exist, how is your tool different from them? Would people care about the difference?

Yes, a similar tool exists, but ours makes improvements in several important ways. For example, what windows indexer does is a search for keywords (when you enable that feature on) and doesn’t perform when you have multiple keywords in your query. This is because it does not have a scoring function.

Secondly, Spotlight search on OSX provides fast desktop searching by extracting meta-data in the background and storing the indexed meta-data for future searches. When a query is made, the indexed meta-data is searched for matching files. This indexing of meta-data will not be that helpful in finding relevant documents for queries that are intended towards the text in a document, as it dosen't support full text based indexing. To test this, try creating multiple documents with similar content and then type a query in the Spotlight search - this will not find documents listed according to relevance. All it does is capture keywords that are contained within documents and list them.
 
Our tool intents to improve local search by including an index and ranking function. We believe, and feel the end user will agree, that this difference is important and will drastically improve personalized search on your local machine. I, for one, have been frustrated when trying to find where a file was located on my computer and had no use in finding it after running various searches within Spotlight. Developing a tool as we intend will bring more intelligence to searching for files on your computer.

## What existing resources can you use?

This project intends to make a system that not only ranks documents/texts based upon the scorer but also generate many useful information about the document. An existing tool that we plan to build from is a python based library called Whoosh. Whoosh is a fast, featureful full-text indexing and searching library implemented in pure Python. Programmers can use it to easily add search functionality to their applications and websites.

## What techniques/algorithms will you use to develop the tool? (It's fine if you just mention some vague idea.)

 We plan to build up a parsing module that would pick up each file and generate some meta information and extract fields from the document. Next, we shall use Woosh to construct an indexer that shall be based on a custom schema. Following that, we plan to use the BM25 ranker to score our documents. Finally, we plan to expose a shell and a REST interface that can be used by the user to interact with the application.

## How will you demonstrate the usefulness of your tool.

We will be evaluating our systems by supplying a set of datasets and performing side by side serach on the application and splotlight search. We shall also be working on improving the performance of the system in whatever manner it would be possible. We will add screen-shots on our git-lab project page that will document how to install and how to use the tool. We plan to show a head-to-head comparison between searching for a file on your local machine with Spotlight (or similar Windows tool) versus the search tool we developed.

## A very rough time-line to show when you expect to finish what. (The time-line doesn't have to be accurate.)

At minimum, building a personal search tool for a user’s local machine that is better at finding relevant documents/files than the existing built-in search software. We want to make finding files on your machine faster and easier.

Before implementing Whoosh, the first thing to be developed is a document parser to scrape relevant information such as document title and text. Then the schema will be designed. Then an indexer will be implemented along with a scoring module (BM25). Finally, the interface will be created for the user to interact with. We plan to attack each of these tasks together, one by one, so that each of us get experience in each stage of the project. Between four and five weeks from now (a few weeks before the Progress report), we plan to meet to discuss our progress and increase/decrease our workload/expectations according to the difficulty of the process.
