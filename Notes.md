**Views that require your users to be logged in can be decorated with the login_required decorator:**
```py
@app.route("/settings")
@login_required
def settings():
    pass
```