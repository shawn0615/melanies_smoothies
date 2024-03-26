# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize your Smoothie! :cup_with_straw:")
st.write("""Choose the fruits you want in your custom Smoothie!""")

#import streamlit as st

name_on_order = st.text_input('Name on smoothie:')
st.write('The name on the smoothie will be: ', name_on_order)   

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

from snowflake.snowpark.functions import col

session = get_active_session()
my_dataframe = session.table("SMOOTHIES.PUBLIC.FRUIT_OPTIONS").select(col('FRUIT_NAME'))

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients: '
    ,my_dataframe
    ,max_selections=5
)

if ingredients_list:
    st.write(ingredients_list) 
    st.text(ingredients_list)

    ingredients_string = ' '

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    st.write(ingredients_string)

my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

if ingredients_string:
        session.sql(my_insert_stmt).collect()
    
        st.success('Your Smoothie is ordered!', icon="✅")

