arr = []
top = -1
size = 0


def push(x):
    global top
    top += 1
    arr.append(x)
    
def pop(x):
    global top
    return arr.pop()
    top -= 1

def peek():
    global top
    print("Top in peek",top)
    
    return arr[top]
def display():
    print(arr)

def size():
    return len(arr)
    

def main():
    while True:
        print("1. Push an element on the stack")
        print("2. Pop an element from the stack")
        print("3. Display the top element")
        print("4. Display all stack elements")
        print("5. Display size of the stack")
        print("6. Quit")
        print("Enter your choice: ")
        choice = int(input())
        if choice == 6:
            break
        elif choice == 1:
            print("enter the element to be pushed: ")
            x = int(input())
            push(x)
            continue
        elif choice == 2:
            x = pop(x)
            print("Popped element is: ",x)
            continue
        elif choice == 3:
            print("Element at the top is: ",peek())
            continue
        elif choice == 4:
            display()
            continue
        elif choice == 5:
            print("size of stack is: ",size())
            continue
        else:
            print("wrong choice")


main()
            
