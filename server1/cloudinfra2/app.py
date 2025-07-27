from flask import Flask
import pyfiglet
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    server_name = "Server 2"
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    region = "ap-south-1 (Mumbai)"
    uptime = "45 hours"

    figlet_text = pyfiglet.figlet_format(server_name)

    html = f"""
    <html>
    <head>
        <title>{server_name}</title>
        <style>
            body {{
                background: linear-gradient(135deg, #2c1e00, #ff9900);
                color: #ffffff;
                font-family: 'Courier New', Courier, monospace;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                text-align: center;
            }}
            .figlet {{
                color: #ffaa00;
                font-size: 22px;
                white-space: pre;
            }}
            .info {{
                margin-top: 20px;
                background-color: rgba(0,0,0,0.4);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px #ffaa00;
            }}
            h2 {{
                color: #ffffff;
            }}
        </style>
    </head>
    <body>
        <div class="figlet"><pre>{figlet_text}</pre></div>
        <div class="info">
            <h2>⚡ Welcome to {server_name} ⚡</h2>
            <p><strong>Hostname:</strong> {hostname}</p>
            <p><strong>IP Address:</strong> {ip}</p>
            <p><strong>Current Time:</strong> {now}</p>
            <p><strong>AWS Region:</strong> {region}</p>
            <p><strong>Uptime:</strong> {uptime}</p>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
