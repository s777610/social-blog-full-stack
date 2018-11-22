
from social_blog import create_App_Db


app, db = create_App_Db()

# create db and all table before request, unless they exist already
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)