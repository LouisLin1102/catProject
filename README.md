# IoT catProject
# 動機想法
- 家中有飼養貓咪，由於無法與寵物做言語上的溝通，所以觀察身體行為才能了解到貓咪的身體狀況。
- 偶然發現貓咪頻繁進出便盆卻無排泄物，且於便溺時哀號，便懷疑是不是生病了；帶去醫院檢查發現是泌尿道感染、膀胱發炎導致尿液結晶，所以造成貓咪排泄困難。
- 此次實驗希望能掌握貓咪進出便盆次數，提早發現異常，提早治療。

**異常情況**
1.  頻繁進出便盆
2.  便盆無排泄物

# 功能
- 統計貓咪進入便盆次數，當次數異常時，藉由通訊軟體通知飼主，並提供照片觀察情況。
# 觀察對象
![cat](https://lh5.googleusercontent.com/8WqYPe0HUNuGbjoH3E2CuVfUzFm6--J8tDbZsbj2oCadjbiqS9BI7RkYHlXuhk4FnxxLRz1L6SocDcb3ystR=w1037-h1057-rw)

# 整體架構
**硬體架構**
- Raspberry Pi
- 紅外線感測模組
- 超音波感測器
- Pi Camera
- Red Led
- 便盆
- 攝影機

**軟體架構**
- Python Programming
- Google Cloud Platform
- Line Bot
- VS Code

**流程架構**
![flow](https://lh3.googleusercontent.com/phJmvUqzU1OrDird0XP9qNC-v8W3trqkvjUO_8Xx_yhQZzM7DdoeOVWBzKPjmom4wSVinejdzBAXgeg0XwyB=w1920-h1057-rw)

**電路圖**
![flow2](https://lh5.googleusercontent.com/GF6y2XS-bipPy6E6g5y8gaaaFub6POdP5-cpS7bfG1V4NCR9bOfN-d9noOIdj9Xfecxh-pRrLjKlBnHeJoAA=w1920-h1057-rw)

**LINE Bot Setting**
1. [登入LINE Developers](https://developers.line.biz/zh-hant/services/bot-designer/)
2. Create a new Provider 
- ![](https://lh6.googleusercontent.com/IUegsenf1sTCtwFlQM4TkIkBvu9CCcqDBQq7vbF3hjfPYbu_9LFS_oDDIHuZQyT8NlsbN7S9nG8NYLD9aNOU=w1037-h1057)
3. Create a new Channel
- ![](https://lh5.googleusercontent.com/4mNW-DtPi8WtbwR6SZIQAs-awIpsnXGG-vKN08pJ13EB_PmkgfqANOR9oQLLWBw-OgS9-TstJQwtks1H_ZYz=w1037-h1057-rw)
4. Channel secret : 頻道密碼，位於Basic settings
- ![](https://lh5.googleusercontent.com/xKPTeeYvCF87GZiIyJuurJqttTzTOe7q_aGxx_nv71wisnK7o8R2tmdNK93G64a8y6w85Z-GiOnhJW3Z2flo=w1920-h1057-rw)
5. Channel access token : 頻道憑證，位於Messaging API
- ![](https://lh4.googleusercontent.com/iEy7-fYQeZ7SOUEAhDxtaczlS8rudVf48YYeqA65TlhQmROVk2US8_EJ7HfP6RvvjtXX1BbVtBYgoFDD5GP9=w1037-h1057-rw)
6. User ID : 收信息使用者ID，位於Basic settings
- ![](https://lh6.googleusercontent.com/hqoffiJsJ2QBoa3BXnHIV4_zOqxrAAFCmsj3snU-xzwiyWESiBOmSatJN-AOuOCPAL0GnEnuDOxat3k_nr_V=w1037-h1057-rw)
**利用Heroku雲端部屬LINE Bot**
1. [登入Heroku，免費創建](https://signup.heroku.com/)
2. 建立Heroku 專案
3. 可以選擇安裝Heroku Git 或是使用 GitHub Deploy LINE Bot，此次使用GitHub
- ![](https://lh3.googleusercontent.com/lSXN7n9CtpwDCewydjb0wUDncWL9z7klfMEqiTkwYewPyL9oDFE7D6LhRyXnxHcZFOCWdmzANfVXoVEJUjlq=w1037-h1057-rw)
4. GitHub的LINE Bot具備三個檔案
- Procfile : Web執行檔案(app.py)
- app.py : 主程式邏輯，LINE Bot 相關憑證都要加入此檔案中
- requirements.txt : import library
5. Deploy LINE Bot
- ![](https://lh6.googleusercontent.com/2p1c7ei6pl99HHCLQbtuDzVm32h83gs2Nh2djCm9jKUlmFQ62wqiruXEWLuqOAJhG1L9Az_AfI8VBju32rQ1=w1920-h1057-rw)
**LINE Bot Webhook URL Setting**
1. 登入 LINE Developers，在Messaging API頁籤中，Webhook URL的地方，填入Heroku雲端平台賦予的HTTPS網址，來連接LINE Bot應用程式
- ![](https://lh3.googleusercontent.com/AoXBYWxS27N-2POpcJiZdUdyAXxstQ2gBiQLbh7ydynmeHuMFF3Bg39RBDTf2oybFlTjfZLVcmYM0Rj26YYO=w1037-h1057-rw)
2. 測試
- ![](https://lh5.googleusercontent.com/qMj5GNwAn6EZRBXnenYqYgHTrZNE0dG3cQhnbdgeZhMYdqTZSwbZhBqMw5qopC_KcxlqKcMBm-N1gXdfyees=w1037-h1057)


# 成品
**正面**
![photo](https://lh4.googleusercontent.com/f_Gg6zH4AFEd2mZYpNPeEVjx7oSZ0-rWG77THSEEqrF5rE7Ka5yzhiWSBw8UHz-8uEqv3QoEiwnaSpyu7Spm=w1920-h1057-rw)

**側面**
![photo](https://lh5.googleusercontent.com/Fwebitj8KaYNgBqIJ4-zEsIsl95TpEQdZkJmBKGxmQQGhmBVaXoba6Unc1ihqvq8-oIffs_bUhj0LJJ_UWCW=w1920-h1057-rw)

**頂部**
![photo](https://lh5.googleusercontent.com/HHQz4oZA8hF0pSDZQoV8O5c9O-3KImGVD_7h_fp9wGfJPt9e7O8X7Gjp3TGcNc90zC6Hl72ceBykbOlwCMwl=w1920-h1057-rw)

**內裝**
![photo](https://lh3.googleusercontent.com/76UYh9odPYMG4MFR4uUH05aNmIcsYpd9ZYaJNvNmsPu6VBCz4o9s490V_Xqz6Nt4QUj-eoE6FhIsgdqYD83C=w1920-h1057-rw)

**攝影機**
![photo](https://lh6.googleusercontent.com/dawGcg_KHQTZoexyHxEtiqQw6ei-qyiJoPF6e08ZJHQP5Pr-25pXui_PRuH7cuD2y_6xbKw3fGJ6oPLd7eKA=w1920-h1057-rw)

**Line Bot**
![photo](https://lh3.googleusercontent.com/CogfUN8DHxrWLU3O69iE1D6ipeBpRxwEvSMD9p1yzRBjDgPpnC0Q_9QmS1vSTefGA0akJPmDGKQWIpXcSfLm=w1037-h1057-rw)

**影片:**
- https://youtu.be/Q7wo56F3GwQ (白天)
- https://youtu.be/OnHeCfSKVKs (晚上)

# 參考資料
- [Cloud IoT Core](https://cloud.google.com/iot/docs/quickstart)
- [Cloud Function](https://cloud.google.com/functions/docs/how-to)
- [Cloud Storage](https://cloud.google.com/storage/docs/introduction)
- [Cloud BigQuery](https://cloud.google.com/bigquery/docs/introduction)
- [Cloud Dataflow](https://cloud.google.com/dataflow/docs/quickstarts)
- [Cloud Pub/Sub](https://cloud.google.com/pubsub/docs/quickstart-console)
- [AI Robot Maker Space](https://airobot.ccu.edu.tw/chapter-6-google%E7%9A%84%E7%89%A9%E8%81%AF%E7%B6%B2%E8%A7%A3%E6%B1%BA%E6%96%B9%E6%A1%88/)
- [物聯網氣象台](https://www.wandianshenme.com/play/mongoose-os-esp32-google-cloud-iot-core-build-mqtt-iot-weather/)
- [淺談 Cloud Dataflow & Apache Beam 處理資料流](https://tech.hahow.in/%E6%B7%BA%E8%AB%87-cloud-dataflow-apache-beam-%E8%99%95%E7%90%86%E8%B3%87%E6%96%99%E6%B5%81-a1a73af87fe9)
- [Python JWT](https://myapollo.com.tw/zh-tw/python-json-web-token/t)
- [Python virtualenv](https://ithelp.ithome.com.tw/articles/10199980)
- [Python 虛擬環境](https://www.gushiciku.cn/pl/gfCd/zh-tw)
- [Python Chatbot 開發](https://qiu-yan-ming.gitbook.io/python-chatbot/shi-yong-line-bot-sdk)
- [樹莓派Raspberry Pi之人體紅外線感測器實作](http://hophd.com/raspberry-pi-sensor-infrared/)
- [[PIR] 簡易人體紅外線感應 (PIR) 模組測試電路](https://ruten-proteus.blogspot.com/2013/03/PIR-testing.html)
- [超音波測距離](https://atceiling.blogspot.com/2014/03/raspberry-pi_18.html)
- [Pi Camera](http://www.raspigeek.com/index.php?c=read&id=51&page=1)
