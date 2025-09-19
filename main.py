#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)

@app.route('/feedback')
def feedback_form():
    return '''
    <form method="POST" action="/submit_feedback">
        <label>Имя:</label>
        <input type="text" name="username"><br>
        <label>Отзыв:</label>
        <textarea name="comment"></textarea><br>
        <input type="submit" value="Отправить">
    </form>
       '''

# Приём данных формы
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    username = request.form['username'] # сохраняем в переменную имя
    comment = request.form['comment'] # сохраняем отзыв
    return f"Спасибо, {username}! Ваш отзыв: {comment}"


if __name__ == "__main__":
    app.run(debug=True)
