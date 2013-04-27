import fileinput
import csv
import matplotlib.pyplot as plt
import numpy as np

from math import log, exp
from scipy.stats import linregress

(day, room, price) = range(3)

weekend = [6,7]
weekday = [1,2,3,4,5]


weekendprices = []
weekendrooms = []
weekdayprices = []
weekdayrooms = []

lnweekendprices = []
lnweekendrooms = []
lnweekdayprices = []
lnweekdayrooms = []



for row in csv.reader(fileinput.input()):
	if not fileinput.isfirstline():
		if int(row[day]) in weekend:
			weekendprices.append(float(row[price].strip()[1:]))
			weekendrooms.append(float(row[room].strip()))
		if int(row[day]) in weekday:
			weekdayprices.append(float(row[price].strip()[1:]))
			weekdayrooms.append(float(row[room].strip()))

lnweekendprices = np.log(weekendprices)
lnweekendrooms = np.log(weekendrooms)
lnweekdayprices = np.log(weekdayprices)
lnweekdayrooms = np.log(weekdayrooms)

weslope, weintercept, wer_value, wep_value, westd_err = linregress(lnweekendrooms,lnweekendprices)
wdslope, wdintercept, wdr_value, wdp_value, wdstd_err = linregress(lnweekdayrooms,lnweekdayprices)


print "Weekend price elasticity "+ str(weslope)
print "Weekday price elasticity "+ str(wdslope)

# checking on graphs:
plt.figure(1)

plt.subplot(411)
plt.plot(weekendrooms,weekendprices, 'ro')
plt.xlim([0,2650])
plt.title("Weekend")

plt.subplot(412)
plt.plot(weekdayrooms,weekdayprices, 'ro')
plt.xlim([0,2650])
plt.title("Non Weekend")

t =  np.arange(3,9)

plt.subplot(413)
plt.plot(lnweekendrooms,lnweekendprices, 'ro', t,weslope*t+weintercept)
plt.title("Ln Weekend")

plt.subplot(414)
plt.plot(lnweekdayrooms,lnweekdayprices, 'ro', t,wdslope*t+wdintercept)
plt.title("Ln Non Weekend")

plt.tight_layout()

plt.figure(2)

p =  np.arange(0,700)
q =  np.arange(0,700)
# considering that: (I understand that this is only for small changes on P and Q...)
# %DQ/%DP = Elasticity, then:
# ((Q-1000)/1000)/((P-200)/200) = Elasticity
# (Q-1000)/1000 = Elasticity*((P-200)/200)
# Q = 1000*Elasticity*((P-200)/200) + 1000
#
#so 
# P*Q = 1000*Elasticity*P*((P-200)/200) + 1000*P
#
#which means:
# Revenue(P) = 1000*Elasticity*P*((P-200)/200) + 1000*P 
# Deriving, and equating to zero, we can get the maximun revenue
# R'(P) = 1000*Elasticity*2*P/200 - 1000*Elasticity*200/200 + 1000 = 0
# P = (1000*Elasticity*200/200 - 1000)/(1000*Elasticity*2/200)  to max the revenue 

plt.subplot(411)
plt.plot(p, p*((1000*weslope*(p-200)/200)+1000))
plt.title("Revenue P*Q Weekend vs. P")

plt.subplot(412)
plt.plot(p, p*((1000*wdslope*(p-200)/200)+1000))
plt.title("Revenue P*Q Weekday vs. P")

plt.subplot(413)
plt.plot(q, q*(((200/weslope)*(q-1000)/1000)+200))
plt.title("Revenue P*Q Weekend vs. Q")
plt.annotate("we are interested in the revenue for 100 rooms", 
								xy = (100,100000), xytext = (300,150000),
								arrowprops=dict(facecolor='black', shrink=0.05),)
plt.subplot(414)
plt.plot(q, q*(((200/wdslope)*(q-1000)/1000)+200))
plt.title("Revenue P*Q Weekday vs. Q")

#given that I can only sell 100 rooms, 
# what is the maximum revenue that I can get by selling
# 100 rooms
max_rev_wd =  100*(((200/wdslope)*(100-1000)/1000)+200)
max_rev_we =  100*(((200/weslope)*(100-1000)/1000)+200)

# finally, the maximum price that I can charge for those rooms is
max_price_wd = max_rev_wd/100
max_price_we = max_rev_we/100

print "max price on weekend "  + str(max_price_we)
print "max price on weekday "  + str(max_price_wd)

#this is to get the overall maximum
we_price_to_max = (1000*weslope - 1000)/(1000*weslope*2/200)
wd_price_to_max = (1000*wdslope - 1000)/(1000*wdslope*2/200)

#print "price to max revenue on weekend " + str(we_price_to_max)
#print "price to max revenue on weekday " + str(wd_price_to_max)

plt.tight_layout()

plt.show()
