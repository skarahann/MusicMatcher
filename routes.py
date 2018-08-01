##This imports the stuff needed to run Flask. request allows you to get the value, render_template allows 
##you to display an html page
from flask import Flask,request,render_template

app = Flask(__name__, template_folder="/Users/serdarkarahann/Desktop/MusicMatcher/app/templates")

##This creates the flask app. template_folder is the directory of the folder called templates

##When the someone first goes to the site, the app will load up this template(html page).
@app.route("/")
def index():
	return render_template('index.html')
	
##When someone clicks submit after selecting a value, the html page sends a the slider value to this	
@app.route("/test", methods=["POST"])
def test():
     bdylansongwriter = request.form["bdylansongwriter"]
     acollctivepsychedelic = request.form["acollctivepsychedelic"]
     foceanrb = request.form["foceanrb"]
     mgmtelectronic = request.form["mgmtelectronic"]
     nasrap = request.form["nasrap"]
     miapop = request.form["miapop"]
     grimesexperimental = request.form["grimesexperimental"]
     radioheadrock = request.form["radioheadrock"]
     mgayesoul = request.form["mgayesoul"]
     atwinambient = request.form["atwinambient"]
 
    return atwinambient
	
if __name__=="__main__":
    app.run() 
