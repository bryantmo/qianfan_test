import os
import appbuilder

# 请前往千帆AppBuilder官网创建密钥，流程详见：https://cloud.baidu.com/doc/AppBuilder/s/Olq6grrt6#1%E3%80%81%E5%88%9B%E5%BB%BA%E5%AF%86%E9%92%A5
os.environ["APPBUILDER_TOKEN"] = 'bce-v3/ALTAK-e8I60qicEUcctvvnFZqNR/0be9cbc0e1ed072db084a7cc3ed3f3ba8675c3b1'

# 相似问生成组件（SimilarQuestion）可以用于基于输入的问题，挖掘出与该问题相关的类似问题。广泛用于客服、问答等场景。
similar_question = appbuilder.SimilarQuestion(model="ERNIE Speed-AppBuilder")

msg = "我想吃冰淇淋，哪里的冰淇淋比较好吃？"
msg = appbuilder.Message(msg)
answer = similar_question(msg)

print("Answer: \n{}".format(answer.content))