# 植物识别（PlantRecognition），即对于输入的一张图片（可正常解码，且长宽比较合适），输出植物识别结果。

import os
import requests
import appbuilder

# 请前往千帆AppBuilder官网创建密钥，流程详见：https://cloud.baidu.com/doc/AppBuilder/s/Olq6grrt6#1%E3%80%81%E5%88%9B%E5%BB%BA%E5%AF%86%E9%92%A5
os.environ["APPBUILDER_TOKEN"] = 'bce-v3/ALTAK-e8I60qicEUcctvvnFZqNR/0be9cbc0e1ed072db084a7cc3ed3f3ba8675c3b1'

image_url = "https://bj.bcebos.com/v1/appbuilder/palnt_recognize_test.jpg?authorization=bce-auth-v1%2FALTAKGa8m4qCUasgoljdEDAzLm%2F2024-01-23T09%3A51%3A03Z%2F-1%2Fhost%2Faa2217067f78f0236c8262cdd89a4b4f4b2188d971ca547c53d01742af4a2cbe"

# 从BOS存储读取样例文件
raw_image = requests.get(image_url).content
inp = appbuilder.Message(content={"raw_image": raw_image})
# inp = Message(content={"url": image_url})

# 运行植物识别
plant_recognize = appbuilder.PlantRecognition()
out = plant_recognize.run(inp)
# 打印识别结果
print(out.content)

# {'plant_score_list': [{'name': '榕树', 'score': 0.4230029582977295}, {'name': '榆树', 'score': 0.1273619383573532}, {'name': '美国榆', 'score': 0.12065108865499496}, {'name': '白蜡树', 'score': 0.11650644987821579}, {'name': '雨树', 'score': 0.045340824872255325}]}
