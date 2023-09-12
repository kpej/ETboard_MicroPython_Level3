from microdot import Microdot
    
app = Microdot()

htmldoc = '''<!DOCTYPE html>
<html>
    <head>
        <title>Microdot Example Page</title>
        <meta charset="UTF-8">
    </head>
    <body>
        <div>
            <h1>Microdot Example Page</h1>
            <p>Hello from Microdot!</p>
            <p><a href="/shutdown">Click to shutdown the server</a></p>
        </div>
        
        <form action="/submit" method="POST">
          <label for="fname">First name:</label>
          <input type="text" id="fname" name="fname"><br><br>
          <label for="lname">Last name:</label>
          <input type="text" id="lname" name="lname"><br><br>
          <input type="submit" value="Submit">
        </form>

    </body>
</html>
'''


@app.route('/')
def hello(request):
    return htmldoc, 200, {'Content-Type': 'text/html'}


@app.route('/shutdown')
def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'

@app.route('/submit', methods=['GET', 'POST'])
def submit(request):    
    if request.method == 'POST':
        fname = request.form.get('fname')
        print(fname)
    return htmldoc, 200, {'Content-Type': 'text/html'}    


app.run(debug=True)
