from flask import Flask, render_template,request
app = Flask(__name__)
app.debug=True

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    sentence = request.form['txt']
    hashtags = sentence.split()
    hashtags = [hashtag.replace('#', '') for hashtag in hashtags]
    result = ','.join(hashtags)
    return render_template('index.html',result=result)
    

if __name__ == '__main__':
   app.run()
