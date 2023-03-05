# python3
#211RMB021 Daniels Raivo Ivanovs 15.grupa

import sys
import threading
import numpy


def compute_height(n, parents):
    heights = np.zeros(int(n))
    max_height = 0
    for i in range(int(n)):
        if heights[i] > 0:
            continue
            height = 0
        j = i 
        while j != -1:
            if heights [j] > 0:
                height += heights[j]
                break
            else:
                height += 1
                j= int(parents[j])
                heights[i] = height
                if height > max_height:
                    max_height = height
    return max_height

def main():
    input_method = input().strip()
    
    if input_method == "F":
        try:
            file_name = input().strip()
            with open(f"./test/{file_name}") as file:
                n = file.readline().strip()
                parents = file.readline().strip().split()
                except:
                    print("ERROR")
                return
         elif input_method == "I":
            n = input().strip()
            parents = input().strip().split()
          else:
            print("Invalid input method.")
            return
        
        height = compute_height(n, parents)
        print(int(height))
        
                    
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
