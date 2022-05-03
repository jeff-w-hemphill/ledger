# ledger (Peach Finance)

This repo has been updated to work with `Python v3.8` and up.

### How To Run
1. Clone repo

```
git clone https://github.com/jeff-w-hemphill/ledger.git
```
```
cd ledger
```
2. Install `virtualenv`:
```
pip3 install virtualenv
```

3. Open a terminal in the project root directory and run:
```
virtualenv env
```

4. Then run the command:
```
source env/bin/activate
```

5. Then install the dependencies:
```
pip3 install -r requirements.txt
```
6. Run initialization script
```
python3 script.py
```

7. Finally start the web server:
```
python3 app.py
```
For landing page client go to:
```
http://127.0.0.1:5000
```

## Tests
I used VS Code's Rest Client package to run GET and POST requests. See the "requests.rest" file.
