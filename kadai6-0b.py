# kadai6-2.py
# ------------------------------
# オープンデータ：Open-Meteo（https://open-meteo.com/）
# 概要：緯度・経度を指定して、指定地域の天気予報（気温、湿度、風速など）を取得する
# エンドポイント：https://api.open-meteo.com/v1/forecast
# 機能：時間ごとの気温予測データをJSON形式で取得可能
# 使用方法：東京（緯度35.7、経度139.7）の24時間気温予測を取得・整形表示
# ------------------------------

import requests
import pandas as pd

# Open-MeteoのAPIエンドポイント
API_URL = "https://api.open-meteo.com/v1/forecast"

# 緯度・経度（東京周辺）と取得内容（気温予測）を指定
params = {
    "latitude": 35.7,
    "longitude": 139.7,
    "hourly": "temperature_2m",
    "timezone": "Asia/Tokyo"
}

# APIリクエスト送信
response = requests.get(API_URL, params=params)

# JSONデータを取得
data = response.json()

# 必要な部分を抽出しDataFrameに変換
df = pd.DataFrame({
    "時刻": data["hourly"]["time"],
    "気温(℃)": data["hourly"]["temperature_2m"]
})

# 上位10件だけ表示
print(df.head(10))
