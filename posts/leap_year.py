#%% Import the libraries
import pandas as pd
# %% Define the start and end dates
birth_date = "1990-02-12"
end_date = pd.Timestamp.now() + pd.DateOffset(month=12)

# %% Create the date range
date_range = pd.date_range(start=birth_date, end=end_date, freq="12ME")

# %% Create a DataFrame with the date range
df = pd.DataFrame(date_range, columns=["Date"])
df
# %% Calculate number of days in each month
df["days_in_month"] = df["Date"].dt.days_in_month
df
# %% Identify the leap years
df["leap_year"] = df["Date"].dt.is_leap_year
df
# %% Filter the leap years
leap_years = df[df["leap_year"]]
leap_years
# %%
