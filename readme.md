**Convert Your JSON File to Sqlite file**
==========

>   Clone the project or download to your local file
>  Enter the project directory
>  Run `pip install -r requirements.txt`

This will setup all the necessary files and run the server

    python manage.py runserver
This will run in localhost by default i.e. http://127.0.0.1:8000 if you want to run in local IP then go to settings.py and add your local ip assigned to your computer in AllowedHost in settings.py 

    ALLOWED_HOSTS = ['192.168.0.100']
and then run     `python manage.py runserver 192.168.0.100:8000`

The result will be

![enter image description here](https://github.com/yuviii/jsontosqlite-Webview-/blob/master/screenshots/Screenshot%202018-04-12%2013.59.31.png?raw=true)

After upload 
![enter image description here](https://github.com/yuviii/jsontosqlite-Webview-/blob/master/screenshots/Screenshot%202018-04-12%2013.59.57.png?raw=true)

The sample json file to create table and adding data for table are provided in [JSON Sample folder](https://github.com/yuviii/jsontosqlite-Webview-/tree/master/samplejson)
Here table is created as tables.json and data is inserted as in datas.json. The schema in table is the key in object whereas the object name is the table name.

Happy coding. Any contribution is heartly welcomed and for any queries
[Yubaraj Poudel @Author](yubarajpoudel708@gmail.com)
