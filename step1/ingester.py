import sqlite3
import pathlib
import os
import xml.etree.ElementTree as ET

TABLE = 'cvdata'
DB = 'data.db'
FIELDS = ['AcceptedAnswerId', 'AnswerCount', 'Body', 'ClosedDate', 'CommentCount', 'CreationDate', 'FavoriteCount', 'Id', 'LastActivityDate', 'LastEditDate', 'LastEditorUserId', 'OwnerDisplayName', 'OwnerUserId', 'ParentId', 'PostTypeId', 'Score', 'Tags', 'Title', 'ViewCount']

def xmltree(file):
    
    tree = ET.parse(file)
    return tree
    
def ingestIntoDB(file):
    
    if not os.path.exists(file):
        print("File does not exist")
        return
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    values = []
    root = xmltree(file).getroot()
    # set of all fields
    # s = set()
    for row in root:
        row_values = []
        for field in FIELDS:
            if field in row.attrib:
                row_values.append(row.attrib[field])
            else:
                row_values.append(None)
            # s.add(field)
        # print(row_values)
        values.append(tuple(row_values))
    c.executemany('INSERT INTO ' + TABLE + ' VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', values)
    conn.commit()
    print("Ingested xml file successfully")
    # print(sorted(s))
    conn.close()
def display():
    
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    z = [row for row in c.execute('SELECT * FROM ' + TABLE)]
    print(z)
    conn.close()
    
ingestIntoDB('data.xml')
display()