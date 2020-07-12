arr = []




def main():
    front = -1
    rear = -1
    while True:
        print("1. Insert an element in the queue")
        print("2. Delete an element from the queue")
        print("3. DIsplay element at the front")
        print("4. Display all elements of the queue")
        print("5. Display size of the queue")
        print("6.Quit")
        choice= int(input("Enter your choice: "))
        if choice == 1:
            x = int(input("enter an element in the queue: "))
            insert(x)
            continue
        elif choice == 2:
            delete()
            print("Deleted element is: ",x)
            continue
        elif choice == 3:
            top()
        elif choice == 4:
            display()
        elif choice == 5:
            size()
        elif choice == 6:
            exit()
        else:
            print("not a valid choice")

def isEmpty():
    if len(arr) == 0:
        return 1
    else:
        return 0

def insert(x):
    if isEmpty():
        print("Queue empty")
    if front == -1:
        front = 0
    rear += 1
    arr.append(x)
    print(arr)

def delete():
    front
    x = arr[front]
    arr.remove(x)
    front += 1
    print("front: ",front)
    return x

main()
            
