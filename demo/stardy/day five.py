# 计算体脂率
height = input("请输入你的身高(米):")  # 输入身高(米)
weight = input("请输入你的体重（千克）:")  # 输入体重（kg）
sex = input("请输入你的性别(男:1.女:0):")  # 输入性别
age = input("请输入你的年龄:")  # 输入年龄

bmi = float(weight) / (float(height) * float(height))  # 计算bmi指数
per = 1.2 * bmi + 0.23 * int(age) - 5.4 - 10.8 * int(sex)
per = 1.2 * bmi + 0.23 * int(age) - 5.4 - 10.8 * int(sex)

if int(sex) == 1:
    if 15 < per < 18:
        print("体脂率合格", format(str(per)))
    else:
        print("体脂率不合格", format(str(per)))
else:
    if 25 < per < 28:
        print("体脂率合格", format(str(per)))
    else:
        print("体脂率不合格", format(str(per)))
