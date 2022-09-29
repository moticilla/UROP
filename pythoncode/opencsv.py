from cmath import nan
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

word_freq = {
"Hello": 56,
"at": 23,
"test": 43,
"this": 43
}

#print(word_freq)

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


df2 = pd.DataFrame(df.iloc[:,1])
df2.insert(0, "CondD", [21 for n in range(df2.shape[0])], True)
#print(df2)

CondB = pd.DataFrame(EUROVENTdf.iloc[:,47])
CondB.insert(0, "temp", [30 for n in range(CondB.shape[0])], True)
CondB = CondB.rename(columns={"temp":"Temp",'Cooling PL CondB | EER @ 30°C ':"EER"})
CondB = CondB.loc[np.isnan(CondB["EER"]) == False]
#print(CondB)

CondC = pd.DataFrame(EUROVENTdf.iloc[:,51])
CondC.insert(0, "temp", [25 for n in range(CondC.shape[0])], True)
CondC = CondC.rename(columns={"temp":"Temp",'Cooling PL CondC | EER @ 25°C':"EER"})
CondC = CondC.loc[np.isnan(CondC["EER"]) == False]
#print(CondC)

CondD = pd.DataFrame(EUROVENTdf.iloc[:,55])
CondD.insert(0, "temp", [20 for n in range(CondD.shape[0])], True)
CondD = CondD.rename(columns={"temp":"Temp",'Cooling PL CondD | EER @ 20°C ':"EER"})
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

plt.errorbar([30,25,20],[b, c, d],linestyle = ":", yerr = [berr, cerr, derr])
plt.show()


#data = data.loc[(data["deaths_7_days"] > 0) & (data["deaths_24_hours"] > 0)]