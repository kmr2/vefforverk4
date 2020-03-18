from flask import Flask, render_template, session, url_for, request, redirect, escape
import os

app = Flask(__name__)

app.secret_key = os.urandom(8)
print(os.urandom(8))

# vörulisti
vorur = [
        [0,'Peysa','peysa.jpg',1500],
        [1,'Skór','skor.jpg',3500],
        [2,'Buxur','buxur.jpg',4500],
        [3,'Trefill','trefill.jpg',1500],
        [4,'Jakki','jakki.jpg',13500],
        [5,'Húfa','hufa.jpg',3550]        
]

@app.route('/')
def homepage():
        karfa = []
        fjoldi = 0
        if 'karfa' in session:
                karfa=session['karfa']
                karfa.append(vorur[id])
                fjoldi = len(karfa)
        return render_template('index.html', vorur=vorur,fjoldi=fjoldi)

# add - bæta í körfu
@app.route("/add/<int:id>")
def telja(id):
        karfa = []
        fjoldi = 0
        if 'karfa' in session:
                karfa=session['karfa']
                karfa.append(vorur[id])
                session['karfa'] = karfa
                fjoldi = len(karfa)
        else:
                karfa.append(vorur[id])
                session['karfa'] = karfa
                fjoldi = len(karfa)
        return render_template('index.html', vorur=vorur,fjoldi=fjoldi)

@app.route("/karfa")
def karfa():
        karfa = []
        summa = 0
        if 'karfa' in session:
                karfa = session['karfa']
                fjoldi = len(karfa)
                for i in karfa:
                        summa += int(i[3])
                return render_template("karfa.html", k = karfa, tom = False, fjoldi = fjoldi, summa = summa)

        else:
                return render_template("karfa.html", k = karfa, tom = True)

@app.route("/eydavoru/int:id")
def eydavoru(id):
        karfa = []
        karfa = session['karfa']
        vara = 0
        for i in range(len(karfa)):
                if karfa[i][0] == id:
                        vara = i
        karfa.remove(karfa[vara])
        session['karfa'] = karfa
        return render_template("eydavoru.html")

@app.route("/eyda")
def eyda():
        session.pop('karfa', None)
        return render_template("eyda.html")

@app.route('/result', methods = ['POST'])
def result():
        if request.method == 'POST':
                kwargs={
                        'name': request.form['nafn'],
                        'email': request.form['email'],
                        'phone': request.form['simi'],
                        'price': request.form['samtals']
                }
                return render_template('result.html',**kwargs)

@app.route('/lougout')
def logout():
        session.pop('karfa', None)
        return redirect(url_for('index'))

@app.errorhandler(404)
def pagenotfound(error):
    return render_template('pagenotfound.html'), 404


if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)