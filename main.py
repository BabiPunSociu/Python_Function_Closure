# 1, Nested function (Hàm lồng nhau)
# - Một hàm được định nghĩa trong 1 hàm khác thì ta gọi đó là
# Nested function

# - Các hàm Nested function có thể sử dụng biến trong phạm vi
#     hàm cha của nó nhưng không thay đổi được giá trị của chúng

# 2, Non-local variable (biến không cục bộ):
# - Là một biến được khai báo trong một hàm A, và nó cũng có thể
#     được dùng bên trong nested function khai báo bên trong hàm
#     A đó.
# - Bạn không được thay đổi giá trị của biến không cục bộ.

# 3, Khai báo Closure function:
# - Là hàm mà giá trị trả về là 1 hàm khác
# - Các biến không cục bộ được ghi nhớ
# - Nếu ta return hàm nested_function, chứ không phải gọi thực thi
#     nó.
# - Lúc này, việc sử dụng hàm sayHi sẽ qua 2 công đoạn:
#     Thứ nhất: Gọi hàm sayHi, trả về hàm printer
#     Thứ hai: Gọi đến hàm printer bằng cách gọi đến biến lưu
#         trữ giá trị trả về từ hàm sayHi

# Ví dụ:

def sayHi(msg):
    # Phạm vi code bên ngoài
    name = 'Dũng'
    
    def printer():
        # Đây là nested function
        print(f'{msg} {name}')
    return printer # return hàm
if __name__=='__main__':
    s = sayHi("Chào mừng")
    print(s) # function sayHi.<locals>.printer
    # Vì nó là một hàm printer nên ta gọi thêm một lần nữa
    s()
    # Điều đặc biệt, biến msg được gán khi gọi hàm sayHi, nhưng
    #   vẫn được lưu trữ giá trị khi gọi đến hàm printer()
    