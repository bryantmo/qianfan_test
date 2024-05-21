# 二维码识别 (QRcodeOCR) 可对图片中的二维码、条形码进行检测和识别，返回存储的文字信息及其位置信息。

import os
import appbuilder
import requests

# 请前往千帆AppBuilder官网创建密钥，流程详见：https://cloud.baidu.com/doc/AppBuilder/s/Olq6grrt6#1%E3%80%81%E5%88%9B%E5%BB%BA%E5%AF%86%E9%92%A5
os.environ["APPBUILDER_TOKEN"] = 'bce-v3/ALTAK-e8I60qicEUcctvvnFZqNR/0be9cbc0e1ed072db084a7cc3ed3f3ba8675c3b1'

# 从BOS读取样例图片
image_url = "https://bj.bcebos.com/v1/appbuilder/qrcode_ocr_test.png?" \
            "authorization=bce-auth-v1%2FALTAKGa8m4qCUasgoljdEDAzLm%2F2024-" \
            "01-24T12%3A45%3A13Z%2F-1%2Fhost%2Ffc43d07b41903aeeb5a023131ba6" \
            "e74ab057ce26d50e966dc31ff083e6a9c41b"
raw_image = requests.get(image_url).content
# 创建二维码识别组件实例
qrcode_ocr = appbuilder.QRcodeOCR()
# 执行识别操作并获取结果
out = qrcode_ocr.run(appbuilder.Message(content={"raw_image": raw_image}), location="true")
print(out.content)
# {'codes_result': [{'type': 'QR_CODE', 'text': ['ocr文字识别'], 'location': {'top': 506, 'left': 1302, 'width': 1972, 'height': 1961}}]}