from flask.views import MethodView
from flask import *

class homeView(MethodView):
    
  
    def get(self,name):
        
        if name == 'admin':
            #value used for url_for is the endpoint
            return redirect(url_for('homepage_endpoint'))
        else:
            return f"This is a GET request for domain {name}"
    
    def post(self):
        return "This is a POST request for my homepage"
