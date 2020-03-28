# Ingesting CCV

The repository is a django project for selection test implementing the requirements.
> First step is to ingest this file in a sqlite database.

looking inside the `step1` folder we have `ingester.py` which can take an xml file and insert into sqlite3 database.
`ingester.py` has the methods
```
ingestintoDB(filename)
display()
```
> Write an endpoint to return these posts, by default it should be in chronological order. By way of a query string in the URL, these posts may also be ordered by view count or score.

After writing into the database, we make an endpoint to display the posts in chronological order. 
The online version is [here](http://savesubmissions.pythonanywhere.com) (hosted on pythonanywhere)
Query Parameters
 - `order_by` {'ViewCount', 'Score', 'LastActivityDate', 'LastEditDate', 'CreationDate'}
 - `body` if present will render the html in body column
 - `asc` the default ordering is descending, pass `asc` to make it ascending
 - 
Example Query: 
`http://savesubmissions.pythonanywhere.com/?&order_by=ViewCount&body&asc`

>  Write an endpoint to search these posts. Again, by way of a query string, filter the posts based on the presence of the search term, either in the title or body of the post.

The search endpoint is located at `/search`
Query Parameters
 - `q` pass the search string here
 - `body` if present will render the html in body column

Example Query
`http://savesubmissions.pythonanywhere.com/search?q=wuhan&body`