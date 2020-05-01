from scipy import signal
import matplotlib.pyplot as plt
import control as con

#if using termux
import subprocess
import shlex
#end

s1 = signal.lti([-3.084], [0,-1,-15.54], [10])
s2 = signal.lti([],[0,-1],[10])

w1, mag1, phase1 = signal.bode(s1)
w2, mag2, phase2 = signal.bode(s2)

sys1 = (mag1,phase1,w1)
gm1,pm1,wg1,wp1 = con.margin(sys1)
sys2 = (mag2,phase2,w2)
gm2,pm2,wg2,wp2 = con.margin(sys2)

#print('pm1:',pm1)
#print('wg1:',wg1)
#print('pm2:',pm2)
#print('wg2:',wg2)


plt.figure()
plt.semilogx(w2, phase2,label = 'Original System')
plt.plot([wg1,wg1],[-180,(-180+pm1)],'r--',lineWidth=1,label='final phase margin')
plt.plot([wg2,wg2],[-180,(-180+pm2)],'g--',lineWidth=1,label = 'initial phase margin')
plt.semilogx(w1,phase1,label = 'Compensated system')
plt.plot([0.01,100],[-180,-180],'b--',lineWidth=1,label='-180deg line')
plt.title('Bode phase plot')
plt.legend()
plt.grid()
#if using termux
plt.savefig('./figs/ee18btech11044_2_1.pdf')
plt.savefig('./figs/ee18btech11044_2_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_2_1.pdf"))
#plt.show()

