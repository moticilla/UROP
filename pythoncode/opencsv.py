from cmath import nan
import csv
from distutils.log import set_verbosity
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

#data = data.loc[(data["deaths_7_days"] > 0) & (data["deaths_24_hours"] > 0)]
CondBSEERB = CondB.loc[CondB["SEER class"] == "B" ]
CondBSEERA = CondB.loc[CondB["SEER class"] == "A" ]
CondBSEERA1 = CondB.loc[CondB["SEER class"] == "A+" ]
CondBSEERA2 = CondB.loc[CondB["SEER class"] == "A++" ]
CondBSEERA3 = CondB.loc[CondB["SEER class"] == "A+++" ]

CondCSEERB = CondC.loc[CondC["SEER class"] == "B" ]
CondCSEERA = CondC.loc[CondC["SEER class"] == "A" ]
CondCSEERA1 = CondC.loc[CondC["SEER class"] == "A+" ]
CondCSEERA2 = CondC.loc[CondC["SEER class"] == "A++" ]
CondCSEERA3 = CondC.loc[CondC["SEER class"] == "A+++" ]

CondDSEERB = CondD.loc[CondD["SEER class"] == "B" ]
CondDSEERA = CondD.loc[CondD["SEER class"] == "A" ]
CondDSEERA1 = CondD.loc[CondD["SEER class"] == "A+" ]
CondDSEERA2 = CondD.loc[CondD["SEER class"] == "A++" ]
CondDSEERA3 = CondD.loc[CondD["SEER class"] == "A+++" ]

SEERb = [CondBSEERB, CondCSEERB, CondDSEERB]
SEERb = pd.concat(SEERb)

SEERa = [CondBSEERA, CondCSEERA, CondDSEERA]
SEERa = pd.concat(SEERa)

SEERa1 = [CondBSEERA1, CondCSEERA1, CondDSEERA1]
SEERa1 = pd.concat(SEERa1)

SEERa2 = [CondBSEERA2, CondCSEERA2, CondDSEERA2]
SEERa2 = pd.concat(SEERa2)

SEERa3 = [CondBSEERA3, CondCSEERA3, CondDSEERA3]
SEERa3 = pd.concat(SEERa3)

b = SEERb.plot(kind='scatter',x='Temp',y='EER',color='red',alpha = 0.01)
a = SEERa.plot(kind='scatter',x='Temp',y='EER',color='red',alpha = 0.01, ax = b)
a1 = SEERa1.plot(kind='scatter',x='Temp',y='EER',color='red',alpha = 0.01, ax = a)
a2 = SEERa2.plot(kind='scatter',x='Temp',y='EER',color='yellow',alpha = 0.01, ax = a1)
SEERa3.plot(kind='scatter',x='Temp',y='EER',color='green',alpha = 0.01, ax = a2)
plt.legend()
plt.show()