import os
import appbuilder
import requests

# 请前往千帆AppBuilder官网创建密钥，流程详见：https://cloud.baidu.com/doc/AppBuilder/s/Olq6grrt6#1%E3%80%81%E5%88%9B%E5%BB%BA%E5%AF%86%E9%92%A5
os.environ["APPBUILDER_TOKEN"] = "..."

# 从BOS存储读取样例文件
image_url = "https://bj.bcebos.com/v1/appbuilder/test_image_understand.jpeg?authorization=bce-auth-v1%2FALTAKGa8m4qCUasgoljdEDAzLm%2F2024-01-24T09%3A41%3A01Z%2F-1%2Fhost%2Fe8665506e30e0edaec4f1cc84a2507c4cb3fdb9b769de3a5bfe25c372b7e56e6"
raw_image = requests.get(image_url).content
# 输入参数为一张图片
inp = appbuilder.Message(content={"raw_image": raw_image, "question": "图片里内容是什么?"})
# 进行图像内容理解
image_understand = appbuilder.ImageUnderstand()
out = image_understand.run(inp)
# 打印识别结果
print(out.content)