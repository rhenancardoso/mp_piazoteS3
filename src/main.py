from lib.microdot import Microdot, Response

app = Microdot()

@app.route('/')
def index(request):
    return '<h1>Hello, World!</h1>', {'Content-Type': 'text/html'}

@app.route('/shutdown')
def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'

if __name__ == '__main__':
    app.run(host='192.168.1.144', port=8080, debug=True)