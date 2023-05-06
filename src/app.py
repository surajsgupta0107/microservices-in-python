from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)


def get_hostname_and_ipaddr():
    try:
        hostname = socket.gethostname()
        ipaddr = socket.gethostbyname(hostname)

        return str(hostname), str(ipaddr)
    except:
        print("unable to get hostname and ip")

    return


@app.route("/")
def home():
    return "<h1>Jai Shri Ram</h1>"


@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )


@app.route("/index")
def index():
    hostname, ipaddr = get_hostname_and_ipaddr()
    return render_template("index.html", HOSTNAME=hostname, IPADDR=ipaddr)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
