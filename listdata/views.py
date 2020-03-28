import sqlite3,os
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

TABLE = 'cvdata'
DB = 'data.db'
# possible ordering of keys
FIELDS = ['CreationDate','LastActivityDate', 'LastEditDate','Score','ViewCount']
# row headers
ALLFIELDS = ['AcceptedAnswerId', 'AnswerCount', 'Body', 'ClosedDate', 'CommentCount', 'CreationDate', 'FavoriteCount', 'Id', 'LastActivityDate', 'LastEditDate', 'LastEditorUserId', 'OwnerDisplayName', 'OwnerUserId', 'ParentId', 'PostTypeId', 'Score', 'Tags', 'Title', 'ViewCount']

def orderedlistview(request):
    VALIDKEY=True
    renderBody=False
    ordering='DESC'
    # for body rendering in view table
    if 'body' in request.GET:
        renderBody=True
    # Ascending or descending order of key
    if 'asc' in request.GET:
        ordering = 'ASC'
    
    ORDER = FIELDS[0]
    
    # check order_by value
    if 'order_by' in request.GET:
        if request.GET['order_by'] in FIELDS:
            ORDER = request.GET['order_by']
        else:
            VALIDKEY=False
    
    # build SQL query
    QUERY = "SELECT * FROM " + TABLE + " ORDER BY " + ORDER + " " + ordering
    conn = sqlite3.connect(DB)
    # print(QUERY)
    c = conn.cursor()
    table = [row for row in c.execute(QUERY)]
    conn.close()
    return render(request, 'list.html', {'table': table,
                    'fields': ALLFIELDS,
                    'valid': VALIDKEY,
                    'renderBody': renderBody})
                    
def searchview(request):
    renderBody=False
    if 'body' in request.GET:
        renderBody=True
    if 'q' not in request.GET:
        return HttpResponse('Please provide search term as ?q=')
    BASE_QUERY = "SELECT * FROM " +  TABLE
    Query_String = request.GET['q'] 
    QUERY = BASE_QUERY + " WHERE BODY LIKE '%" + Query_String +"%' OR TITLE LIKE '%" + Query_String + "%'"
    conn = sqlite3.connect(DB)
    print(QUERY)
    c = conn.cursor()
    table = [row for row in c.execute(QUERY)]
    conn.close()
    return render(request, 'search.html', {'table': table,
                    'fields': ALLFIELDS,
                    'row_count': len(table),
                    'renderBody': renderBody})