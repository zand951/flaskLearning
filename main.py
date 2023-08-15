from flask import Flask
from homeView import homeView as home
from homepageView import homepageView as homepage

app = Flask(__name__)

app.add_url_rule('/home/<name>', view_func=home.as_view('home_endpoint'))
app.add_url_rule('/home/', view_func=homepage.as_view('homepage_endpoint'))

if __name__ == '__main__':
    print("hello world")
    app.run(debug=True)

