## Twitter - ElasticSearch Application

**Launch ElasticSearch Instance**
Navigate to 'elasticsearch-6.3.0/bin/' folder and run command : 
```
elasticsearch
```

**For loading and search of tweets**
Navigate to 'script' folder and run commands :
For Loading of tweets : 
```
python load.py"
```
For Search of tweets  : 
```
python search.py
```

**Run the web app server** 
Inside the project folder,run command : 
```
python -m http.server 8000
```
and navigate to http://localhost:8000