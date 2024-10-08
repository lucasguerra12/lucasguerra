from flask import Flask, render_template

app = Flask(__name__)


@app.route('/pagina-especifica')
def pagina_especifica():
    return render_template('pagina_especifica.html')

@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
