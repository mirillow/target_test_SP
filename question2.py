def is_in_fibonacci(target):
    if target == 0:
        return True
    if target < 0:
        return False
    return fibonacci_loop(target, 1, 0)
    

def fibonacci_loop(target, current_num, previous_num):
    
    if target == current_num:
        return True
    if target < current_num:
        return False

    next_num = current_num + previous_num

    return fibonacci_loop(target, next_num, current_num)


def main():
    n = int(input())
    if is_in_fibonacci(n):  
        print(f'O número {n} está na sequência de fibonacci')
    else:
        print(f'O número {n} NÃO está na sequência de fibonacci')


if __name__ == '__main__':
    main()