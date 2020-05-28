
import time,colorama
import vk_api,random
from colorama import Fore
from colorama import init


yellow = '\033[33m'
banner="""
%s
        D D n   T T T T
         D  D      T
         D  D      T
         D D       T

     DarkTrollVk
     proger : Naruto Uzumaki

""" % yellow

user=random.randint(1, 2147483647)
print(banner)
token = str (input(' Токен :'))
print("\n   Меню опцией : \n  \033[37m[\033[33m1\033[37m]  - Массовое смс. \n  \033[37m[\033[33m2\033[37m] - Вступить в группы тематики 'Лгбт' . \n    [\033[33m3\033[37m] -  Поставить статус( Который  вы сами хотите).\n   \033[37m[\033[33m4\033[37m] - Создать 5 бесед . \n   \033[37m[\033[33m5\033[37m] - Спам постами.")           
doings=int(input(Fore.YELLOW+' Номер опции :' ))
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

if doings==1:
    print(" \n   Напишите сообщение ,которое должно отправиться \n   Если оставите поле пустым ,то тогда смс будет 'я гей' ")
    message=str(input('\n  Сообщение :'))
    if message =="":
       message="Я гей"
    def sendmas():
       i=0
       online=vk.friends.getOnline()
       for onl in online   :
          i +=1
          vk.messages.send(user_ids =onl ,message=message,random_id=user)
          print(f"{i}. Сообщение отправленно ")
    sendmas()
elif doings ==3:
   print('   Введите сообщение для статуса \n   По умолчанию смс - "Я гей" ')
   status=str(input(' Статус :'))
   if status == '':
      status='Я гей'
   stat= vk.status.set(text=status)
   print(' Статус успешно установлен')
elif doings ==4:
   online=vk.friends.getOnline()
   onl = random.choice(online)
   print("\n   Введите название беседы \n   По умолчанию смс - 'Я гей'" )
   name =str(input(" Название :"))
   if name == "":
      name= "я гей"
   n=5
   stop =3
   stop_kapcha= 10
   def krutkabeced():
      for i in  range (n):
          time.sleep(stop)
          vk.messages.createChat(user_ids =onl,title= name)
          i+=1
          print('%s. Беседа создана' % i)                                                                                                              
          if i == 5:
             print(' Успешно создано 5 бесед . ')      
                                                                                                      
    krutkabeced()
elif doings ==2:
   def joingroups():
      n=1
      group= [ 65797052,151233321,128556106,97340700,79970646,60683281]
      for groups in group:
         vk.groups.join(group_id=groups)
         print(" Успешно вступил во все Лгбт группы")
   joingroups()
elif doings ==5:
   print( "\n   Введите числовой айди пользователя/сообщемтва")
   id=int(input('   айди :'))
   print(' Теперь введите текст будущих постов. По умолчанию будет "Я гей" ')
   messange=str(input('   text:'))
   if messange =="":
      messange= "Я гей"
   number_posts=int(input("  Число постов (от 1 до 500):"))
   stop= 3
   i=1
   stop_kapcha= 10
   kapcha= ' Капча долбанная . Ждем 10 секунд и на второй круг !'
   def spam():
      for i in range(number_posts):
         time.sleep(stop)
         vk.wall.post(owner_id=id,from_group=0,message=messange)
         i += 1
         print('%s пост отправлен' % i)
         if i == 10:
            print(kaptcha)
            i = 1
            time.sleep(stop_kapcha)
   spam()
