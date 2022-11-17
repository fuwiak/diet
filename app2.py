import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


df = pd.read_csv('selected_clean.csv', sep = ",", encoding = "utf-8") #чтение данных
df = df[['message', 'message_clean']]
df = df[:1000]

match_saved = pd.read_csv('match_saved.csv', sep = ",", encoding = "utf-8") #чтение данных


st.title("Анализатор переписки между тренером и клиентом")

st.markdown(''' ### примеры удаленных смайликов ''')

def show_table_grid(data):
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb.configure_side_bar() #Add a sidebar
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    gridOptions = gb.build()
    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT',
        update_mode='MODEL_CHANGED',
        fit_columns_on_grid_load=True,
        enable_enterprise_modules=True,
        height=600,
        width='100%',
        reload_data=True
    )
    return grid_response

show_table_grid(df)

#markdown
st.markdown(''' ### примеры вытащенных фраз(Приветствие в переписке) ''')

show_table_grid(match_saved)
