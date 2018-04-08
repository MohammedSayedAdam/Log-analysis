Logs Analysis
Project Description
This is the third project for the Udacity Full Stack Nanodegree. In this project, a large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data. The project mimics building an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site.
To Run:
1- you should have Python2 or Python3
2- you should have Vagrant and Virtual Box
3- you should have the database
3- run on the tereminal vagrant up to boot VM
4- log in it with vagrant ssh
5- run "psql -d news -f newsdata.sql" to display and load the database
6- finally run "python3 newsdata.py" this command to execute