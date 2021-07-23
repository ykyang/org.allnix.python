from learnall import fak # Flask object

@fak.route('/hello')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    fak.run()
