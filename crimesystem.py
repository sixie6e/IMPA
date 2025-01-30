#!/usr/bin/env python3
#
#2022 sixie6e <sixie6e@distherapy>
#
import numpy
import pandas
import matplotlib.pyplot as plt
#2020
#pseudocode
#need to convert to dictionaries probably
arrests0=7630000  #annually
arrests1=305200000  #in 40 years
def federal():
	t0=1
	t1=t0*30
	t2=t1*6
	t3=t2*2+5
	t4=t3*10
	a=76656 #convictions
	b=.97(a) #plea_deals
	c=a-b #trial_convictions
	d=.004(a)  #acquittals
	e=c+d  #trials
	f=1770 #num_judges
	g=88899  #num_laws/rules/regs
	h=1400000+35000+4000+10100+1700+30000+20000+3800(military,fbi,usm,dea,atf,nsa,cia,attorneys)  #num_enforcers
	i=122  #num_facilities
	j=38000  #num_guards
	k=153000 #num_prisoners
	l=195771  #num_prisoners_annually(half are immigration related)
	m=14137  #probation
	n=.084(a)  #probation_as_a_sentence
	o=330000000  #population
	#(p-r) based on the most severe. i.e. a home invasion where the depraved tie up people for their money is all three but is more violent than it is q or r.
	p=1313105   #violent_crime_reported (does not always mean conviction and/or actual violence)
	q=6452038  #property_crime_reported (does not always mean conviction and/or actual property crime)
	r=4606410  #financial_crime_reported (does not always mean conviction and/or actual financial crime)
	s=t1*40  #sentence
	t=650000  #released_annually
	u=110000  #youth_prisoners
	v=i*t3*(util+basic_needs +(45779(j)))  #overhead
	w=gross-v  #revgen
	x=.37(e)  #not_charged estimate
	y=.52(e)  #not_reported - this is an absurd 'statistic' (https://bjs.ojp.gov/content/pub/pdf/vnrp0610.pdf)
	z=.50(p+q+r+x+y)  #total "crimes" - high if you go by legislative wording and even higher by morality. also consider the amount of false accusations and exonerations.
	appeals=.227(a)  #success_rate
	dna_ex=375  #in 40 years
#2020
def  state():
	t0=1
	t1=t0*90
	t2=t1*2
	t3=t2*2+5
	t4=t3*10
	a=157500  #convictions
	b=.95(a)  #plea_deals
	c=97156  #trials ( 65.4*148558/100)
	d=a-b  #trial_convictions	
	e=.01(arrests)  #dismissed
	f=30000  #num_judges
	g=6000  #num_laws
	h=900000  #num_enforcers from policebluenation.org ny state trooper base salary is $104040, maine is $49296 coming from our taxed wages. **need to get salaries of police and sheriffs** We are literally paying to be exploited.
	i=3100  #num_facilities
	j=400000  #num_guards
	k=2185008  #num_prisoners
	l=12000000  #prisoner_commits_annually
	m=3492880  #probation
	n=.54(m)  #probation_as_a_sentence
	o=federal.o  #population
	p=t3*15  #sentence
	q=i*t3*(util+basic_needs +(47509(j)))  #overhead
	r=gross-q  #revgen
#2020
#https://harvardlawreview.org/2021/01/criminal-municipal-courts/
def  municipal():
	t0=1
	t1=t0*90
	t2=t1*2
	t3=t2*2+5
	t4=t3*10
	a=3500000  #convictions
	b=.99(a)  #plea_deals
	c=a-b  #trial_convictions
	d= 100000  #dismissed
	e=c+.20(d)  #trials
	f=state.f  #num_judges
	g=1500  #num_laws
	h=state.h  #num_enforcers
	i=state.i  #num_facilities
	j=state.j  #num_guards
	k=7500  #num_courts
	l=state.j  #num_guards
	m=state.k  #num_prisoners
	n=state.l  #num_prisoners_annually
	o=federal.o  #population
	p=t3*525  #sentence in us dollars
	q=i*t3*(util+basic_needs +(47509(j)))  #overhead
	r=2000000000  #revgen in us dollars
#2020
def corporate():
	t0=1
	t1=t0*30
	t2=t1*6
	t3=t2*2+5
	t4=t3*10
	a=1400000000  #phone calls in us dollars
	b=12.95*52*(federal.l+state.l)  #video visits in us dollars
	c=1700000000  #commissary in us dollars
	d=3700000000  #corecivic/cca/privateprisons in us dollars
	e=278000000  #turner construction in us dollars $14.4 Billion total
	f=531453000  #unicor fed prison labor
	g=1600000000  #state prison labor
	h=a+b+c+d+e+f+g  #revgen (t3)
	
for y in range(2024,2040):
	rf=federal.z2*r-federal.z1*q
	rs=state.z2*r-state.z1*q
	rm=municipal.z2*r-municipal.z1*q
	rc=corporate.z2*r-corporate.z1*q
	revgen=rf+rs+rm+rc
	print(y+'='+revgen)

spc = np.arange(26)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(spc + 0.00, federal.a, width = 0.20)
ax.bar(spc + 0.20, federal.b,  width = 0.20)
ax.bar(spc + 0.40, federal.c, width = 0.20)

