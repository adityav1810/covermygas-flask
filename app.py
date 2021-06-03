from flask import Flask,render_template



app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/buy')
def buy():
    return render_template('buy.html')


@app.route('/sell')
def sell():
    return render_template('sell.html')

@app.route('/team')
def team():
    return render_template('team.html')
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)