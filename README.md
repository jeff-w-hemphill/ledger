# ledger

This repo has been updated to work with `Python v3.8` and up.

### How To Run
1. Install `virtualenv`:
```
pip3 install virtualenv
```

2. Open a terminal in the project root directory and run:
```
virtualenv env
```

3. Then run the command:
```
source env/bin/activate
```

4. Then install the dependencies:
```
pip3 install -r requirements.txt
```
5. Run initialization script
```
python3 script.py
```

6. Finally start the web server:
```
python3 app.py
```

## Tests
I used VS Code's Rest Client package to run GET and POST requests. See the "requests.rest" file.
