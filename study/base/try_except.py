def foo(s):
    return 10 / int(s)
 
def bar(s):
    return foo(s) * 2
 
def main():
    try:
        bar(0)    #可以捕获到foo处可能发生的错误.
        foo(0)
    
    except Exception as e:
    #except (ZeroDivisionError, ValueError) as e:
        print("Error",e)

    finally:
        print("finally..")

main()


### 多个except
def deposit(amount,balance):
    # assert 断言，后面的描述是except的内容
    assert amount > 0,"The deposit amount must be greater than 0."
    balance += amount
    return balance

try:
    balance = deposit(-1,0)
#先被AssertionError 捕获
except AssertionError as e:
    print(f"Assertion Error: {e}")
except Exception as e:
    print(f"common Exception: {e}")