import pandas as pd
import matplotlib.pyplot as plt

# importing data from csv files
homeownership = pd.read_csv('home_ownership_data.csv')
loandata = pd.read_csv('loan_data.csv')
# merging both files based on member_id
merged = homeownership.merge(loandata, on="member_id", how="outer").fillna("")
merged.to_csv('merged.csv', index=False)
# import merged csv files as Dataframe
final = pd.read_csv('merged.csv', usecols=[0, 1, 2])
# create groups based on homeownership type
output = final.groupby('home_ownership')
#compute the average for each loan category
output = output['loan_amnt'].mean().reset_index().rename(
    columns={'home_ownership': 'Home Ownership', 'loan_amnt': 'Average loan'})
print(output)
#plot in a bar graph the resulting means
output.plot(kind='bar',x='Home Ownership',y='Average loan',title='Average loan amount per home ownership')
plt.xticks(rotation=0)
plt.xlabel('Home Ownership')
plt.ylabel('Average Loan')
print(plt.show())

