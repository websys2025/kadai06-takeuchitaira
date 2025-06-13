# kadai6-1.py
# e-Stat APIを使って「労働力調査（基本集計）」のデータを取得するプログラム
# 統計表ID: 0003212545 （労働力調査（基本集計）2023年）
# エンドポイント: https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
# 機能: 地域ごとの完全失業率（2023年）を取得し、JSON形式で出力する
# 使用方法: このスクリプトを実行すると、千葉県の複数市区の完全失業率データが取得・表示される

import requests

# APIキー（適切に管理してください）
APP_ID = "f960840b82863746f4c838dcbd7aa0f43bd13653"

# e-Stat APIのエンドポイント
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

# パラメータ設定
params = {
    "appId": APP_ID,
    "statsDataId": "0003212545",      # 労働力調査（基本集計）2023年
    "cdArea": "12101,12102,12103,12104,12105",  # 千葉県内のいくつかの市（千葉市等）
    "cdCat01": "130",                 # 完全失業率（一般カテゴリコード）
    "metaGetFlg": "Y",                # メタ情報も取得
    "cntGetFlg": "N",                 # 件数取得は行わない
    "explanationGetFlg": "Y",         # 説明を取得
    "annotationGetFlg": "Y",          # 注記を取得
    "sectionHeaderFlg": "1",          # セクションヘッダーあり
    "replaceSpChars": "0",            # 特殊文字置換しない
    "lang": "J"                       # 日本語指定
}
# API呼び出し
response = requests.get(API_URL, params=params)
# レスポンス処理
data = response.json()
# 結果を出力（辞書形式）
import json
print(json.dumps(data, indent=2, ensure_ascii=False))
