from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# 1つの都道府県の行政区域データを返す
@app.route('/api/prefs/<pref_code>', methods=['GET'])
def get_prefecture(pref_code):
    path = fr"data\N03-20230101_27_GML\N03-23_{pref_code}_230101.geojson"
    # ファイルの読み込み
    with open(path, encoding="utf-8") as f:
        data = f.read()
    return data


if __name__ == '__main__':
    app.run(debug=True)
