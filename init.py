from flask import *
app = Flask(__name__)
app.secret_key = "secret"

import python.src.Andrew.index as Andrew
import python.src.Glenn.index as Glenn
import python.src.Insan.index as Insan
import python.src.Rhaylene.index as Rhaylene
import python.src.Ryan.index as Ryan

Andrew.run(app)
Glenn.run(app)
Insan.run(app)
Rhaylene.run(app)
Ryan.run(app)

app.run()
