height=float(input("请输入你的身高(米):"))      #输入身高(米)
weight=float(input("请输入你的体重（千克）:"))      #输入体重（kg）
bmi=weight/(height*height)                 #计算bmi指数

#判断身材是否合理
if bmi<18.5:
    print("您的BMI指数为："+str(bmi))       #输出bmi指数
    print("体重过轻 ~@-@~")
if bmi>18.5 and bmi<24.9:
    print("您的BMI指数为："+str(bmi))       #输出bmi指数
    print("正常范围，注意保持哦(-_-)")
if bmi>24.5 and bmi<29.9:
    print("您的BMI指数为："+str(bmi))        #输出bmi指数
    print("体重过重 ~@_@~")
if bmi>=29.9:
    print("您的BMI指数为："+str(bmi))       #输出bmi指数
    print("肥胖 ^@_@^")