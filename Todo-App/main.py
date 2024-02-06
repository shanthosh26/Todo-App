from flask import Flask, render_template, request

app = Flask('Todo App')

tasks = []

@app.route('/', methods=['POST', "GET"])
def main():
    
    if request.method == 'POST':
        task = request.form.get('task')
        tasks.append(task)
        return render_template('index.html', tasks=tasks)
    return render_template('index.html')


app.run(debug=True)