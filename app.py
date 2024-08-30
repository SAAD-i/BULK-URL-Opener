from flask import Flask, render_template, request, redirect, url_for
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/open-urls', methods=['POST'])
def open_urls():
    urls = request.form.get('urls')
    if urls:
        url_list = urls.split()
        for url in url_list:
            webbrowser.open_new_tab(url)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
