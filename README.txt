




-Prcoessed in a relations database

date, channel, country, os, impressions, clicks, installs, spend, revenue



1: filter by time range (date_from / date_to is enough), channels, countries, operating systems
O/P:
--date         
--channels     http://127.0.0.1:8000/webapp/?search=adcolony
--countries    http://127.0.0.1:8000/webapp/?search=US
--operating systems   http://127.0.0.1:8000/webapp/?search=android

2: group by one or more columns: date, channel, country, operating system
O/P:
     http://127.0.0.1:8000/webapp/search=chartboost,ios

3:sort by any column in ascending or descending order
O/P:
     http://127.0.0.1:8000/webapp/?ordering=clicks

4: see derived metric CPI (cost per install) which is calculated as cpi = spend / installs
O/P: