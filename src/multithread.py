import concurrent.futures
import datetime

def show_time(n):
    now = datetime.datetime.now()
    print ("Current date and time (%s): " %(n))
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for a in range(1,4):
        futures.append(executor.submit(show_time,n=a))
    
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
