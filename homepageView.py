from flask.views import MethodView


class homepageView(MethodView):
    
    def get(self):
        return "This is a GET to homepage admin"