# ntu-course-planning-system
This project initiated by me and Taoyu Chen aims to provide NTU students with a website where they could plan their courses in the most convenient manner. It automatically generates possible index combinations of the input courses without any clash.

The server is written in Python and Django while the data are stored in MySQL.
## Setup
### Install Python and pip
If you don't have Python or pip on your machine, please refer to a tutoiral [here](https://github.com/jarrettyeo/NTUOSS-PythonPipInstallation) and install them.
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
To install MySQL on your own machine, please refer to the official tutorial [here](https://dev.mysql.com/doc/mysql-getting-started/en/) or a shorter tutorial [here](http://www.mysqltutorial.org/install-mysql/) (only for windows users). 
MySQL Workbench is optional but highly recommanded for those who are new to MySQL, as it provides a nice and friendly GUI. You can find the official tutorial to install MySQL Workbench [here](https://dev.mysql.com/doc/workbench/en/wb-installing.html). After installing MySQL Workbench, refer to this [tutorial](http://www.mysqltutorial.org/how-to-load-sample-database-into-mysql-database-server.aspx) on how to set up connection for the first time. 
It might take some time and effort to install all of these. If you encounter any error in the process, don't panic! Google and Stack Overflow are your best friends. Let's install MySQL once and for all!
