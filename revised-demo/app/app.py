from flask import Flask, render_template, jsonify
import psutil
import socket
import threading
import time
import getpass

app = Flask(__name__)

cpu_usage_history = []

def get_system_info():
    ip_address = socket.gethostbyname(socket.gethostname())
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.used / (1024 * 1024)  # Convert bytes to MB
    net_io = psutil.net_io_counters()
    net_stats = {
        'bytes_sent': net_io.bytes_sent / 1024,  # Convert to KB
        'bytes_recv': net_io.bytes_recv / 1024   # Convert to KB
    }
    return ip_address, cpu_usage, memory_usage, net_stats

def collect_cpu_usage():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        if len(cpu_usage_history) >= 10:
            cpu_usage_history.pop(0)
        cpu_usage_history.append(cpu_usage)
        time.sleep(1)

threading.Thread(target=collect_cpu_usage, daemon=True).start()

@app.route('/')
def index():
    user_name = getpass.getuser()  # Get the system user's name
    ip_address, cpu_usage, memory_usage, net_stats = get_system_info()
    return render_template('result.html', name=user_name, ip_address=ip_address, cpu_usage=cpu_usage, memory_usage=memory_usage, net_stats=net_stats)

@app.route('/cpu_history')
def cpu_history():
    return jsonify(cpu_usage_history)

@app.route('/live_data')
def live_data():
    _, cpu_usage, memory_usage, net_stats = get_system_info()
    return jsonify({
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'net_stats': net_stats
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')