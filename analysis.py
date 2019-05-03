import pandas as pd
import matplotlib.pyplot as mt
import statistics as st
import math
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
data1 = pd.read_csv("./data/0-75U1--1-64U3--170T.csv")
data2 = pd.read_csv("./data/0.75U1--1.75U3--170T.csv")
data3 = pd.read_csv("./data/0.85U1--1.73U3--170T.csv")
data4 = pd.read_csv("./data/0-75U1--1-65U3--182T.csv")
data5 = pd.read_csv("./data/0.75U1--1.75U3--182T.csv")
data6 = pd.read_csv("./data/0.85U1--1.73U3--182T.csv")
data7 = pd.read_csv("./data/0-75U1--1-64U3--192T.csv")
data8 = pd.read_csv("./data/1-00U1--1-64U3--200T.csv")
data9 = pd.read_csv("./data/1-30U1--1-64U3--211T.csv")
data10 = pd.read_csv("./data/1-30U1--1-64U3--220T.csv")
data1['Character'] = 1
data2['Character'] = 2
data3['Character'] = 3
data4['Character'] = 4
data5['Character'] = 5
data6['Character'] = 6
data7['Character'] = 7
data8['Character'] = 8
data9['Character'] = 9
data10['Character'] = 10
#data = pd.concat([data1,data2,data3,data4,data5,data6,data7,data8,data9,data10])
#data.drop(['f'],axis=1)
#data.to_csv("Data.csv")
#mt.plot(data1.U_2,data1.I_A,color="black")
#mt.scatter(data1.U_2,data1.I_A,color="green")
peak1=[5.63,10.04,15.18,20.13,25.35,30.6]
peak2=[5.20,10.15,15.2,20.28,25.09,30.06]
peak3=[5.13,9.94,15.11,20.21,25.38,30.05]
peak4=[5.34,10.08,14.90,20.28,25.09,30.47]
peak5=[5.39,9.96,15.11,20.18,25.40,30.20]
peak6=[5.56,10.08,15.11,19.99,25.16,30.47]
peak7=[5.20,10.01,14.89,20.06,24.95,30.19]
peak8=[4.99,10.13,14.99,19.50,24.79,29.86]
peak9=[5.23,10.05,14.81,19.96,24.79,29.70]
peak10=[5.49,10.23,15.11,19.85,24.73,29.61]
arr = []
for i in range(len(peak1) - 1):
    arr.append(peak1[i+1]-peak1[i])
    arr.append(peak2[i+1]-peak2[i])
    arr.append(peak3[i+1]-peak3[i])
    arr.append(peak4[i+1]-peak4[i])
    arr.append(peak5[i+1]-peak5[i])
    arr.append(peak6[i+1]-peak6[i])
    arr.append(peak7[i+1]-peak7[i])
    arr.append(peak8[i+1]-peak8[i])
    arr.append(peak9[i+1]-peak9[i])
    arr.append(peak10[i+1]-peak10[i])
smean = st.mean(arr)
std = st.stdev(arr)
n = len([1,3,1,4,15,4,5,9,4,4])                          
mean = sum([1,3,1,4,15,4,5,9,4,4])/n
sigma = st.stdev([1,3,1,4,15,4,5,9,4,4])
xarr = []
for x in range(len(arr)):
    xarr.append(4.4+(x/50))
def gaus(x,a,x0,sigma):
    return a*exp(-(x-x0)**2/(2*sigma**2))
popt,pcov = curve_fit(gaus,[4.4,4.5,4.6,4.7,4.8,4.9,5.0,5.1,5.2,5.3],[1,3,1,4,15,4,5,9,4,4],p0=[1,mean,sigma])
meanarr = [4.99,4.97,4.98,5.03,4.96,4.98,4.99,4.97,4.89,4.82]
stdarr = [0.35,0.11,0.23,0.32,0.27,0.30,0.19,0.30,0.15,0.08]
top,bottom,meanw,stdw = 0,0,0,0
for r in range(len(meanarr)):
    top += ((meanarr[r])/(stdarr[i]**2))
    bottom += ((1)/(stdarr[i]**2))
wmean = top/bottom
wstd = math.sqrt(1/bottom)   
mt.hist(arr)
mt.plot(ar(xarr),gaus(ar(xarr),*popt))










    