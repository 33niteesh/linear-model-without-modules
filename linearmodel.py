x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,4,5,6,7,8,9,10]
x_test=x[6:]
y_test=y[6:]
#x=[11,12,13,14]
#y=[11,12,13,14]
#y=a0+a1x
#sigma(y)=ma0+a1sigma(x) @1 m=len(x)
#sigma(x*y)=ma0*sigma(x)+a1(sigma(x**2)) @2
m=5
sigma_y=sum(y[0:6])
sigma_x=sum(x[0:6])
xy=[]
xx=[]
for i in range (0,6):
    xy.append(x[i]*y[i])
    xx.append(x[i]*x[i])
sigma_xy=sum(xy)
sigma_xx=sum(xx)
#fitting model
a1=((sigma_xy)-(sigma_x)*(sigma_y))/((sigma_xx)-(sigma_x)**2)
a0=((sigma_y)*(sigma_xx)-(sigma_x)*(sigma_xy))/((sigma_xx)-(sigma_x)**2)
#m=10
#y=x our linear model
print('weights are--','a0:',a0,'a1:',a1)
r=int(input('input:'))
print('y=',a0,'+',a1,'x')
y0=a0+a1*(r)
print('predicted output',y0)
print('training data set',x[0:6],y[0:6])
for k in range(0,len(x_test)):
    y0=a0+a1*x_test[k]
    if y0==y_test[k]:
        pass
print('our model is correct')