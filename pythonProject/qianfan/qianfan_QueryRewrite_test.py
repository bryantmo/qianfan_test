#!/usr/bin/env python
# -*- coding:utf-8 -*-

import appbuilder
import os

# 多轮改写组件 (QueryRewrite) 是一个用于处理多轮对话和查询改写的组件。它主要用于理解和优化用户与机器人的交互过程，进行指代消解及省略补全。该组件支持不同的改写类型，可根据对话历史生成更准确的用户查询。

# 请前往千帆AppBuilder官网创建密钥，流程详见：https://cloud.baidu.com/doc/AppBuilder/s/Olq6grrt6#1%E3%80%81%E5%88%9B%E5%BB%BA%E5%AF%86%E9%92%A5
os.environ["APPBUILDER_TOKEN"] = 'bce-v3/ALTAK-e8I60qicEUcctvvnFZqNR/0be9cbc0e1ed072db084a7cc3ed3f3ba8675c3b1'

# 初始化并使用 QueryRewrite 组件
query_rewrite = appbuilder.QueryRewrite(model="ERNIE Speed-AppBuilder")
answer = query_rewrite(appbuilder.Message(['我应该怎么办理护照？', '您可以查询官网或人工咨询', '我需要准备哪些材料？', '身份证、免冠照片一张以及填写完整的《中国公民因私出国（境）申请表》', '在哪里办']), rewrite_type="带机器人回复")
print(answer)