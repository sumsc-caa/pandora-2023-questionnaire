# third-party packages
from flask import Flask
from flask import render_template
from flask_htmlmin import HTMLMIN

# local files
from service import blueprint


app = Flask(__name__)
app.config['MINIFY_HTML'] = True
htmlmin = HTMLMIN(app, remove_comments=True)
app.register_blueprint(blueprint)

@app.route("/example")
def example():
    """样例问卷，最终会删除本页面"""
    return render_template("example.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
