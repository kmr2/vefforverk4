from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
        the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

        return """
        <h1>Hello heroku</h1>

        <p><a href="/sida2" title="Síða 2">Síða 2 </a> |
        <a href="/sida3" title="Síða 3">Síða 3 </a></p> 

        <p>It is currently real nibba hours.</p>

        <img src="http://loremflickr.com/600/400/dog,cat/all">
        """.format(time=the_time)

@app.route('/sida2')
def page2():
        return """
        <h1>hér er önnur síða</h1>

        <p><a href="/" title="Síða 1">Síða 1 </a> |
        <a href="/sida3" title="Síða 3">Síða 3 </a></p> 

        <p>It is currently real nibba hours.</p>

        <img src="http://loremflickr.com/600/400/ferret/">
        """
    
@app.route('/sida3')
def page3():
    return render_template('sida3.html')



if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)