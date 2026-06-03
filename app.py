
from flask import Flask
from module1 import app as jwt_app
from module2 import app as access_app
from module3 import app as guest_app

app = Flask(__name__)

for src in (jwt_app, access_app, guest_app):
    for rule in src.url_map.iter_rules():
        if rule.endpoint == 'static':
            continue
        view = src.view_functions[rule.endpoint]
        endpoint = f"{src.name}_{rule.endpoint}"
        app.add_url_rule(rule.rule, endpoint, view, methods=rule.methods)

@app.route('/')
def home():
    return {
      "routes":["/guest?uid=&pw=","/jwt?access_token=","/access?eat_token="]
    }

if __name__ == '__main__':
    app.run()
