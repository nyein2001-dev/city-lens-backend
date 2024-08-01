from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://u1f1ppkqdof6rb:p63cc0a4c9d8ba05114ab4eac7f77c30c39ae05a7e1dd2c806485a0df98c51a2a@c67okggoj39697.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/db062dgbvu3ma4'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
