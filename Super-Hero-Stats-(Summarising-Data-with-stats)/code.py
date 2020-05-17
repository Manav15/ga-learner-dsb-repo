# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 
data=pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
gender_count=data['Gender'].value_counts()
gender_count.plot(kind='bar')
plt.xticks(rotation=360)
plt.show()



# --------------
#Code starts here
alignment=data['Alignment'].value_counts()
alignment.plot(kind='pie',label='Character Alignment')
plt.show()


# --------------
#Code starts here
sc_df=data[['Strength','Combat']]
conv=sc_df.cov()
sc_covariance=conv['Strength']['Combat']
sc_strength=sc_df['Strength'].std()
sc_combat=sc_df['Combat'].std()
sc_pearson=sc_covariance/(sc_combat*sc_strength)

ic_df=data[['Intelligence','Combat']]
convi=ic_df.cov()
ic_covariance=convi['Intelligence']['Combat']
ic_intelligence=ic_df['Intelligence'].std()
ic_combat=ic_df['Combat'].std()
ic_pearson=ic_covariance/(ic_combat*ic_intelligence)



# --------------
#Code starts here
total_high=data['Total'].quantile(q=0.99)
super_best=data[data['Total']>total_high]
super_best_names=[name for name in super_best['Name']]
print(super_best_names)


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3)=plt.subplots(1,3,figsize=(20,10))
data.boxplot(column='Intelligence',ax=ax_1)
data.boxplot(column='Speed',ax=ax_2)
data.boxplot(column='Power',ax=ax_3)
ax_1.set_title('Intelligence')
ax_2.set_title('Speed')
ax_3.set_title('Power')
plt.show()


