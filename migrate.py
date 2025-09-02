from directory import db, app
from directory.models import User
app.app_context().push()
db.drop_all()
db.create_all()