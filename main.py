from flask import Flask, render_template, request

app = Flask(__name__)

# 학급 분필 개수를 저장할 딕셔너리
classrooms = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        class_name = request.form['class_name']
        chalk_count = int(request.form['chalk_count'])

        # 입력된 값을 딕셔너리에 저장
        classrooms[class_name] = chalk_count

    return render_template('index.html', classrooms=classrooms)

if __name__ == '__main__':
    app.run(debug=True, port=30215)
