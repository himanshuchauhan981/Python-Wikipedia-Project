import wikipedia
import webbrowser
from flask import Flask, request,render_template,redirect,url_for
app = Flask(__name__)
app.jinja_env.filters['zip'] = zip

@app.route('/search_result/<word>')
def search_result(word):
    detailList=urlList=[]
    result=tuple(wikipedia.search(word,results=5));
    for item in result:
        detail = wikipedia.summary(item,sentences=1);
        detailList.append(detail);
        urlDetail = wikipedia.page(item);
        URL = urlDetail.url;
        urlList.append(URL);
    detailTuple = tuple(detailList)
    urlTuple = tuple(urlList)
    length = len(detailTuple)
    return render_template('index.html', result=result, detailTuple=detailTuple, urlTuple=urlTuple);


@app.route('/searchBox', methods = ['POST','GET'])
def searchBox():
    if request.method == "POST":
        search = request.form['word']
    return redirect(url_for('search_result', word = search))


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/randomPage', methods = ['POST','GET'])
def random_page():
    if request.method == "POST":
        ran_wiki = wikipedia.random()
        ran_url = wikipedia.page(ran_wiki)
        ran_urls = ran_url.url
        webbrowser.open(ran_urls)
    return '0',204

if __name__ == '__main__':
    app.run(debug=True)
