from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary list to store the tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)