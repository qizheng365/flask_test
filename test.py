from hello import app2
from flask import current_app

app2_ctx = app2.app_context()
app2_ctx.push()
print(current_app.name)
app2_ctx.pop()
