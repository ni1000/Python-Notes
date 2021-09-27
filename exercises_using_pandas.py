"""
File Name: Exercises Using Pandas with DataFrames
Description: Selecting Views (data that meets certain criteria) from DataFrames (rows & columns) using Pandas
Author: Nuruddin Isa
Created on: 27/09/2021
"""


# make sure our data file (data.csv) is in the same folder as this python file

# imports pandas and gives it the nickname "pd"
import pandas as pd

# tells pandas to read our data file (data.csv) and call it "df"
df = pd.read_csv("data.csv")

# prints our data file, "df"
print(df)


# we can add functions to this to get different views of the data, e.g. print(df.FUNCTION())

# prints the first 5 lines of "df"
print(df.head())

# prints the size (or shape) of "df" in (rows, columns)
print(df.shape)

# prints the headers and row 1 of "df"
print(df.loc[0])

# prints the headers, row 1, row 3 and row 5 of "df"
print(df.loc[[0, 2,4]])

# prints the headers of the columns as a list
print(df.columns)

# creates a sample of "df", called "df_sample", with 20 rows
df_sample = df.sample(n=20)

# prints the shape of the new "df_sample" in (rows, columns)
print(df_sample.shape)


# we can also add functions to specific columns, e.g. print(df.["COLUMN NAME"].FUNCTION())

# counts the number of times a value occurs in the column called "gender"
print(df["gender"].value_counts())

# counts the number of times a value occurs in the column called "bp_before_exercise"
print(df["bp_before_exercise"].value_counts())

# calculates the mean of the values in the column called "bp_before_exercise"
print(df["bp_before_exercise"].mean())

# calculates the sum of the values in the column called "bp_before_exercise"
print(df["bp_before_exercise"].sum())

# finds the maximum value in the column called "bp_before_exercise"
print(df["bp_before_exercise"].max())

# we can do this to more than one column, e.g. print(df["COLUMN 1"]["COLUMN2"].FUNCTION())


# we can also add conditions to specific columns, e.g. print(df["COLUMN NAME"] > NUMBER)
#                                                   or print(df["COLUMN NAME"] == "STRING")

# returns all rows with a True or False value, where "bp_before_exercise" greater than 150 is True
print(df["bp_before_exercise"] > 150)

# returns all data where the column "agegrp" is equal to "30-45"
print(df[df["agegrp"] == "30-45"])

# calculates the mean values of each column and returns all data grouped by the "agegrp" column
print(df.groupby("agegrp").mean())


# we can also have multiple conditions for multiple columns e.g.
# print(df[(df["COLUMN 1"] > NUMBER) & (df["COLUMN 2"] == "STRING")])

# returns all data where the value in column "bp_before exercise" is above 130 AND below 140
print(df[(df["bp_before_exercise"] > 130) & (df["bp_before_exercise"] < 140)])


# we can also display specific columns only, e.g.
# print(df[df["COLUMN NAME"] > NUMBER][["COLUMN 1", "COLUMN 2"]])
# important to have double (NOT single) square brackets around the To Show columns here

# when column "agegrp" is equal to "30-45", display the columns "bp_before_exercise" and "bp_after_exercise" ONLY
print(df[df["agegrp"] == "30-45"][["bp_before_exercise", "bp_after_exercise"]])


#MARTIN'S EXERCISES:



# Exercise 1:
# show all males with a bp_before_exercise of under 142

print(df    [   (df["gender"] == "Male")   &   (df["bp_before_exercise"] < 142) ]   )

# this can get confusing easily, so we can use variables:

maleGender = (df["gender"] == "Male")
BPBeforeExerciseUnder142 = (df["bp_before_exercise"] < 142)

# and simplify it to:

print(df    [   (maleGender)    &   (BPBeforeExerciseUnder142)  ]   )



# Exercise 2:
# show a count of people with bp_after_exercise of under 140, grouped by age



print(df    [   (df["bp_after_exercise"] < 140) ]   [["agegrp"]]   .value_counts()  )

# or using a variable:

BPAfterExerciseUnder140 = (df["bp_after_exercise"] < 140)

print(df    [   (BPAfterExerciseUnder140)   ]   ["agegrp"] .value_counts()  )



# Exercise 3:
# shows count of females with a bp_before_exercise of over 145



# using variables:

females = (df["gender"] == "Female")
BPBeforeExerciseOver145 = (df["bp_before_exercise"] >145)

print(df    [   (females)   &   (BPBeforeExerciseOver145)   ]   [["gender"]].value_counts() )



# Exercise 4:
# show mean bp_after_exercising of the 60+ age group



print(df    [   (df["agegrp"] == "60+") ]   [["bp_after_exercise"]].mean())

# or using variables:

ageGroup60Plus = (df["agegrp"] == "60+")
print(df    [   (ageGroup60Plus)    ]   [["bp_after_exercise"]].mean()  )