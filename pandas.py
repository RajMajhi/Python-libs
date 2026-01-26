import pandas as pd # for data handling 
import matplotlib.pyplot as plt # for visualization

df = pd.read_csv(r"C:\Users\rajm4\Downloads\complete.csv")
print(df.head())

import pandas as pd # for data handling 
import matplotlib.pyplot as plt # for visualization
df = pd.read_csv(r"C:\Users\rajm4\Downloads\complete.csv")
print(df.head())

df.columns = df.columns.str.strip() # remove unwanted spaces in column names
df['Date']= pd.to_datetime(df['Date'])#This lets matplotlib treat dates properly on the x-axis

print(df.columns)

state_name = 'Maharashtra'  # change to any state you want
state_data = df[df['Name of State / UT'] == state_name]

plt.figure(figsize=(10,5))
plt.plot(state_data['Date'], state_data['Total Confirmed cases'], label=state_name)

plt.title(f"COVID Total Confirmed Cases Over Time - {state_name}")
plt.xlabel("Date")
plt.ylabel("Total Confirmed Cases")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

state_name = 'Kerala'  # change to any state you want
state_data = df[df['Name of State / UT'] == state_name]

plt.figure(figsize=(10,5))
plt.plot(state_data['Date'], state_data['Total Confirmed cases'], label=state_name)

plt.title(f"COVID Total Confirmed Cases Over Time - {state_name}")
plt.xlabel("Date")
plt.ylabel("Total Confirmed Cases")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

state_name = 'Tamil Nadu'  # change to any state you want
state_data = df[df['Name of State / UT'] == state_name]

plt.figure(figsize=(10,5))
plt.plot(state_data['Date'], state_data['Total Confirmed cases'], label=state_name)

plt.title(f"COVID Total Confirmed Cases Over Time - {state_name}")
plt.xlabel("Date")
plt.ylabel("Total Confirmed Cases")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

state_name = 'Bihar'  # change to any state you want
state_data = df[df['Name of State / UT'] == state_name]

plt.figure(figsize=(10,5))
plt.plot(state_data['Date'], state_data['Total Confirmed cases'], label=state_name)

plt.title(f"COVID Total Confirmed Cases Over Time - {state_name}")
plt.xlabel("Date")
plt.ylabel("Total Confirmed Cases")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

state_name = 'Assam'  # change to any state you want
state_data = df[df['Name of State / UT'] == state_name]

plt.figure(figsize=(10,5))
plt.plot(state_data['Date'], state_data['Total Confirmed cases'], label=state_name)

plt.title(f"COVID Total Confirmed Cases Over Time - {state_name}")
plt.xlabel("Date")
plt.ylabel("Total Confirmed Cases")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

state_data = state_data.sort_values('Date')

state_data['7day_avg'] = state_data['New cases'].rolling(window=7).mean()

plt.figure(figsize=(10,5))
plt.plot(state_data['Date'], state_data['New cases'], alpha=0.4, label='Daily New Cases')
plt.plot(state_data['Date'], state_data['7day_avg'], color='red', label='7-Day Moving Average')

plt.title(f"Daily New Cases Trend with Moving Average - {state_name}")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

pivot_df = df.pivot_table(
    index='Date',
    columns='Name of State / UT',
    values='Total Confirmed cases'
)

top_states = pivot_df.max().sort_values(ascending=False).head(5).index
pivot_df[top_states].plot(figsize=(12,6))

plt.title("COVID Case Trends - Top 5 Indian States")
plt.xlabel("Date")
plt.ylabel("Total Confirmed Cases")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(title="States")
plt.tight_layout()
plt.show()


pivot_df.plot(figsize=(12,6), alpha=0.4, legend=False)
plt.title("COVID Trends - All Indian States & UTs")
plt.xlabel("Date")
plt.ylabel("Total Confirmed Cases")
plt.grid(True)
plt.tight_layout()
plt.show()

pivot_smooth = pivot_df.rolling(window=7).mean()

pivot_smooth[top_states].plot(figsize=(12,6))
plt.title("7-Day Moving Average - Top 5 States")
plt.xlabel("Date")
plt.ylabel("Cases (7-Day Avg)")
plt.grid(True)
plt.tight_layout()
plt.show()




