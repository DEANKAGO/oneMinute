from flask import render_template as render_template
from app.main import main_blueprint as main


@main.route('/home/')
def index():
    return render_template('index.html')


@main.route('/home', methods=['POST'])
def register():
    # query = request.form.get('query1')
    # selected = request.form.get('query')
    # if (not query or not selected):
    # return 'failure'
    # processed_text = query.upper()
    return render_template('index.html')


if __name__ == "__main__":
    main.run(debug=True, use_reloader=False)
