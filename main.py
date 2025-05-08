from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def page():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    promotion_list = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]
    return '<br>'.join(promotion_list)


@app.route('/image_mars')
def image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='13.png')}">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <title>Промо Марс</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                  </head>
                  <body>
                    <div class="container mt-5">
                      <h1 class="promo-title">Жди нас, Марс!</h1>
                      <img src="{url_for('static', filename='img/13.png')}" class="promo-image img-fluid">
                      <div class="promo-items">
                        <div class="promo-item item-1">Человечество вырастает из детства.</div>
                        <div class="promo-item item-2">Человечеству мала одна планета.</div>
                        <div class="promo-item item-3">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                        <div class="promo-item item-4">И начнем с Марса!</div>
                        <div class="promo-item item-5">Присоединяйся!</div>
                      </div>
                    </div>
                  </body>
                </html>"""


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <title>Варианты выбора</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                  </head>
                  <body>
                    <div class="container mt-5">
                      <h1 class="text-center mb-4">Мое предложение: {planet_name}</h1>
                      <div class="choice-items">
                        <div class="choice-item item-1">Эта планета близка к Земле;</div>
                        <div class="choice-item item-2">На ней много необходимых ресурсов;</div>
                        <div class="choice-item item-3">На ней есть вода и атмосфера;</div>
                        <div class="choice-item item-4">На ней есть небольшое магнитное поле;</div>
                        <div class="choice-item item-5">Наконец, она просто красива!</div>
                      </div>
                    </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
                  </body>
                </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Результаты отбора</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                  </head>
                  <body>
                    <div class="container mt-5">
                      <h1 class="text-center mb-4">Результаты отбора</h1>
                      <div class="choice-item item-1">
                        Претендента на участие в миссии {nickname}:
                      </div>
                      <div class="choice-item item-2">
                        Поздравляем! Ваш рейтинг после {level} этапа отбора составляет {rating}!
                      </div>
                      <div class="choice-item item-4">
                        Желаем удачи!
                      </div>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
