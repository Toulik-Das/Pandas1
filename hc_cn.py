import pandas as pd
Run_list = [35,225,375,420,76, 105, 175, 85,120,155,230,55,67,320,174,194,205,337]
hc=[]
cn=[]

for i in Run_list:
    if i in range(0,49):
        hc.append(None)
        cn.append(None)

    elif (i in range(50,99)) :
         hc.append(1)
         cn.append(None)

    elif (i in range(100,149)):
          hc.append(None)
          cn.append(1)
    elif (i in range(150,199)):
          hc.append(1)
          cn.append(1)
    elif (i in range(200,249)):
          hc.append(None)
          cn.append(2)
    elif (i in range(250,299)):
          hc.append(1)
          cn.append(2)
    elif (i in range(300,349)):
          hc.append(None)
          cn.append(3)
    elif (i in range(350,399)):
          hc.append(1)
          cn.append(3)
    elif (i in range(400,449)):
          hc.append(None)
          cn.append(4)
    elif (i in range(450,499)):
          hc.append(1)
          cn.append(4)
    elif (i in range(500,549)):
          hc.append(None)
          cn.append(5)

#print('Hc :',hc)
#print('Cn:',cn)
l=[hc,cn]
df=pd.DataFrame({'Half_Century':hc,'Century':cn},index=Run_list)
print(df)
