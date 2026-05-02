"""
简易计算器
练习内容：函数、条件判断、循环、异常处理
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("不能除以零！")
    return x / y

def main():
    print("=== 简易计算器 ===")
    print("操作：1.加  2.减  3.乘  4.除  0.退出")
    
    while True:
        choice = input("\n选择操作 (0-4)：")
        
        if choice == "0":
            print("再见！")
            break
        
        if choice not in ("1", "2", "3", "4"):
            print("无效输入，请重新选择")
            continue
        
        try:
            num1 = float(input("输入第一个数："))
            num2 = float(input("输入第二个数："))
        except ValueError:
            print("请输入有效的数字！")
            continue
        
        try:
            if choice == "1":
                result = add(num1, num2)
                op = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                op = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                op = "*"
            elif choice == "4":
                result = divide(num1, num2)
                op = "/"
            
            print(f"结果：{num1} {op} {num2} = {result}")
        except ValueError as e:
            print(f"错误：{e}")

if __name__ == "__main__":
    main()
