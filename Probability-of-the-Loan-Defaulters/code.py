# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
total=len(df)
p_a=len(df[df['fico']>700])/total

p_b=len(df[df['purpose']=='debt_consolidation'])/total

df1=pd.DataFrame(df[df['purpose']=='debt_consolidation'])

p_a_b=p_a/p_b

if(p_a_b==p_a):
    result=True
else:
    result=False

print(result)



# code ends here


# --------------
# code starts here
total=len(df)
prob_lp=len(df[df['paid.back.loan']=='Yes'])/total
prob_cs=len(df[df['credit.policy']=='Yes'])/total
new_df=len(df[df['credit.policy']=='Yes'])

prob_lp_cs=len(df[(df['paid.back.loan']=='Yes') & (df['credit.policy']=='Yes')])/total
prob_pd_cs=prob_lp_cs/prob_lp

print(prob_pd_cs)

bayes=(prob_pd_cs*prob_lp/prob_cs)

print(bayes)

# code ends here


# --------------
# code starts here
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(12,18))
df['purpose'].value_counts().plot(kind='bar',ax=ax1)
df1=pd.DataFrame(df[df['paid.back.loan']=='No'])

df1['purpose'].value_counts().plot(kind='bar',ax=ax2)

# code ends here


# --------------
# code starts here
inst_median=df['installment'].median()

inst_mean=df['installment'].mean()

df.hist(column='installment',bins=10)
plt.axvline(x=inst_mean,color='black')
plt.axvline(x=inst_median,color='green')

df.hist(column='log.annual.inc',bins=10)

plt.show()
# code ends here


