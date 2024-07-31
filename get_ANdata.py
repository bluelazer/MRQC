# 导入openai api key
import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
# .env 存储api_key
load_dotenv()

def get_data(file_path=None):
    # 指定你的文本文件路径
    file_path = file_path

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    client = OpenAI()

    messages=[{"role": "user", "content":"请从以下病历文本中抽取以下字段，并以JSON格式返回结果，其中每个字段应严格对应于给定的字段名,这些字段"
                                         "名要全部返回。如果没有找到对应的信息，请将该字段的值设为'None'。字段包括：姓名、性别、年龄、职业、"
                                         "婚姻、民族、籍贯、联系电话、患者住址、过敏史、身份证号、患者入院时间、病史叙述者、病史采集时间、入院时情况、"
                                         "联系人、与患者关系、联系人电话、主诉、现病史、既往史、个人史、婚育史、家族史、体格检查、专科情况、辅助检查、"
                                         "初步诊断、主任医师、主治医师、住院医师、记录时间。请确保返回的JSON结构如下所示："
                                         "{姓名': ..., '性别': ..., ... '主治医师': ...}。"
                                         f"病历入院记录是：{lines}。"}]

    response = client.chat.completions.create(
                messages=messages,
                response_format={"type": "json_object"},
                max_tokens=None,
                temperature=0.0,
                model="gpt-4o-mini", )

    response_text = response.choices[0].message.content
    return response_text

if __name__ == "__main__":
    datas = get_data('./datas/data1/患者1-入院记录.txt')

    print(datas)


