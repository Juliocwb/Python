from cgi import print_environ


def fat(n):
    if n == 1:
       return 1
    else:
        return n * fat(n-1)
n =int(input("numero : "))
print(fat(n))