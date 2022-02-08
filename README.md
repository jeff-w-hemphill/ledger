# ledger

This repo has been updated to work with `Python v3.8` and up.

### How To Run
1. Install `virtualenv`:
```
$ pip3 install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip3 install -r requirements.txt
```
5. Run initialization script
```
$ (env) python3 script.py
```

6. Finally start the web server:
```
$ (env) python3 app.py
```

## Tests
I used VS Code's Rest Client package to run GET and POST requests. See the "requests.rest" file.
