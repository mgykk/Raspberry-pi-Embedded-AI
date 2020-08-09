"""
    @author: Miguanyu
"""
from aip import AipSpeech
#填你自己的id和密钥
APP_ID='xxxxxx'
API_KEY='xxxxxx'
SECRET_KEY='xxxxxxx'
#初始化
aipSpeech=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
#读文件
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()
#格式是amr，语言是中文
result=aipSpeech.asr(get_file_content('/home/pi/miguanyu/speech/8k.amr'),'amr',8000,{
        'lan':'zh',
        })
print(result['result'][0])