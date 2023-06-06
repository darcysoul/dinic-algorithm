from flask import Flask, render_template, request
from dinic import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_data = request.form['data-from-client']
        lines = input_data.strip().split('\n')
        max_flow = find_max_flow(lines)
        return render_template('index.html', flow=max_flow)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()