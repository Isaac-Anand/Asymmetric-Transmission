import matplotlib.pyplot as plt

t_yy = open('D:/intern 2025/CST/AT-swirl-05-07/tyy_f.txt')
t_yx = open('D:/intern 2025/CST/AT-swirl-05-07/tyx_f.txt')
t_xy = open('D:/intern 2025/CST/AT-swirl-05-07/txy_f.txt')
t_xx = open('D:/intern 2025/CST/AT-swirl-05-07/txx_f.txt')

tyy = []
tyx = []
txy = []
txx = []
freq = []

for line in t_yy:
    line = line.rstrip()
    line = line.lstrip()
    a,b = tuple(line.split())
    freq.append(float(a))
    tyy.append(float(b))
t_yy.close()

for line in t_yx:
    line = line.rstrip()
    line = line.lstrip()
    a,b = tuple(line.split())
    tyx.append(float(b))
t_yx.close()

for line in t_xy:
    line = line.rstrip()
    line = line.lstrip()
    a,b = tuple(line.split())
    txy.append(float(b))
t_xy.close()

for line in t_xx:
    line = line.rstrip()
    line = line.lstrip()
    a,b = tuple(line.split())
    txx.append(float(b))
t_xx.close()

del_lin_x_f = []
for i in range(1003):
    del_lin_value = (abs(tyx[i]))**2 - (abs(txy[i]))**2
    del_lin_x_f.append(del_lin_value)

del_lin_y_f =[]
for i in range(1003):
    del_lin_value = -1*(del_lin_x_f[i])
    del_lin_y_f.append(del_lin_value)

Tx_f = []
for i in range(1003):
    Tx_f_val = (abs(txx[i]))**2 + (abs(txy[i]))**2
    Tx_f.append(Tx_f_val)

Ty_f = []
for i in range(1003):
    Ty_f_val = (abs(tyy[i]))**2 + (abs(tyx[i]))**2
    Ty_f.append(Ty_f_val)

plt.plot(freq, del_lin_x_f , 'r-o', markevery = 40, label= 'lin_x', linewidth = 2)
plt.plot(freq, del_lin_y_f , 'k-s', markevery = 70, label= 'lin_y', linewidth = 2)
plt.grid(True)
plt.xlabel('Frequency')
plt.ylabel('Asymmetric Transmission')
plt.title('Asymmetric Parameters')
plt.legend()
plt.show()

plt.plot(freq, Tx_f, 'r-o', markevery = 40, label = 'Tx', linewidth = 2)
plt.plot(freq, Ty_f, 'k-s', markevery = 40, label = 'Ty', linewidth = 2)
plt.grid(True)
plt.xlabel('Frequency')
plt.ylabel('Total Transmittance')
plt.title('...')
plt.legend()
plt.show()
