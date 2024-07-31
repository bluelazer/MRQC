from get_ANdata import get_data
from ANQC import Anqc
import json

filepaths = [
    './datas/data1/患者1-入院记录.txt',
    './datas/data2/入院记录.txt',
    './datas/data3/入院记录.txt']

anqc_result_all = []
for i, filepath in enumerate(filepaths):

    #提取入院记录的信息，保存为字典，再保存到json文本
    datas = get_data(filepath)
    datas = json.loads(datas)
    #打印结构化的数据
    print(datas)
    # 把提取到的数据保存到json文本
    filename1 = f'Andata{i}.json'
    # 使用with语句确保文件正确关闭，并指定编码为UTF-8
    with open(filename1, 'w', encoding='utf-8') as f:
        # 将字典列表写入JSON文件，并使用缩进美化输出
        json.dump(datas, f, indent=4, ensure_ascii=False)


    #根据质控规则，根据判断规则需求把提取到的数据交给大模型判断对应条目是否合规，结果保存为字典列表
    anqc_result = Anqc(datas)
    anqc_result_all.append(anqc_result)

    print(anqc_result)

    # 指定输出的JSON文件名
    filename2 = f'ANQC{i}.json'
    # 使用with语句确保文件正确关闭，并指定编码为UTF-8
    with open(filename2, 'w', encoding='utf-8') as f:
        # 将字典列表写入JSON文件，并使用缩进美化输出
        json.dump(anqc_result_all, f, indent=4, ensure_ascii=False)


print("任务完成")
print("该喝咖啡了")