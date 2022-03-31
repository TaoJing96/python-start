from flask import Flask, request, redirect, jsonify, abort

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():  # put application's code here
    if request.method == 'GET':
        print('GET')
    return 'Hello World!'


@app.route('/users/<int:id>')
def query_by_id(id):
    user = {'name': 'tj', 'age': 22}
    if id == 1:
        return jsonify(user)
    elif id == 2:
        return 'tt'
    else:
        raise RuntimeError


# 重定向
@app.route('/redirect')
def redirect_url():
    return redirect('https://www.baidu.com')


# 重定向
@app.route('/abort')
def abort_test():
    abort(404)


@app.errorhandler(404)
def my_error_handler(err):
    return '出现404%s' % err


if __name__ == '__main__':
    app.run()
