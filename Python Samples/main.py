from pprint import pprint
import pandas as pd
import os

# Saves Results to local Desktop with name Results.txt
username = os.getlogin()  # Fetch username
ResultFile = open(f'C:\\Users\\{username}\\Desktop\\Results.txt', 'wt')
########
# 1. Ingest data file into dataframe
########

df = pd.read_csv("datafile.txt", sep='\t')

########
# 2.1: Find the max variance (high-low) its date
########
df['Variance'] = df['High'] - df['Low']
maxVariance = df['Variance'].max()
maxVarianceIndex = df['Variance'].idxmax()
maxVarianceRecord = df.loc[maxVarianceIndex]

ResultFile.write("\n Question 2.1 \n")
ResultFile.writelines(
    "The largest variance was on " + maxVarianceRecord['Date'] +
    ", which has a variance of " + str(round(maxVariance, 3))
)

########
# 2.2: Average volume for July 2022
########
df['Date-Converted'] = pd.to_datetime(df['Date'])
july_data = df.loc[(df['Date-Converted'] >= '2020-07-01') & (df['Date-Converted'] <= '2020-07-31')]
ResultFile.write("\n Question 2.2 \n")
ResultFile.writelines("The average trading volume in July 2020 was " + str(round(july_data['Volume'].mean(), 3)))

########
# 2.3: Months where performance was same (+ or -) YoY
########
# Sort dates with earlist first
df.sort_values('Date-Converted', inplace=True)
resultDf = df.groupby(
    by=[
        df['Date-Converted'].dt.year,
        df['Date-Converted'].dt.month
    ]
).agg(["first", "last"])

# Set the performance for each month as True (net positive) or False (net negative)
resultDf["performance"] = resultDf[("Close", "last")] > resultDf[("Open", "first")]
ResultFile.write("\n Question 2.3 \n")
ResultFile.write("Months whose YoY performance was the same from 2020 to 2021: \n")
for month in range(1, 12):
    mmxx = resultDf.loc[2020, month]
    mmxxi = resultDf.loc[2021, month]

    if (mmxx.performance.iloc[0] == mmxxi.performance.iloc[0]):
        ResultFile.writelines(
            str(mmxx['Date-Converted'].dt.month['first']) +
            str(' (positive) ' if mmxx.performance.iloc[0] else ' (negative) \n')
        )

########
# 2.4: Max vol by month where intra-day > 1.5
########

# create dataframe with variance > 1.5
df = df.query('Variance > 1.5')
# pprint(df)

dfm = df.groupby(
    by=[
        df['Date-Converted'].dt.year,
        df['Date-Converted'].dt.month
    ],
    group_keys=True
).apply(lambda x: x)
ResultFile.write("\n Question 2.4 \n")
ResultFile.write("Max Variance and Volume by Month with Intra-Day > 1.5: \n")
for year in [2020, 2021]:
    for month in range(1, 12):
        maxVariance = dfm.loc[year, month]['Variance'].max()
        maxVolume = dfm.loc[year, month]['Volume'].max()

        maxVarianceIndex = dfm.loc[year, month]['Variance'].idxmax()
        maxVolumeIndex = dfm.loc[year, month]['Volume'].idxmax()

        maxVarianceRecord = dfm.loc[year, month].loc[maxVarianceIndex]
        maxVolumeRecord = dfm.loc[year, month].loc[maxVolumeIndex]

        ResultFile.writelines(
            str(year) + '-' + str(month) + ' max variance: ' + str(round(maxVariance, 3)) + ' (on ' + maxVarianceRecord[
                'Date'] + ')' + ' max Volume: ' + str(round(maxVolume, 3)) + ' (on ' + maxVolumeRecord[
                'Date'] + ') \n')

        # pprint(maxVarianceRecord)
ResultFile.close()
