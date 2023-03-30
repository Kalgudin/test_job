import os
import threading


def get_repository(name):
    print(f'поток {name} стартовал')
    url = 'https://gitea.radium.group/radium/project-configuration.git'
    os.system(f'git clone {url}')
    # os.system(f'cd template')
    os.system('git pull')
    print(f'поток {name} отработал')


if __name__ == "__main__":
    t1 = threading.Thread(target=get_repository, args=('t1',))
    t2 = threading.Thread(target=get_repository, args=('t2',))
    t3 = threading.Thread(target=get_repository, args=('t3',))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

