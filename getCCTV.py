import datetime
import requests



time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
def getData(url, sources_dataName):
    # 目标网页URL
    url = url

    # 发送HTTP请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 获取网页内容
        data = response.text
        # 将内容写入到txt文件
        with open(sources_dataName, 'w') as file:
            file.write(data)
            writelog('数据已保存到' + sources_dataName)
    else:
        writelog('请求失败，状态码:', response.status_code)


def writelog(info):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(info)
        f.write('\n')



if __name__ == "__main__":
    writelog("---------------------" + "start " + time +"-----------------------------")
    getData('http://192.168.1.101:5000/Sub?type=m3u', "live.m3u")
    writelog("---------------------" + "end... " + time + "-----------------------------")
