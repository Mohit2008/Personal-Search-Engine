## Technology review :

This technology review aims at covering the area of "Useful software toolkits for processing text data or building text data applications". As we know that there are already so many tools out there in market which aims at performing fast and efficient search retrieval task which could be used across many areas like searching for web pages, searching for documents, searching for text and many such related areas. What this paper is focusing on is to compare existing technologies or tools that could be used for performing search on your local desktop which is kind of a personal search engine that aims at performing full text base indexing and searching.

Organizing data on a computer is a difficult job, and in most cases is the sole responsibility of the user. However, even the most organized user may find it nearly impossible to arrange their files in a way that makes it easy to find information. Because the underlying file systems offer only one way of organizing information, users must resort to special tools to search for what they want. The problem is that most search tools can be slow and limited in how they do their search.

To introduce about this application just imagine this system like that of Google where you type in a query which in some case would be either general when the user wishes to explore information or would be targeted when the user know what document he wants. Similar to that we thought of coming up with a system which not only aims to perform a full text based search but also gives full access to control the application by selecting a drive/directory where a user wants to perform the search and also use this application across multiple platform which has python installed on it. Since for any document which is in a local file system what is most important is to match the text in the document with the given query and then generate a set of relevant documents, for which system must be capable of dealing with incomplete query , ambiguity, stemming of words and building a full document indexer.

We shall consider comparing this application to the current desktop search engines provided by Windows and MacOs.


## Windows

SearchIndexer.exe is the Windows service that handles indexing of files for Windows Search, which fuels the file search engine built into Windows that powers everything from the Start Menu search box to Windows Explorer, and even the Libraries feature. SearchIndexer.exe uses lot of RAM and CPU.

There are options to reduce indexing by limiting the search, for example limit the search to file name matching the search criteria not the file content. So, this reduces quality of the search engine in order to save RAM and CPU space.

There are many alternate search application on windows for e.g. Lokeen, Everthing, Listary, GrepWin etc. These application claim to be better than native explorer. However, all these applications are OS dependent . Some of them are even specific to windows version as well. We aim to build a fast, light weight search engine that runs on any OS.


## MacOs

MacOs uses a search engine known as Spotlight search.Spotlight is a fast desktop search technology that allows users to organize and search for files based on metadata. Spotlight is extensible, allowing developers to provide metadata importers for their application’s documents.

Metadata is data about a file, rather than the actual content stored in the file.Metadata can include familiar information such as an asset’s author and modification date but it can also be keywords or other information that is custom to a particular asset.

Every time a file is created, modified or deleted, the kernel notifies the Spotlight engine that it needs to update the system store for changed file. Using Launch Services, Spotlight determines the uniform type identifier of the file and attempts to find an appropriate importer plug-in. If an importer exists and is authorized, it is loaded and passed the path to the file.

Spotlight queries are made by client applications, such as the Finder. The application constructs the appropriate query expression for the search, specifies the scope of the search, how the data is to be grouped when it is returned, and then executes the query.

So the main idea behind the spotlight search engine is the use of metadata information and thus it does not support full text based indexing which is the main thing our application aims to solve.


### Personal Search Engine


For the purpose of this project we will implement it in python and package it in wheel format so that it can run on any Operating System.
We will be using Whoosh(open source code search library), useful for a flexible or pure-Python search engine.

Whoosh is fast and it uses only pure Python, both indexing and searching is done in Python. Whoosh will run anywhere Python runs, without requiring a compiler. Whoosh creates very small indexes compared to many other search libraries, it's really light weight.
By default, Whoosh uses the Okapi BM25F ranking function, but like most things the ranking function can be easily customized.

We reviewed the following before finalizing Whoosh for our project.


### SOLR

Solr is an open source enterprise search platform, written in Java. It's features include full-text search, highlighting, real-time indexing, dynamic clustering, database integration, NoSQL features. Solr runs as a standalone full-text search server and has REST-like HTTP/XML and JSON APIs. In order for Solr to search a document, the operations follow these steps: (1) Convert the document into machine-readable format (Indexing), (2) Understand query terms entered by the user, (3) Map user query to documents stored in the database, and (4) When the engine searches the indexed documents, the output is ranked according to relevance.

Pros	: Solr is complicated and by far the most comprehensive search solution.

Cons	: Its implemented in Java and would need java environment to be installed on the system along with Python. It's heavy weight.

```
Query "machine"
Size of Corpus:9.9mb
No of files indexed: 45
Indexing time:Indexing completed in 2.78180384636 seconds
Query Results:Hits 10
Searching:Searching completed in 0.000238976 seconds
Size of index created:7.1mb
Supported Features: Highlighted text, Scoring, Incremental index update, boolean query operators,position highlighting,
Missing features: schema can only hold the content, different parsers, spell check
```


### Xapian

Xapian is an open source probabilistic information retrieval library and a full text search engine library. It is written in C++, but has binding to allow use in Perl, Python, PHP, Java, and other languages. Xapian is  a very portable across operating systems, able to be ran on Linux, OS X, Windows, FreeBSD, and several other OS. Xapian has a number of features including: (1) When updating a database, if it fails in the middle of a transaction, the database is guaranteed to remain in a consistent state, (2) Simultaneous search and update - new documents become visible for use immediately, (3) Spelling correction, and (4) Ensuring more relevant documents are listed first (probabilistic ranking).

Pros	: Xapian is very fast and allows adding advanced indexing and search facilities.

Cons	: It has licensing limitations. It only has support for python2 , we found it difficult to run through python3. Also it has dependencies on c++ code which might be a problem to the users in terms of the installation.

Our analysis with Xaplin worked out to be very interesting and fast. The indexing took no time as compared to others and search was fast. Here are the stats:

```
Query "machine"
Size of Corpus:9.9mb
No of files indexed: 45
Indexing time:Indexing completed in 4.78180384636 seconds
Query Results:Number of documents matching query: 17
Searching:Searching completed in 0.000494956970215 seconds
Size of index created:9.2mb
Supported Features: Highlighted text, Scoring, Incremental index update, boolean query operators, spell check
Missing features: position highlighting, schema can only hold the content, different parsers
```


### Metapy
Metapy is a python wrapper over c++ meta library which is used across various domain to do search task, text categorization, text mining, nlp and much more. Data is stored in a disk index and meta is capable of creating both forward and inverted index.

Pros : It has support for many rankers and also quite fast as it uses c++ .

Cons : Metapy is a wrapper around a c++ meta implementation and since we want to keep the connivance of portability, handling the c++ part would be an overhead.


### NLTK :

Natural Language Toolkit (or NLTK) is an open source suite of python libraries for symbolic and natural language processing for the English language. NLTK supports classification, tokenization, stemming, tagging, parsing, and semantic reasoning applications. NLTK has good support for doing natural language processing but for a search task on a local machine such capabilities will be of no use.

Pros :It comes with a good support for NLP which can be useful for a search engine.Nltk has good support for parsing text from different file extension like pdf, html, docx.

Cons :Its a very general library that dosent have much support for full indexing and searching although it supports simple search task. Since it does not have support for full text based index ,searching can only happen with the documents that are loaded in memory and it dosent creates any index. So such use cases will be inappropriate to handle the local desktop file searching scenario. Also there is not much support for ranking or scoring documents returned from the search results.

Here is a small performance stat as to how searching in nltk worked for a small data-set on text files

```
Query "mining"
Size of Corpus:9.9mb
No of files indexed: 45
Indexing time:Indexing completed in 28.37328338623047 seconds
Query Results:Displaying 2 of 25 matches:
Searching:Searching completed in 28.37452530860901 seconds
Size of index created:Does not creates any index
Supported Features: Highlighted text, different parsers
Missing features: position highlighting, scoring, spell check
```
What we get out is simple plain sentences that has the occurrence of the word "mining", which is of not much use to a user whose purpose is to locate the file and the now the surrounding text.


## LDSE (Local Desktop Search Engine)

LDSE was developed with an aim to give a desktop owner the power to search through any document that is there in his local drive. We all know that we often keep flooding our systems with lot of data at various points of time and when we wish to search for the documents we end up getting to many anonymous results. This is because while searching what we remember is the content and not the file name and currently no OS has support to provide full text based searching. Also with different OS you see different interfaces and different mechanism through which they try to do the searches. LDSE solves all these problem by giving you an application that can be shipped across any platform and reused.

LDSE is designed to operate for various file format like[".txt",".html",".htm",".docx",".pdf"]. If you do wish to perform a bash indexing you might have to give some time as this is a time taking process , for incremental indexing we have given support in our application where in you can keep adding the documents to the index as an when you add them in drive also you can delete the indexes of the file that has been been removed from the file system. LDSE has an intelligent way of identifying such changes and can automatically update your indexes when a file is deleted or added.

LDSE is build on python3 and is made to operate in 2 ways.One way is using the shell interface and the other is using your browsers. Both of them are made compatible to run on any OS. LDSE also is developed to make you understand more about your system by knowing the system capabilities and configurations. We have given an option to know your system in the shell interface.

LDSE works by searching for all the target supported files that are there in your search directory and then parse them. Files of different formats have different parsers which are tuned to extract the text from any document type. Once you have the text data ready we push the data to the woosh which does the job of creating inverted index. LDSE will create the index once and then for every subsequent run it shall use the same index to perform future searches. Once we have indexes loaded in memory the shell interface will start up and will look like"

```
***Welcome to the CLI for Search Engine utility commands! This is an online help utility.
the command sehelp() offers a short introduction***
Search Engine cli>
```


```
Query "mining"
Size of Corpus:9.9mb
No of files indexed: 45
Indexing time:Indexing completed in 12.085040807723999 seconds
Query Results:Displaying top 10 results
Searching:<Top 10 Results for Term('content', 'mining') runtime=0.0019794980762526393>
Size of index created:9.1mb
Supported Features: Highlighted text, spell check, incremental indexing, position highlighting
Missing features: boolean query operators, different parsers
```

