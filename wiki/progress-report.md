## Progress Report:

### What has been done?

On the front end, a simple user interface has been built using HTML, CSS, JavaScript, and Flask framework. The UI displays a search bar and makes an ajax call of the search function every time search terms change (e.g. typing a character, deleting a character, copy/pasting or cutting characters). When the call successfully receives a response, file names get displayed below the search bar. The names show up as links in order of relevance depending on the query (search) term(s).

As far as the backed of the application is concerned we have added the business logic of scanning the files in the user directory , where the files can be of multiple type(We support .pdf, .html,.docx, .txt formats), each format has its own parsers to extract the text data out from it once the parsing is done we then use the data to perform the word segmetation, stemming and create an index out of it. There is a provision through which if any of the files get added or deleted or modified we update the existing index and dont recreate it every-time. A nice shall interface has been implemented which has support of performing all these actions using its commands. Also we now have a bash script that packages our application in wheel.

### What remains to be done?

On the UI side, more information needs to be displayed about each file found in a search, such as the path to the file, size, and the date modified. Also, if possible, the user should have a way to view the file (or its location) upon clicking the link with its name. This task has posed a challenge that will be discussed in the project barriers section.

The evaluation of application and its deployement is still pending to be done.



### Any barriers in achieving the proposed project goal?


Due to security reasons, browsers currently don't allow loading local files. This has been a barrier to implementing the functionality that allows a user to click on the file link on the search engine page to open the file. Some of the proposed solutions that are being explored include: (1.) attempting to implement this functionality on the backend (using python), (2.) requiring users to install one of the browser extensions that make loading local files possible (e.g. LocalLinks), or (3.) scraping this functionality altogether and only displaying a non-clickable path to the file in the search results.
