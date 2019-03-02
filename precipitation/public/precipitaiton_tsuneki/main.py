from flask import Flask, render_template, request
import random
from datetime import datetime
from get_wether import get_jma,get_tenki_jp
app = Flask(__name__)

@app.route("/")
def index():
    start = request.args.get("start", "")
    average = random.randint(0, 100)
    
    now = datetime.now().strftime("%H")
    now = int(now)  
    if 0 <= now < 6:
        now = '00-06'
    elif 6 <= now < 12:
        now = '06-12'
    elif 12 <= now < 18:
        now = '12-18'
    elif 18 <= now < 24:
        now = '18-24'
    
    data2 =get_tenki_jp(now)

    data1 = get_jma(now)
    average = (int(data2)+int(data1))/2
    return render_template("index.html",
                            start=start,
                            average=average,
                            data1 = data1,
                            data2 = data2)

if __name__ == '__main__':
    app.run( host = '0.0.0.0' )