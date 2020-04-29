from scipy import signal
import matplotlib.pyplot as plt
import control as con

#if using termux
import subprocess
import shlex
#end


x = []
y = []
for i in range(1,50):
    s1 = signal.lti([], [0,-1], [i])
    w, mag, phase = signal.bode(s1)
    sys = (mag,phase,w)
    gm,pm,wg,wp = con.margin(sys)
    x.append(i)
    y.append(pm)
    #print('Phase Margin:' ,pm)
    #print('Gain cross over frequency:' ,wg) 
#plt.figure()
#plt.semilogx(w, mag)    # Bode magnitude plot
#plt.figure()
#plt.semilogx(w, phase)  # Bode phase plot
#plt.show()
plt.figure()
plt.ylabel('Phase margin')
plt.xlabel('K')
plt.title('Phase margin vs K')
plt.plot(x,y)


#if using termux
plt.savefig('./figs/ee18btech11044_2.pdf')
plt.savefig('./figs/ee18btech11044_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_2.pdf"))

#else
#plt.show()

