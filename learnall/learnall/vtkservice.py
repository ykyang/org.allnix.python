from learnall import app

@app.route('/hellovtk')
def hellovtk():
    return 'Hello VTK!'
