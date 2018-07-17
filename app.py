from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/lifestyle')
def lifestyle():
    return render_template('lifestyle.html')

@app.route('/travel')
def travel():
    return render_template('travel.html')

@app.route('/about')
def about():
    return render_template('about.html')







if __name__ == '__main__':
 	app.run(debug=True)