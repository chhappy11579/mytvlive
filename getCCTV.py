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

def getAllData(file1, file2, Live):
    # 打开第一个文件并读取内容
    with open(file1, 'r',encoding='utf-8') as file1:
        content1 = file1.read()

    # 打开第二个文件并读取内容
    with open(file2, 'r',encoding='utf-8') as file2:
        content2 = file2.read()

    # 合并文件内容
    combined_content = content1 + '\n' + content2

    # 将合并后的内容写入新文件
    with open(Live, 'w',encoding='utf-8') as combined_file:
        combined_file.write(combined_content)
        writelog('合并写入完成！')


def convert_encoding(allData, newData, from_encoding='gbk', to_encoding='utf-8'):
    try:
        # 打开旧文件
        with open(allData, 'rb') as f:
            content = f.read().decode(from_encoding)
        # 转换编码并保存
        with open(newData, 'wb') as f:
            f.write(content.encode(to_encoding))
        writelog(f"Converted ok")
    except Exception as e:
        writelog(f"Error converting error: {e}")


def writelog(info):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(info)
        f.write('\n')



if __name__ == "__main__":
    writelog("---------------------" + "start " + time +"-----------------------------")
    getData('https://gh-proxy.com/raw.githubusercontent.com/fanmingming/live/refs/heads/main/tv/m3u/ipv6.m3u', "oldcctv.m3u")
    getData('http://aktv.top/live.m3u', "oldhktv.m3u")
    convert_encoding("oldcctv.m3u", "cctv.m3u")
    convert_encoding("oldhktv.m3u", "hktv.m3u")
    getAllData("cctv.m3u", "hktv.m3u", "live_ipv6.m3u")
    writelog("---------------------" + "end... " + time + "-----------------------------")
