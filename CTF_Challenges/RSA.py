from Crypto.Util.number import *
#from sage.all import *

n = 744818955050534464823866087257532356968231824820271085207879949998948199709147121321290553099733152323288251591199926821010868081248668951049658913424473469563234265317502534369961636698778949885321284313747952124526309774208636874553139856631170172521493735303157992414728027248540362231668996541750186125327789044965306612074232604373780686285181122911537441192943073310204209086616936360770367059427862743272542535703406418700365566693954029683680217414854103
e = 57595780582988797422250554495450258341283036312290233089677435648298040662780680840440367886540630330262961400339569961467848933132138886193931053170732881768402173651699826215256813839287157821765771634896183026173084615451076310999329120859080878365701402596570941770905755711526708704996817430012923885310126572767854017353205940605301573014555030099067727738540219598443066483590687404131524809345134371422575152698769519371943813733026109708642159828957941
c = 305357304207903396563769252433798942116307601421155386799392591523875547772911646596463903009990423488430360340024642675941752455429625701977714941340413671092668556558724798890298527900305625979817567613711275466463556061436226589272364057532769439646178423063839292884115912035826709340674104581566501467826782079168130132642114128193813051474106526430253192254354664739229317787919578462780984845602892238745777946945435746719940312122109575086522598667077632

'''lst=continued_fraction(Integer(e)/Integr(n))
conv=lst.convergents()

for i in conv:
	k=i.numerator()
	d=int(i.denominator())
	msg=pow(c,d,n)
	print(long_to_bytes(msg))
'''
def c_fraction(e,n):
	cf=[]
	q=e/n
	print(q)
	r=e%n
	cf.append(q)

	while (r!=0):
		e,n=n,r
		q=e/n
		r=e%n
		cf.append(q)
	return cf

k=c_fraction(e,n)
#print k

def convergent(cf):
	#divide numerators and denominators into two different lists
	num = []
	denom = []
	conv = []
	for i in range(len(cf)):
		if(i==0):
			num.append(cf[0])
			denom.append(1)
		elif(i==1):
			num.append(cf[1]*cf[0]+1)
			denom.append(cf[1])
		else:
			num.append(cf[i]*num[i-1]+num[i-2])
			denom.append(cf[i]*denom[i-1]+denom[i-2])
		
	return num,denom
l=convergent(k)
print(len(l[1]))

for i in l[1]:
	m=pow(c,i,n)
	m=long_to_bytes(m)
	if(m[:4]=='d4rk'):
		print(m)
	

