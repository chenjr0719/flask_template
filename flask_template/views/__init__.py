from flask_template import app
from flask_template.views.admin import admin_blueprint
from flask_template.views.v1.users import v1_users_api

app.register_blueprint(admin_blueprint)
app.register_blueprint(v1_users_api)
