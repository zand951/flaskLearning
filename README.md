Notes: 

1. redirect(url_for(endpoint_name))

2. instead of app.route('/foo'), create a class, methods that could be called at named as http requests, def get, def post, etc. Then routing using app.add_url_rule('/home/', view_func=homepage.as_view('homepage_endpoint')) in main

3. https://www.w3cschool.cn/flask/flask_http_methods.html tutorial on how to handle different http request

4. What about static files? 
    We first create a static folder, containing all the static content
    Then use url_for() like this : url_for('static', filename = 'hello.js')

5. Get response using request, then pass as param to render_template
  https://www.w3cschool.cn/flask/flask_sending_form_data_to_template.html

6. Cookies are temp or perm data that stores during the session so the user can log in next time automatically, or save the current session data. 

    ```
    from flask import Flask, make_response, request # 注意需导入 make_response

    app = Flask(__name__)

    @app.route("/set_cookies")
    def set_cookie():
        resp = make_response("success")
        resp.set_cookie("key", "stuff you wanna save",max_age=3600)
        return resp

    @app.route("/get_cookies")
    def get_cookie():
        cookie_1 = request.cookies.get("key")  # 获取名字为Itcast_1对应cookie的值
        return cookie_1

    @app.route("/delete_cookies")
    def delete_cookie():
        resp = make_response("del success")
        resp.delete_cookie("key")

        return resp

    if __name__ == '__main__':
        app.run(debug=True)
    ```
5. A smart way of organizing routing: https://www.w3cschool.cn/flask/flask-qcki3get.html


0
 