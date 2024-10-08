

@app.route('/paginahome')
def pagina_especifica():
    return render_template('baseflask.html')



if __name__ == '__main__':
    app.run(debug=True)









@app.route('/paginahome')
def pagina_especifica():
    return render_template('baseflask.html')

if __name__ == '__main__':
    app.run(debug=True)
