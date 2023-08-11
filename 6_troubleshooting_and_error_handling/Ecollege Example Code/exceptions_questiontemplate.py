try:
    print('a', end=' ')
    x = int(input("Enter the denominator: "))
    print('b', end=' ')
    y = 1 / x
    #raise Exception
    print('c')
##except ZeroDivisionError:
##    print('d', end=' ')
except ValueError:
    print('e', end=' ')
##except Exception:
##    print('f', end=' ')
##except:
##    print('g', end=' ')
else:
    print('h', end=' ')
##finally:
##    print('i', end=' ')


print('j', end=' ')

