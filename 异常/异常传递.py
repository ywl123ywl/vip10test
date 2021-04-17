import time
try:
    f = open('test.txt')
    try:
         while True:
             content = f.readline()
             if len(content) == 0:
                break
             time.sleep(2)
             print(content)
    except:
         # 如果在读取⽂件的过程中，产⽣了异常，那么就会捕获到
         # ⽐如 按下了 ctrl+c
         print('意外终⽌了读取数据')
    finally:
         f.close()
         print('关闭⽂件')
except:
     print("没有这个⽂件")