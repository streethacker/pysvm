# -*- coding: utf-8 -*-

from flask import Flask, make_response
from fakeredis import FakeStrictRedis
from pysvm.svm import VerifyCodeManager

manager = VerifyCodeManager(redis_factory=lambda dsn: FakeStrictRedis())
app = Flask(__name__)


@app.route('/retrieve')
def retrieve():
    buf, h = manager.verify_code_create()
    resp = make_response(buf.getvalue())
    resp.headers['Content-Type'] = 'image/jpeg'
    return resp

if __name__ == '__main__':
    app.run()
