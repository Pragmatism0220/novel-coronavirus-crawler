# novel-coronavirus-crawler
关于中国境内新冠病毒走势的爬虫

## 它是什么
该项目使用Python3语言开发。它是一个爬取中国境内新冠病毒走势信息的爬虫，调用的163的公开接口，解析的json数据，然后将其保存到Excel。

保存的Excel文件的第一个表是关于中国的时间序列，后面的表是具体到每个省份，当日的感染情况详情。

## 使用方法
首先克隆本仓库：
```shell
git clone https://github.com/Pragmatism0220/novel-coronavirus-crawler.git
```

接着安装依赖，
```shell
pip install -r requirements.txt
```
如果你的默认Python版本不是3，请使用`pip3`代替`pip`。

之后只需要运行即可：
```shell
python run.py
```
同样地，如果你的默认Python版本不是3，请使用`python3`代替`python`。

## 作者
一个学生，一个宅男。

一个Kizuner，一个[春日望(twitter@kasuga_nozomi)](https://twitter.com/kasuga_nozomi)的死忠粉。

* **联系方式**
  * 博客地址: https://pragmatism0220.cf
  * 电子邮件: pragmatism0220@gmail.com
  * 微博: [@保護者_Pragmatism0220](https://weibo.com/u/7341561133)
  * 推特: [@Pragmatism_0220](https://twitter.com/Pragmatism_0220)

## 开源许可证
[MIT License](https://github.com/Pragmatism0220/novel-coronavirus-crawler/blob/master/LICENSE)