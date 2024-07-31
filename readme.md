## Introduction
=================
这是一个基于Gpt-4o-mini对病历数据进行质量控制的demo项目，比如说核查入院记录中的主诉、现病史、既往史、家族史、体格检查、辅助检查等信息的填写是否符合 规定，是否缺失信息，是否存在不合理的地方。

## Quick start
=================
### 1. 下载项目
git clone https://github.com/bluelazer/MRQC.git

### 2. 安装依赖

### 3. 运行main.py 直接获取结果
      python main.py

main.py是整个项目的入口，调用get_ANdata.py和ANQC.py完成任务。
get_ANdata.py是对dataset文件夹中的数据集进行读取，并返回一个json格式的数据集。
ANQC.py是质量控制的核心代码，其中包含了对病历数据的核查，包括主诉、现病史、既往史、家族史、体格检查、辅助检查等信息的填写是否符合规定， 是否
缺失信息，是否存在不合理的地方。
病历信息存放到datas文件夹中，下面每个data文件夹包含一个患者的病历信息。


## reference
