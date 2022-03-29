from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask!'

def about():
    return 'About this website'

app.add_url_rule('/about', 'about', about)
    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
