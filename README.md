# ntu-course-planning-system
This project initiated by James Yang and Taoyu Chen aims to provide NTU students with a website where they could plan their courses in the most convenient manner. It automatically generates possible index combinations of the input courses without any clash.

The server is written in Python and Django while the data are stored in MySQL.
## Setup
### Install Python and pip
If you don't have Python or pip on your machine, please refer to a tutoiral [here](https://github.com/jarrettyeo/NTUOSS-PythonPipInstallation) written by [Jarrett](https://github.com/jarrettyeo).
### Required dependencies
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Django](https://www.djangoproject.com)
- [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/)
- [Requests](http://docs.python-requests.org/en/master/)
#### pip commands
```
$ pip3 install beautifulsoup4        # Install Beautiful Soup
$ pip3 install Django                # Install Django
$ pip3 install mysql-connector       # Install MySQL Connector
$ pip3 install requests              # Install Requests
```
### Install MySQL on your computer
To install MySQL on your machine, please refer to the official tutorial [here](https://dev.mysql.com/doc/mysql-getting-started/en/) or a shorter tutorial [here](http://www.mysqltutorial.org/install-mysql/) (only for Windows users). 

MySQL Workbench is optional but highly recommanded for those who are new to MySQL, as it provides a nice and friendly GUI. You can find the official tutorial to install MySQL Workbench [here](https://dev.mysql.com/doc/workbench/en/wb-installing.html). After installing MySQL Workbench, refer to this [tutorial](http://www.mysqltutorial.org/how-to-load-sample-database-into-mysql-database-server.aspx) on how to set up connection for the first time. 

It might take some time and effort to install all of these. If you encounter any error in the process, don't panic! Google and Stack Overflow are your best friends. Let's install MySQL, once and for all!
### Install git on your computer
If you don't have git on your machine, please refer to a tutoiral [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and install it.

If you haven't used git/github before, you're strongly encouraged to go over the git tutorial [here](https://sp18.datastructur.es/materials/guides/using-git.html) written by UCB CS 61B course staff, as we'll be using git throughout the entire project.
## Host the website on your machine
- Open you terminal/command line and naviage to the directory of your choice
- Clone this repo:
```
git clone https://github.com/Jamesyang2333/ntu-course-planning-system
cd ntu-course-planning-system
```
- In your MySQL, create a database scheme named "courses". In the "courses" database, create a table named "allcourses" using the following SQL script. The table would be used to store NTU course data.
```
CREATE TABLE `allcourses` (
  `course` varchar(10) DEFAULT NULL,
  `indexNo` int(11) DEFAULT NULL,
  `session1` varchar(11) DEFAULT NULL,
  `tag1` varchar(10) DEFAULT NULL,
  `week1` int(11) DEFAULT NULL,
  `session2` varchar(11) DEFAULT NULL,
  `tag2` varchar(10) DEFAULT NULL,
  `week2` int(11) DEFAULT NULL,
  `session3` varchar(11) DEFAULT NULL,
  `tag3` varchar(10) DEFAULT NULL,
  `week3` int(11) DEFAULT NULL,
  `session4` varchar(11) DEFAULT NULL,
  `week4` int(11) DEFAULT NULL,
  `tag4` varchar(10) DEFAULT NULL,
  `session5` varchar(11) DEFAULT NULL,
  `week5` int(11) DEFAULT NULL,
  `tag5` varchar(10) DEFAULT NULL,
  `session6` varchar(11) DEFAULT NULL,
  `tag6` varchar(10) DEFAULT NULL,
  `week6` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8
```
- Update your database password in three config.ini files. The paths of the three files are "ntu-course-planning-system/config.ini", "ntu-course-planning-system/simplesite/config.ini" and "ntu-course-planning-system/coursearrangement/config.ini"
- Host the website using the command:
```
python3 manage.py runserver
```
- Now go to [http://127.0.0.1:8000/home](http://127.0.0.1:8000/home/), and you'll see NTU Course-Planning System hosted on your own machine! Try it out and we are good to go!
