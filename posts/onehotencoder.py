#%%
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = {'location': ['urban', 'suburban', 'rural'], 'size_sqft': [1000, 1500, 1200]}
df = pd.DataFrame(data)

encoder = OneHotEncoder(drop='first', sparse_output=False)
X_encoded = encoder.fit_transform(df[['location']])

# Resulting one-hot encoded columns

df_enc = pd.DataFrame(
    X_encoded, 
    columns=encoder.get_feature_names_out()
)
df_enc = pd.concat([df_enc, df[['size_sqft']]], axis=1)
df_enc
#%%
df
# %%
