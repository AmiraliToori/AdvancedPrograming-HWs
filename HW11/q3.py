import matplotlib.pyplot as plt
import random




def bubbleSort(array, index):
    
  
  for i in range(len(array)):

    
    for j in range(0, len(array) - i - 1):
    
        
        
        if array[j] > array[j + 1]:
            
            
            
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
            
            plt.scatter(random_lst, index, label = "element")
            plt.title("Bubble Sort")
            plt.xlabel("Value")
            plt.ylabel("Index")
            plt.xticks(random_lst)
            plt.yticks(index)
            plt.grid(True, linestyle = '--')
            
            plt.pause(0.5)
            plt.clf()
            


random_lst = [random.randint(0, 100) for _ in range(15)]
random.seed(20)
print('Unsorted Array:')
print(random_lst)

index = [x for x in range(len(random_lst))]

plt.figure(figsize = (23, 10))
bubbleSort(random_lst, index)

print('Sorted Array in Ascending Order:')
print(random_lst)

plt.legend()
plt.show()
