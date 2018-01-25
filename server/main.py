from flask import Flask, request, json, Response

app = Flask(__name__)


#########################################################
#                    Controllers                       #
#########################################################

@app.route("/alive")
def alive():
    return "OK"


if __name__ == '__main__':
    port = int(9001)
    app.run(host='', port=port)
