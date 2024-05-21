import os
import appbuilder
import requests

# 动物识别 (AnimalRecognition) 支持对于输入的一张图片（可正常解码），输出动物识别结果。
# https://github.com/baidubce/app-builder/blob/master/appbuilder/core/components/animal_recognize/README.md
# 请前往千帆AppBuilder官网创建密钥，流程详见：https://cloud.baidu.com/doc/AppBuilder/s/Olq6grrt6#1%E3%80%81%E5%88%9B%E5%BB%BA%E5%AF%86%E9%92%A5
os.environ["APPBUILDER_TOKEN"] = 'bce-v3/ALTAK-e8I60qicEUcctvvnFZqNR/0be9cbc0e1ed072db084a7cc3ed3f3ba8675c3b1'

# 从BOS读取样例图片
image_url = "https://bj.bcebos.com/v1/appbuilder/animal_recognize_test.png?" \
            "authorization=bce-auth-v1%2FALTAKGa8m4qCUasgoljdEDAzLm%2F2024-01-24T" \
            "12%3A19%3A16Z%2F-1%2Fhost%2F411bad53034fa8f9c6edbe5c4909d76ecf6fad68" \
            "62cf937c03f8c5260d51c6ae"
raw_image = requests.get(image_url).content
# 创建动物识别组件实例
animal_recognition = appbuilder.AnimalRecognition()
# 执行识别操作并获取结果
out = animal_recognition.run(appbuilder.Message(content={"raw_image": raw_image}))
print(out.content)

# {'result': [
# {'name': '国宝大熊猫', 'score': '0.975161'},
# {'name': '秦岭四宝', 'score': '0.0161979'},
# {'name': '团团圆圆', 'score': '0.00239265'},
# {'name': '圆仔', 'score': '0.00192277'},
# {'name': '棕色大熊猫', 'score': '0.00130296'},
# {'name': '小熊猫', 'score': '0.000275865'}]}