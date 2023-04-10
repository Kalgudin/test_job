import os
import threading

def get_repository(name):
    print(f'поток {name} стартовал')
    url = 'https://gitea.radium.group/radium/project-configuration.git'
    os.system(f'git clone {url} {name}')
    print(f'поток {name} отработал')


if __name__ == "__main__":
    print('IN RADIUM!!!!!!!!!!!!!!!!!!!!!!!')
    # t1 = threading.Thread(target=get_repository, args=('t1',))
    # t2 = threading.Thread(target=get_repository, args=('t2',))
    # t3 = threading.Thread(target=get_repository, args=('t3',))
    #
    # t1.start()
    # t2.start()
    # t3.start()
    #
    # t1.join()
    # t2.join()
    # t3.join()

