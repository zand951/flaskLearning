Notes: 

1. redirect(url_for(endpoint_name))
2. instead of app.route('/foo'), create a class, methods that could be called at named as http requests, def get, def post, etc. Then routing using app.add_url_rule('/home/', view_func=homepage.as_view('homepage_endpoint')) in main