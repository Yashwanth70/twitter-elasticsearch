## Twitter - ElasticSearch Application

**Launch ElasticSearch Instance**(http://localhost:9200/)
Navigate to 'elasticsearch-6.3.0/bin/' folder and run command : 
```
elasticsearch
```

**For loading and search of tweets**
Navigate to 'script' folder and run commands :
For Loading of tweets : 
```
python load.py
```
For Search of tweets  : 
```
python search.py
```

**Run the server for api's between web app and elasticsearch**(http://localhost:5000/)
Navigate to 'apis' folder and run command :
```
python api.py
```

**Run the web application server** 
Inside the project folder,run command or load index.html to browser: 
```
python -m http.server 8000
```
and navigate to http://localhost:8000