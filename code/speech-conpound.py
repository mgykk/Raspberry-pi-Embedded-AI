"""
    @author: Miguanyu
"""
from aip import AipSpeech
import pygame
from time import time
#输入自己的id和密钥
APP_ID='14842692'
API_KEY='d06L3VtQCXr0qyL9PWGySGf0'
SECRET_KEY='ScxR7ObkPQ1blfGzZGDGkBe5oobfOlDc'

aipSpeech=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
#在可选的参数中对语速，音量，人声进行调整
t=time()
result = aipSpeech.synthesis(text = '调用语音接口进行语音合成',
                             options={'spd':5,'vol':9,'per':1,})
#将合成的语音写如文件
if not isinstance(result,dict):
    with open('.mp3','wb') as f:
        f.write(result)
        
else:print(result)
#调用利用树莓派自带的pygame
pygame.mixer.init()
#MP3文件路径
pygame.mixer.music.load('/home/pi/miguanyu/speech/.mp3')
pygame.mixer.music.play()
t2=time()
print(t2-t)