from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<body>
    <h2>Student Application</h2>
    <form method="POST" action="/submit">
        Name: <input type="text" name="name"><br><br>
        Div: <input type="text" name="div"><br><br>
        Mob: <input type="text" name="mob"><br><br>
        Branch: <input type="text" name="branch"><br><br>
        Email: <input type="email" name="email"><br><br>
        <button type="submit">Submit</button>
    </form>
    <a href="/read"><button>Read</button></a>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    div = request.form.get('div')
    mob = request.form.get('mob')
    branch = request.form.get('branch')
    email = request.form.get('email')
    
    with open('records.txt', 'a') as f:
        f.write(f"{name},{div},{mob},{branch},{email}\n")
        
    return 'Data Saved! <a href="/">Go Back</a>'

@app.route('/read')
def read():
    data = []
    try:
        with open('records.txt', 'r') as f:
            for line in f:
                data.append(line.strip().split(','))
    except FileNotFoundError:
        pass

    table_html = "<h2>Records Table</h2><table border='1'><tr><th>Name</th><th>Div</th><th>Mob</th><th>Branch</th><th>Email</th></tr>"
    for row in data:
        table_html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>"
    table_html += "</table><br><a href='/'>Go Back</a>"
    
    return table_html

if __name__ == '__main__':
    app.run(debug=True)