import threading
import multiprocessing
from time import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            all_data.append(line.split())
            if not line:
                break
    return all_data


files_1 = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
start_time = time()
for files in files_1:
    thread = threading.Thread(target=read_info, args=(files,))

    thread.start()
    thread.join()

end_time = time()
print(f"Линейное выполнение через многопоточность заняло {end_time - start_time:.2f} секунд")

if __name__ == '__main__':
    start_time = time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, files_1)
        end_time = time()
        print(f"Многопроцессный подход занял {end_time - start_time:.2f} секунд")
