from get_ANdata import get_data

from openai import OpenAI
import json

from dotenv import load_dotenv

# .env 存储api_key
load_dotenv()


def llm(messages):
    client = OpenAI()
    response = client.chat.completions.create(
        messages=messages,
        response_format={"type": "json_object"},
        max_tokens=None,
        temperature=0.0,
        model="gpt-4o-mini", ).choices[0].message.content
    response = json.loads(response)
    return response


def Anqc(datas):
    result = []
    cc = datas["主诉"]
    hpi = datas["现病史"]
    pmh = datas["既往史"]
    pd = datas["初步诊断"]
    ph = datas["个人史"]
    cc1 = [{"role": "user",
            "content": "请判断下面这段病历主诉是否包含时间方面的描述，如果不包含返回不合规，如果包含返回合规，结果以json格式返回，请确保返"
                       "回的JSON结构如下例子所示：1.{'主诉时间检查':'合规'}\n2.{'主诉时间检查':'不合规'}"
                       f"病历主诉是：{cc}"}]
    cc2 = [{"role": "user",
            "content": "请判断下面这段病历主诉是否超过20个字，如果超过返回不合规，如果不超过返回合规，结果以json格式返回，请确保返回的JSON"
                       "结构如下例子所示：1.{'主诉简洁检查':'合规'}\n2.{'主诉简洁检查':'不合规'}"
                       f"病历主诉是：{cc}"}]
    hpcc = [{"role": "user",
             "content": "请判断下面的主诉和现病史是否相符，如果不相符返回不合规，如果相符返回合规，结果以json格式返回，请确保返回的JSON结构"
                        "如下例子所示：1.{'主诉现病史相关检查':'合规'}\n2.{'主诉现病史相关检查':'不合规'}"
                        f"病历主诉是：{cc}，现病史是{hpi}"}]
    hpi1 = [{"role": "user",
             "content": "请判断下面现病史中是否包含以下描述，持续时间、大小便情况、精神情况、睡眠情况、体重变化、饮食情况，如果不包含该项返回"
                        "不合规，如果包含则返回合规，结果字典列表的json格式返回，请确保返回的数据结构如下例子所示：[{'现病史大小便情况':'合规'},"
                        "{'现病史精神情况':'合规'},{'现病史睡眠情况':'合规'},{'现病史体重变化':'合规'},{'现病史饮食情况':'合规'}]"
                        f"现病史是{hpi}"}]
    hpi2 = [{"role": "user",
             "content": "请判断下面现病史是否包含诱因，如果不包含返回不合规，如果包含返回合规，结果以json格式返回，请确保返回的JSON结构如下例子"
                        "所示：1.{'现病史诱因检查':'合规'}\n2.{'现病史诱因检查':'不合规'}"
                        f"现病史是{hpi}"}]
    hpoc = [{"role": "user",
             "content": "请判断下面现病史包含的内脏器官是否在既往史有描述，如果现病史没有内脏器官描述或者有且在既往史也有该内脏器官相关描述都"
                        "返回合规，如果在现病史有内脏器官描述但在既往史不包含该内脏器官的描述则返回不合规，结果以json格式返回，请确保返回的"
                        "JSON结构如下例子所示：1.{'现病史既往史脏器检查':'合规'}\n2.{'现病史既往史脏器检查':'不合规'}"
                        f"现病史是{hpi}，既往史是{pmh}"}]
    pd1 = [{"role": "user",
            "content": "请判断下面初步诊断是否有正常的疾病诊断信息，如果有返回合规，如果没有返回不合规，结果以json格式返回，请确保返回的JSON"
                       "结构如下例子所示：1.{'初步诊断检查':'合规'}\n2.{'初步诊断检查':'不合规'}"
                       f"初步诊断是：{pd}"}]
    ph1 = [{"role": "user",
            "content": "请判断下面现病历个人史中是否包含出生地、生活习惯及嗜好、放射性物质、粉尘矿山相关描述，如果不包含该项返回不合规，如果包"
                       "含则返回合规，结果字典列表的json格式返回，请确保返回的数据结构如下例子所示：[{'个人史出生地检查':'合规'},{'个人史"
                       "生活习惯及嗜好检查':'合规'},{'个人史放射性物质接触史检查':'合规'},{'个人史粉尘接触史检查':'合规'}]"
                       f"个人史是{ph}"}]
    ph2 = [{"role": "user",
            "content": "请判断下面现病历个人史中是否包含'吸烟嗜好'、'饮酒嗜好'、'长期居留地'相关描述，如果不包含该项返回不合规，如果包含则返"
                       "回合规，结果必须以字典列表的json格式返回，请确保返回的数据结构一定如下例子所示：[{'个人史吸烟嗜好检查':'合规'},"
                       "{'个人史饮酒嗜好检查':'合规'},{'个人史长期居留地检查':'合规'}]"
                       f"个人史是{ph}"}]
    ph3 = [{"role": "user",
            "content": "请判断下面现病历个人史中是否包含'冶游史'的相关描述，如果不包含返回不合规，如果包含则返回合规，结果必须以json格式返回，"
                       "请确保返回的数据结构一定如下例子所示：{'个人史冶游史检查':'合规'}"
                       f"个人史是{ph}"}]
    ph4 = [{"role": "user",
            "content": "请判断下面现病历个人史中是否包含毒物质、工业毒物相关描述，如果不包含返回不合规，如果包含则返回合规，结果以json格式返"
                       "回，请确保返回的数据结构如下例子所示：{'个人史工业毒物检查':'合规'}"
                       f"个人史是{ph}"}]
    ph5 = [{"role": "user",
            "content": "请判断下面现病历个人史中是否包含药物嗜好或吸毒相关描述，如果不包含返回不合规，如果包含则返回合规，结果以json格式返回，"
                       "请确保返回的数据结构如下例子所示：{'药物嗜好检查':'合规'}"
                       f"个人史是{ph}"}]
    hpipd = [{"role": "user",
              "content": "请判断下面初步诊断和现病史的疾病部位是否相符，相符返回合规，不相符返回不合规，结果以json格式返回，请确保返回的JSON"
                         "结构如下例子所示：{'现病史初步诊断疾病部位一致性检查':'合规'}"
                         f"现病史是{hpi}，初步诊断是{pd}"}]
    ccpd = [{"role": "user",
             "content": "请判断下面主诉和初步诊断的疾病部位是否相符，相符返回合规，不相符返回不合规，结果以json格式返回，请确保返回的JSON结"
                        "构如下例子所示：{'初步诊断主诉疾病部位一致性检查':'合规'}"
                        f"主诉是{cc}，初步诊断是{pd}"}]

    if datas["主任医师"] == None or datas["主任医师"] == None:
        result.append({'医师签名检查': '不合规'})
    else:
        result.append({'医师签名检查': '合规'})

    if datas["患者入院时间"] == None or datas["病史采集时间"] == None:
        result.append({'记录时间检查': '不合规'})
    else:
        result.append({'记录时间检查': '合规'})

    if datas["病史叙述者"] == None:
        result.append({'病史陈述者检查': '不合规'})
    else:
        result.append({'病史陈述者检查': '合规'})

    if datas["婚育史"] == None:
        result.append({'婚姻状态检查': '不合规'})
    else:
        result.append({'婚姻状态检查': '合规'})

    if datas["民族"] == None:
        result.append({'民族检查': '不合规'})
    else:
        result.append({'民族检查': '合规'})

    if datas["年龄"] == None:
        result.append({'年龄检查': '不合规'})
    else:
        result.append({'年龄检查': '合规'})

    if datas["姓名"] == None:
        result.append({'姓名检查': '不合规'})
    else:
        result.append({'姓名检查': '合规'})

    if datas["性别"] == None:
        result.append({'性别检查': '不合规'})
    else:
        result.append({'性别检查': '合规'})

    if datas["职业"] == None:
        result.append({'职业检查': '不合规'})
    else:
        result.append({'职业检查': '合规'})

    if cc == None:
        result.append({'主诉缺失检查': '不合规'})
    else:
        result.append({'主诉缺失检查': '合规'})

    if hpi == None:
        result.append({'现病史缺失检查': '不合规'})
    else:
        result.append({'现病史缺失检查': '合规'})

    if pmh == None:
        result.append({'既往史缺失检查': '不合规'})
    else:
        result.append({'既往史缺失检查': '合规'})

    time_check = llm(cc1)
    result.append(time_check)

    simple_check = llm(cc2)
    result.append(simple_check)

    hpccrc = llm(hpcc)
    result.append(hpccrc)

    hpic = llm(hpi1)
    try:
        hpic = hpic["result"]
    except KeyError:
            hpic = hpic['结果']

    result += hpic

    hpc = llm(hpi2)
    result.append(hpc)

    hpocc = llm(hpoc)
    result.append(hpocc)

    pdc = llm(pd1)
    result.append(pdc)

    phc1 = llm(ph1)
    try:
        phc1 = phc1["结果"]

    except KeyError:
        phc1 = phc1['result']

    result += phc1
    phc2 = llm(ph2)
    try:
        phc2 = phc2['结果']

    except KeyError:
         phc2 = phc2['result']

    result += phc2
    phc3 = llm(ph3)
    result.append(phc3)

    phc4 = llm(ph4)
    result.append(phc4)

    phc5 = llm(ph5)
    result.append(phc5)

    hpipdrc = llm(hpipd)
    result.append(hpipdrc)

    ccpdrc = llm(ccpd)
    result.append(ccpdrc)

    return result


if __name__ == "__main__":
    filepaths = [
        #'./datas/data1/患者1-入院记录.txt',
        './datas/data2/入院记录.txt',
        './datas/data3/入院记录.txt']
    anqc_result_all = []
    for i,filepath in enumerate(filepaths):
        datas = get_data(filepath)
        datas = json.loads(datas)
        # 指定输出的JSON文件名
        filename1 = f'Andata{i}.json'
        # 使用with语句确保文件正确关闭，并指定编码为UTF-8
        with open(filename1, 'w', encoding='utf-8') as f:
            # 将字典列表写入JSON文件，并使用缩进美化输出
            json.dump(datas, f, indent=4, ensure_ascii=False)
        anqc_result = Anqc(datas)
        anqc_result_all.append(anqc_result)

        # 指定输出的JSON文件名
        filename2 = f'ANQC{i}.json'
        # 使用with语句确保文件正确关闭，并指定编码为UTF-8
        with open(filename2, 'w', encoding='utf-8') as f:
            # 将字典列表写入JSON文件，并使用缩进美化输出
            json.dump(anqc_result_all, f, indent=4, ensure_ascii=False)

print("ANQC已完成")