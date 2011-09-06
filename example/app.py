
from flask import Flask

app = Flask(__name__)

app.url_map.strict_slashes = False

# register views
from views import VIEWS
for view in VIEWS:
    app.register_blueprint(view, url_prefix=view.url_prefix)

@app.route('/')
def hello():
    return "server's working"

if __name__ == '__main__':
    app.run()
