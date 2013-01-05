#!/bin/python

import sqlite3 as lite

con = lite.connect('wordlist.db')

cur = con.cursor()

wordFile = open('word_list.txt')

cur.execute('DROP TABLE WORDLIST')
cur.execute('CREATE TABLE WORDLIST(word TEXT)')

for word in wordFile.readlines():
    cur.execute("INSERT INTO WORDLIST(word) VALUES('%s')" % word.strip())

con.commit()
con.close()
