# Python Web Server

SCS2205 Computer Networks I

## Configurations
In the server.py file:

### These are the default configurations, modify them as needed:
```
HOST = "127.0.0.1" 
PORT = 2728
ROOT = "C:\\Users\\srvnn\\Downloads\\htdocs\\"
```

## Run server locally

Run the below command using command prompt from the directory where the server.py file is located

```
python server.py
```

## Viewing the pages

Copy and paste the below URLs in your web browser to view the pages.
_You can also use_ *localhost* _instead of 127.0.0.1_
```
http://127.0.0.1:2728/
http://127.0.0.1:2728/about.php
http://127.0.0.1:2728/contact.php
http://127.0.0.1:2728/text.php
```
## NOTE

This file is made for windows systems, if you are running ona Linux machine or Mac, please modify the backslashes for directory identification in the *ROOT* variable in line 6 and for *webpages* in line 22