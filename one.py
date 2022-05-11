import pandas as pd
import numpy as np
import streamlit as st

#generating dataframe
st.subheader("Records in both dataframe.")
df = {
        "id_1":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,35],
        "id_2":[111,211,311,411,511,611,711,811,911,1011,1111,1211,1311,1411,1511,1611,1711,1811,1911,2011,2111,2211,2311,2411,2511,2611,2711,2811,2911,3011,3111,3511],
        "value":[0,20,3,4,53,66,72,81,95,10,1,2,193,140,152,0,7,108,132,0,21,25,2,4,5,126,270,208,249,130,310,350],
        }
df_1 = {
        "id_1":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,33,40],
        "id_2":[111,211,311,411,511,611,711,811,911,1011,1111,1211,1311,1411,1511,1611,1711,1811,1911,2011,2111,2211,2311,2411,2511,2611,2711,2811,3011,3111,3311,4011],
        "value":[0,20,3,4,53,66,72,81,95,10,1,2,193,140,152,0,7,108,132,0,21,25,2,4,5,126,270,208,249,130,310,410],
        }

df_1 = pd.DataFrame(df_1)
df = pd.DataFrame(df)
col = st.columns(2)
with col[0]:
    st.subheader("df")
    st.write(df)
with col[1]:
    st.subheader("df_1")
    st.write(df_1)
# setting of the index for df and df_1
df.set_index(['id_1','id_2'], inplace=True)
df_1.set_index(['id_1','id_2'], inplace=True)

st.subheader("Records present in df but missing in df_1")
data = df[~df.index.isin(df_1.index)].reset_index()
st.write(data)
st.write("Total Records Present :-",len(data))
st.write("Sum of Value in this Record :-",data.value.sum())

st.subheader("Records present in df_1 but missing in df")
data_1 = df_1[~df_1.index.isin(df.index)].reset_index()
st.write(data_1)
st.write("Total Records Present :-",len(data_1))
st.write("Sum of Value in this Record :-",data_1.value.sum())

st.subheader("Total number of unique records present")
df = df.reset_index()
df_1 = df_1.reset_index()
data_2 = pd.concat([df,df_1]).drop_duplicates(keep=False)
st.write(data_2)
st.write("Total Records Present :-",len(data_2))
st.write("Sum of Value in this Record :-",data_2.value.sum())

st.subheader("Different Records Present in Dataframe")
data_try = df[~df.id_1.isin(df_1.id_1)]
st.write(data_try)
st.write("Total Records Present :-",len(data_try))
st.write("Sum of Value in this Record :-",data_try.value.sum())