this s the webflask sde to the arbnb webste
flask set up https://www.youtube.com/watch?v=Aa-F6zqLmig
==========================================================
https://stackoverflow.com/questions/51025893/
flask-at-first-run-do-not-use-the-development-server-in-a-production-environmen
==========================================================
traditionally while utilizing html code as part of python, the example gives..

from flask import Flask

@app.route('/')
def message():
  return <h1>"Hello HBNB"</h1>

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="5000")


this handles the error code that might be seen while running flask in the terminal\n
>>> "Use a production WSGI server instead."
