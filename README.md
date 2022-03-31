# json_server <br>

<h3>Active endpoints:</h3>
/&lt;name&gt;     <-- takes an argument in the url and returns json entry containing the argument <br>
/&lt;name&gt;/post    <-- same except this route accepts post request instead <br>
                 
/get_users <br>
/get_users/post <br>
                 
/get_animals <br>
/get_animals/post <br>

```
git clone this url
cd json_server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 json_server.py
```
