#-*- encoding: utf-8 -*_

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import TableForm
from PIL import Image, ImageFont, ImageDraw
import datetime
import re
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')


class Config():
    SECRET_KEY = 'My Secret Key'

    @staticmethod
    def init_app(app):
        pass


bootstrap = Bootstrap()

app = Flask(__name__)
app.config.from_object(Config)
Config.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TableForm()
    if form.validate_on_submit():
        img = Image.open(os.path.join(STATIC_DIR, "template.jpg")).convert("RGB")
        #download font.ttf to static file, and use different font will be better
        font1 = ImageFont.truetype(os.path.join(STATIC_DIR, "jmt.ttf"), 30)
        font2 = ImageFont.truetype(os.path.join(STATIC_DIR, "jmt.ttf"), 30)
        font3 = ImageFont.truetype(os.path.join(STATIC_DIR, "jmt.ttf"), 28)

        draw = ImageDraw.Draw(img)
        color = (0, 0, 0)
        draw.text((100, 70), form.name.data, color, font=font1)
        draw.text((300, 65), form.department.data, color, font=font1)
        draw.text((600, 65), form.days.data, color, font=font1)
        draw.text((100, 120), form.reason.data, color, font=font1)

        draw.text((430, 35), form.year.data, color, font=font1)
        draw.text((520, 35), form.month.data, color, font=font1)
        draw.text((560, 35), form.day.data, color, font=font1)

        date_str = form.year.data + "-" + form.month.data + "-" + form.day.data
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        new_date = date + datetime.timedelta(days=int(form.days.data))
        new_month = re.findall('-(\d+)-', str(new_date))[0]
        new_day = re.findall('-(\d+) ', str(new_date))[0]

        draw.text((120, 210), form.month.data, color, font=font1)
        draw.text((170, 210), form.day.data, color, font=font1)
        draw.text((240, 210), new_month, color, font=font1)
        draw.text((280, 210), new_day, color, font=font1)
        draw.text((480, 210), form.destination.data, color, font=font1)
        draw.text((120, 250), form.manager.data, color, font=font2)
        draw.text((440, 250), u"同意", color, font=font3)
        draw.text((520, 250), form.boss.data, color, font=font3)

        img.save(os.path.join(STATIC_DIR, "test.jpg"))
        #add time to prevent browser cache result
        return render_template('index.html', form=form, image_name='test.jpg', time=datetime.datetime.now())
    return render_template('index.html', form=form, image_name='template.jpg')


if __name__ == '__main__':
    bootstrap.init_app(app)
    app.run()
