from flask import Flask, redirect, url_for
import os
import psutil
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('htop')) 

@app.route('/htop')
def htop():

    username = os.getenv('USER')

    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    output = f"""
    <h1>Server Info</h1>
    <p>Name: Rohan</p>
    <p>Username: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    <h2>System Resource Usage</h2>
    <p>CPU Usage: {cpu_usage}%</p>
    <p>Memory Usage: {memory_usage}%</p>
    """

    return output
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)