import dev_stats
from flask import Flask, render_template
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/table')
def dev_table():
    d = dev_stats.Developers()
    if 'figure.png' not in os.listdir(os.getcwd()):

        print('True')
        figure = d.create_plot()
    else:
        print('False')
    html_table = d.html_view(d.dataframe)
    return render_template('view.html', table=html_table, title='Devs Salary Table')


if __name__ == "__main__":
    app.run()
