from flask import *
app = Flask(__name__)
app.secret_key = "secret"

import python.src.Andrew.index as Andrew
import python.src.Glenn.index as Glenn
import python.src.Insan.index as Insan
import python.src.Rhaylene.index as Rhaylene

Andrew.run(app)
Glenn.run(app)
Insan.run(app)
Rhaylene.run(app)

# Ryan
@app.route("/staff/inventory_manage", methods=['GET', 'POST'])
def inventory_manage():
    return render_template("Ryan/inventory_manage.html")
# END Ryan

app.run()
