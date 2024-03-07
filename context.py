from flask import Flask, current_app, request

app = Flask(__name__)

request_cntx = app.test_request_context()
request_cntx.push()

print(request)

request_cntx.pop()