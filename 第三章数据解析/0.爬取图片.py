# import requests

#
# class Demo:
#     __z = 2
#     y = 10
#
#     @staticmethod
#     def getz():
#         return Demo.__z
#
#     def __init__(self):
#         self.__x = 10
#
#     def set(self, t):
#         self.__x = t
#
#     def get(self):
#         return self.__x


if __name__ == '__main__':
    # url = 'https://pic.qiushibaike.com/system/pictures/12410/124102162/medium/1TGARW2BPP90B773.jpg'
    # # 二进制形式的图片数据 text字符串 content二进制 json()对象
    # img_data = requests.get(url=url).content
    # # wb写入二进制数据
    # with open('./qiutu.jpg', 'wb') as fp:
    #     fp.write(img_data)
    #
    # d = Demo()
    # d.set(20)
    # print(d.get())
    #
    # print("------------")

    # print(Demo.y)
    #
    # txt = 'hello world'
    # txt = txt.upper()
    # txt = txt.lower()
    # txt = txt.replace('h', 'j')
    # print(txt)
    #
    # x = int(98.6)
    # print(x)
    #
    # rate = float(input("enter rate:"))
    # hrs = input("Enter Hours:")
    # print(rate)
    #
    # score = input("Enter Score: ")
    # s = float(score)
    # if s < 0.6:
    #     print(F)
    # elif s < 0.7:
    #     print(D)
    # elif s < 0.8:
    #     print(C)
    # elif s < 0.9:
    #     print(B)
    # elif s <= 1.0:
    #     print(A)
    # else:
    #     print("out of range")

    # def computepay(h, r):
    #     if h <= 40:
    #         pay = h * r
    #         return pay
    #     else:
    #         pay = 40 * r + 1.5 * r * (h - 40)
    #         return pay
    #
    #
    # hrs = input("Enter Hours:")
    # h = float(hrs)
    # r = float(input("Enter rate:"))
    # p = computepay(h, r)
    # print("Pay", p)

    # largest = None
    # smallest = None
    # while True:
    #     num = input("Enter a number: ")
    #     if num == "done":
    #         break
    #     else:
    #         try:
    #             num = int(num)
    #         except:
    #             print("Invalid input")
    #             continue
    #         if smallest is None:
    #             smallest = num
    #         elif smallest > num:
    #             smallest = num
    #         if largest is None:
    #             largest = num
    #         elif largest < num:
    #             largest = num
    #
    # print("Maximum is", largest)
    # print("Minimum is", smallest)