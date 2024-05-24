from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('temp5.html')

@app.route('/update_value', methods=['POST'])
def update_value():
    data = request.get_json()
    selected_value = data['value']
    print(f'Selected Value: {selected_value}')
    return 'Value Updated'

if __name__ == '__main__':
    app.run(debug=True)
