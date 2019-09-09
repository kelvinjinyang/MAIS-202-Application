import pandas as pd
import matplotlib.pyplot as plt

# importing data from csv files
homeownership = pd.read_csv('home_ownership_data.csv')
loandata = pd.read_csv('loan_data.csv')
# merging both files based on id
merged = homeownership.merge(loandata, on="member_id", how="outer").fillna("")
merged.to_csv('merged.csv', index=False)
# import merged as Dataframe
final = pd.read_csv('merged.csv', usecols=[0, 1, 2])
# groupby
output = final.groupby('home_ownership')
output = output['loan_amnt'].mean().reset_index().rename(
    columns={'home_ownership': 'Home Ownership', 'loan_amnt': 'Average loan'})
print(output)

output.plot(kind='bar',x='Home Ownership',y='Average loan')
plt.suptitle('Average loan size by home ownership')
plt.xlabel('Home Ownership')
plt.ylabel('Average Loan')
print(plt.show())

