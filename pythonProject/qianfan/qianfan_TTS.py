import os
import appbuilder

# 高级用法https://github.com/baidubce/app-builder/blob/master/appbuilder/core/components/tts/README.md
# - TTS实时播放语音流
# - pcm文件转wav

# 请前往千帆AppBuilder官网创建密钥，流程详见：https://cloud.baidu.com/doc/AppBuilder/s/Olq6grrt6#1%E3%80%81%E5%88%9B%E5%BB%BA%E5%AF%86%E9%92%A5
os.environ["APPBUILDER_TOKEN"] = 'bce-v3/ALTAK-e8I60qicEUcctvvnFZqNR/0be9cbc0e1ed072db084a7cc3ed3f3ba8675c3b1'
tts = appbuilder.TTS()
cwd = os.getcwd()

# 使用baidu-tts模型, 默认返回MP3格式
# {'description': "用户上传的图像，你看到图片存在以下信息：整个图像内容可以表述为：'图片显示了各种新鲜蔬菜。这里有西红柿、黄瓜和可食用的玉米请根据提供的信息，回答用户如下问题：图片里的内容是什么?, 答案需要符合以下标准: 1.回答清晰，不含糊 2.回答完整详细，关注重要的内容 3.不要把用户的问题内容和描述这些信息写入答案"}
inp = appbuilder.Message(content={"text": "图片显示了各种新鲜蔬菜。这里有西红柿、黄瓜和可食用的玉米"})
out = tts.run(inp)
mp3_sample_path = os.path.join(cwd,"sample.mp3")
with open(mp3_sample_path, "wb") as f:
    f.write(out.content["audio_binary"])
print("成功将文本转语音，mp3格式文件已写入：{}".format(mp3_sample_path))

# 使用paddlespeech-tts模型，目前只支持返回WAV格式
wav_sample_path = os.path.join(cwd,"sample.wav")
inp = appbuilder.Message(content={"text": "图片显示了各种新鲜蔬菜。这里有西红柿、黄瓜和可食用的玉米"})
out = tts.run(inp, model="paddlespeech-tts", audio_type="wav")
with open(wav_sample_path, "wb") as f:
    f.write(out.content["audio_binary"])
print("成功将文本转语音，wav格式文件已写入：{}".format(wav_sample_path))

# 成功将文本转语音，mp3格式文件已写入：/Users/momoubin/Desktop/qianfan_test/pythonProject/qianfan/sample.mp3
# 成功将文本转语音，wav格式文件已写入：/Users/momoubin/Desktop/qianfan_test/pythonProject/qianfan/sample.wav