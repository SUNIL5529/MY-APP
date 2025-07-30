from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Welcome to the Home Page</h2><a href="/register">Go to Registration</a>'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        return render_template('success.html', name=name, email=email)
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)