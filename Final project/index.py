from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import re

app = Flask(__name__, static_url_path="/static")
CORS(app)

#Route to handle divider
@app.route("/divider", methods=["POST"])
def divider():
    # Fetch data from front-end
    data = json.loads(request.data)
    resistorZ1 = data.get("z1", 0)
    resistorZ2 = data.get("z2", 0)
    voltageIn = data.get("voltageIn", 0)
    
    # Create a net list file
    with open("divider.cri", "w") as divider:
        divider.write("voltage divider netlist\n")
        v1 = "V1 in 0 " + str(voltageIn) + "\n"
        divider.write(v1)
        r1 = "R1 in out " + str(resistorZ1) + "\n"
        divider.write(r1)
        r2 = "R2 out 0 " + str(resistorZ2) + "\n"
        divider.write(r2)
        divider.write(".control\nop\nprint allv\n.endc\n.end\n")
        divider.close()
    
    os.system("ngspice divider.cri -b -o dividerlog")

    resultVoltage = ""
    with open("dividerlog", "r") as result:
        #items = re.findall("out = .*$", result, re.MULTILINE)
        for line in result:
            if "out =" in line:
                resultVoltage = str(re.search(r"\d+\.\d+[e][\+-]\d+", line).group())
        result.close()

    return jsonify({"result":resultVoltage})
            


#Default route
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def default(path):
    return "<h1>Welcome!</h1>"

if __name__ == "__main__":
    app.run()