#!/usr/bin/env python3
import psycopg2
import time
DBNAME = "news"
db = psycopg2.connect(database=DBNAME)
c = db.cursor()


def executequery(query):
    c.execute(query)
    res = c.fetchall()
    return res


def printing(res):
    for art in res:
        print "\"%s\" -- \"%s\" views" % (art[0], art[1])


def printingerror(res):
    for art in res:
        error = "% errors"
        #print(art[0], "--", "%.2f" % art[1], "% errors")
        print "%s -- %.2f%s" % (art[0], art[1], error)


def popularthreearticles():
    q1 = ("select title, count(title) as views from articles,log "
          "where log.path = concat('/article/',articles.slug) "
          "group by title order by views desc limit 3;")
    res = executequery(q1)
    print "What are the most popular three articles of all time?"
    printing(res)

    
def populararticleauthor():
    q2 = ("select authors.name, count(*) as views from articles,log,authors "
          "where log.path = concat('/article/',articles.slug) and articles"
          ".author = authors.id group by authors.name order by views desc;")
    res = executequery(q2)
    print "Who are the most popular article authors of all time? "
    printing(res)


def error():
    q3 = ("select date(time) as Day, "
            "(count( case when status ilike '%404 NOT FOUND%' then 1 "
            "else null end) / cast(count(date(time)) as float))*100 "
            "as percentage from log group by Day having cast "
            "(((count( case when status  ilike '%404 NOT FOUND%' then 1 "
            "else null end) / cast(count(date(time)) as float))*100)"
            "as integer) > 1 order by Day;")
    res = executequery(q3)
    print "On which days did more than 1% of requests lead to errors?"
    printingerror(res)


popularthreearticles()
populararticleauthor()
error()
db.close()
