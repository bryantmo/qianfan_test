import os
import appbuilder
import requests

# 请前往千帆AppBuilder官网创建密钥，流程详见：https://cloud.baidu.com/doc/AppBuilder/s/Olq6grrt6#1%E3%80%81%E5%88%9B%E5%BB%BA%E5%AF%86%E9%92%A5
os.environ["APPBUILDER_TOKEN"] = 'bce-v3/ALTAK-e8I60qicEUcctvvnFZqNR/0be9cbc0e1ed072db084a7cc3ed3f3ba8675c3b1'

# 从BOS存储读取样例文件
image_url = "https://bj.bcebos.com/v1/appbuilder/test_image_understand.jpeg?authorization=bce-auth-v1%2FALTAKGa8m4qCUasgoljdEDAzLm%2F2024-01-24T09%3A41%3A01Z%2F-1%2Fhost%2Fe8665506e30e0edaec4f1cc84a2507c4cb3fdb9b769de3a5bfe25c372b7e56e6"
raw_image = requests.get(image_url).content
# 输入参数为一张图片
inp = appbuilder.Message(content={"raw_image": raw_image, "question": "图片里的内容是什么?"})
# 进行图像内容理解
image_understand = appbuilder.ImageUnderstand()
out = image_understand.run(inp)
# 打印识别结果
print(out.content)
# {'description': "用户上传的图像，你看到图片存在以下信息：整个图像内容可以表述为：'图片显示了各种新鲜蔬菜。这里有西红柿、黄瓜和可食用的玉米请根据提供的信息，回答用户如下问题：图片里的内容是什么?, 答案需要符合以下标准: 1.回答清晰，不含糊 2.回答完整详细，关注重要的内容 3.不要把用户的问题内容和描述这些信息写入答案"}
