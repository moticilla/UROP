from cmath import nan
import csv
from distutils.log import set_verbosity
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#csv_filename = 'my_csv_experiment.csv'
#with open(csv_filename) as f:
#    reader = csv.DictReader(f)
    #for row in reader:
    #    print(row)

df = pd.read_csv('my_csv_experiment.csv')

#print(df.iloc[:,1]) #second column

EUROVENTdf = pd.read_csv('EUROVENT_AC_tr.csv')

#print(EUROVENTdf.iloc[:,47]) #Cooling PL CondB | EER @ 30°C 
#print(EUROVENTdf.iloc[:,51]) #Cooling PL CondC | EER @ 25°C
#print(EUROVENTdf.iloc[:,55]) #Cooling PL CondD | EER @ 20°C 

CondB = pd.DataFrame(EUROVENTdf.iloc[:,[47,16]])
CondB.insert(0, "temp", [30 for n in range(CondB.shape[0])], True)
CondB = CondB.rename(columns={"temp":"Temp",'Cooling PL CondB | EER @ 30°C ':"EER", 
                              "Seasonal Efficiency in Cooling | SEER Class":"SEER class"})
CondB = CondB.loc[np.isnan(CondB["EER"]) == False]
#print(CondB)

CondC = pd.DataFrame(EUROVENTdf.iloc[:,[51,16]])
CondC.insert(0, "temp", [25 for n in range(CondC.shape[0])], True)
CondC = CondC.rename(columns={"temp":"Temp",'Cooling PL CondC | EER @ 25°C':"EER",
                              "Seasonal Efficiency in Cooling | SEER Class":"SEER class"})
CondC = CondC.loc[np.isnan(CondC["EER"]) == False]
#print(CondC)

CondD = pd.DataFrame(EUROVENTdf.iloc[:,[55,16]])
CondD.insert(0, "temp", [20 for n in range(CondD.shape[0])], True)
CondD = CondD.rename(columns={"temp":"Temp",'Cooling PL CondD | EER @ 20°C ':"EER",
                              "Seasonal Efficiency in Cooling | SEER Class":"SEER class"})
CondD = CondD.loc[np.isnan(CondD["EER"]) == False]
#print(CondD)

frames = [CondB, CondC, CondD]
result = pd.concat(frames)
#result.plot(kind='scatter',x='Temp',y='EER',color='red')
#plt.show()

b = CondB["EER"].mean()
c = CondC["EER"].mean()
d = CondD["EER"].mean()

#plt.plot([30,25,20],[b, c, d],".")
#plt.show()

#print(CondB.EER.quantile([0.25,0.75]))

#standard deviation
berr =np.std(CondB.iloc[:,1])
cerr =np.std(CondC.iloc[:,1])
derr =np.std(CondD.iloc[:,1])

#plt.errorbar([30,25,20],[b, c, d],linestyle = ":", yerr = [berr, cerr, derr])
#plt.show()

#CondBSEERB = CondB.loc[CondB["SEER class"] == "B" ]
#CondBSEERA = CondB.loc[CondB["SEER class"] == "A" ]
#CondBSEERA1 = CondB.loc[CondB["SEER class"] == "A+" ]
CondBSEERBAA1 = CondB.loc[(CondB["SEER class"] == "A+") |
                          (CondB["SEER class"] == "A") |
                          (CondB["SEER class"] == "B")]
CondBSEERA2 = CondB.loc[CondB["SEER class"] == "A++" ]
CondBSEERA3 = CondB.loc[CondB["SEER class"] == "A+++" ]

#CondCSEERB = CondC.loc[CondC["SEER class"] == "B" ]
#CondCSEERA = CondC.loc[CondC["SEER class"] == "A" ]
#CondCSEERA1 = CondC.loc[CondC["SEER class"] == "A+" ]
CondCSEERBAA1 = CondC.loc[(CondC["SEER class"] == "A+") |
                          (CondC["SEER class"] == "A") |
                          (CondC["SEER class"] == "B")]
CondCSEERA2 = CondC.loc[CondC["SEER class"] == "A++" ]
CondCSEERA3 = CondC.loc[CondC["SEER class"] == "A+++" ]

#CondDSEERB = CondD.loc[CondD["SEER class"] == "B" ]
#CondDSEERA = CondD.loc[CondD["SEER class"] == "A" ]
#CondDSEERA1 = CondD.loc[CondD["SEER class"] == "A+" ]
CondDSEERBAA1 = CondD.loc[(CondD["SEER class"] == "A+") |
                          (CondD["SEER class"] == "A") |
                          (CondD["SEER class"] == "B")]
CondDSEERA2 = CondD.loc[CondD["SEER class"] == "A++" ]
CondDSEERA3 = CondD.loc[CondD["SEER class"] == "A+++" ]

#SEERb = [CondBSEERB, CondCSEERB, CondDSEERB]
#SEERb = pd.concat(SEERb)
#SEERa = [CondBSEERA, CondCSEERA, CondDSEERA]
#SEERa = pd.concat(SEERa)
#SEERa1 = [CondBSEERA1, CondCSEERA1, CondDSEERA1]
#SEERa1 = pd.concat(SEERa1)

SEERbaa1 = [CondBSEERBAA1, CondCSEERBAA1, CondDSEERBAA1]
SEERbaa1 = pd.concat(SEERbaa1)

SEERa2 = [CondBSEERA2, CondCSEERA2, CondDSEERA2]
SEERa2 = pd.concat(SEERa2)

SEERa3 = [CondBSEERA3, CondCSEERA3, CondDSEERA3]
SEERa3 = pd.concat(SEERa3)

#b = SEERb.plot(kind='scatter',x='Temp',y='EER',color='red',alpha = 0.01)
#a = SEERa.plot(kind='scatter',x='Temp',y='EER',color='red',alpha = 0.01, ax = b)
#a1 = SEERa1.plot(kind='scatter',x='Temp',y='EER',color='red',alpha = 0.01, ax = a)

a1 = SEERbaa1.plot(kind='scatter',x='Temp',y='EER',color='red',alpha = 0.01)
a2 = SEERa2.plot(kind='scatter',x='Temp',y='EER',color='yellow',alpha = 0.01, ax = a1)
SEERa3.plot(kind='scatter',x='Temp',y='EER',color='green',alpha = 0.01, ax = a2)
plt.show()

b1mean = CondBSEERBAA1["EER"].mean()
c1mean = CondCSEERBAA1["EER"].mean()
d1mean = CondDSEERBAA1["EER"].mean()
b2mean = CondBSEERA2["EER"].mean()
c2mean = CondCSEERA2["EER"].mean()
d2mean = CondDSEERA2["EER"].mean()
b3mean = CondBSEERA3["EER"].mean()
c3mean = CondCSEERA3["EER"].mean()
d3mean = CondDSEERA3["EER"].mean()

b1err =np.std(CondBSEERBAA1.iloc[:,1])
c1err =np.std(CondBSEERBAA1.iloc[:,1])
d1err =np.std(CondBSEERBAA1.iloc[:,1])
b2err =np.std(CondBSEERA2.iloc[:,1])
c2err =np.std(CondBSEERA2.iloc[:,1])
d2err =np.std(CondBSEERA2.iloc[:,1])
b3err =np.std(CondBSEERA3.iloc[:,1])
c3err =np.std(CondBSEERA3.iloc[:,1])
d3err =np.std(CondBSEERA3.iloc[:,1])

plt.errorbar([30,25,20],[b1mean, c1mean, d1mean],
             linestyle = "", yerr = [b1err, c1err, d1err], color = 'red')
plt.errorbar([30,25,20],[b2mean, c2mean, d2mean],
             linestyle = "", yerr = [b2err, c2err, d2err], color='yellow')
plt.errorbar([30,25,20],[b3mean, c3mean, d3mean],
             linestyle = "", yerr = [b3err, c3err, d3err], color = 'green')
plt.plot([30,25,20],[b1mean, c1mean, d1mean],".", color = 'red')
plt.plot([30,25,20],[b2mean, c2mean, d2mean],".", color = 'yellow')
plt.plot([30,25,20],[b3mean, c3mean, d3mean],".", color = 'green')
plt.show()