#coding:utf-8
import math
import copy
import numpy as np
import matplotlib.pyplot as plt
import random
dim=5
num=1000
testnum=500
sigma=[]
u1=[]
u0=[]
X=[]
W=[]
Xtest=[]
step=0.0001
Epsilon=0.01
lamata=0.01
def ini(sigma,u1,u0,X,Xtest,W):
	for i in range(dim):
		sigma.append(0.3)
		u1.append(random.random())
		u0.append(random.random())
	for datanum in range(num):
		a=[]
		b=random.random()
		if b>0.5:
			for i in range(dim):
				a.append(np.random.normal()*sigma[i] + u1[i])
			a.append(1)
		else:
			for i in range(dim):
				a.append(np.random.normal()*sigma[i] + u0[i])
			a.append(0)
		X.append(a)
	for datanum in range(testnum):
		a=[]
		b=random.random()
		if b>0.5:
			for i in range(dim):
				a.append(np.random.normal()*sigma[i] + u1[i])
			a.append(1)
		else:
			for i in range(dim):
				a.append(np.random.normal()*sigma[i] + u0[i])
			a.append(0)
		Xtest.append(a)
	for i in range(dim+1):
		W.append(1.0)

def Probr(X,W):
	temp=0
	for i in range(dim):
		temp=temp+X[i]*W[i]
	son=math.exp(W[dim]+temp)
	return son/(son+1)	
def l(W,X):
	su=0
	for datanum in range(num):
		temp=0
		for i in range(dim):
			temp=temp+W[i]*X[datanum][i]
		su=su+X[datanum][5]*(W[dim]+temp)-math.log(1+math.exp(W[dim]+temp))
	return su	
	
def solute(W,X,Epsilon):
	while True:
		sum=0
		Wold=copy.deepcopy(W)
		Wa=[]
		for i in range(dim+1):
			Wa.append(0.0)
		for datanum in range(num):
			for i in range(dim):
				Wa[i]=Wa[i]+X[datanum][i]*(X[datanum][5]-Probr(X[datanum],W))
			Wa[dim]=Wa[dim]+X[datanum][5]-Probr(X[datanum],W)

		for i in range(dim+1):
			W[i]=W[i]+step*Wa[i]-step*lamata*Wa[i]
		print abs(l(W,X)-l(Wold,X))
		if abs(l(W,X)-l(Wold,X))<Epsilon:
     			break

if __name__ == '__main__':			
	ini(sigma,u1,u0,X,Xtest,W)

	solute(W,X,Epsilon)
	numright=0.0
	for i in range(testnum):
		Y1=0
		tmp=Probr(X[i],W)
		if tmp>0.5:
			Y1=1
		else:
			Y1=0
		if X[i][5]==Y1:
			numright=numright+1.0
        print W
	print "right rate"+str(numright/testnum)
        print "right number" +str(numright)
	print "test number" +str(testnum)






