from learnall import fak
#from flask import make_response

@fak.route('/hellovtk')
def hellovtk():
    response = fak.make_response('Hello VTK!')
    response.mimetype = "text/plain"
    return response

