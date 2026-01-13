=none# Import python packages
import streamlit as st
#import requests
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Zina's Amazing Athleisure Catalog")
st.write(
  """Pick a Sweatsuit Color or Size!.
  """
)

#smoothiefroot_response_all = requests.get("https://my.smoothiefroot.com/api/fruit/all")
#st.text(smoothiefroot_response_all.json())
#session = get_active_session()
cnx=st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website").select(col('color_or_style'),col('price'), col('file_url'), col('size_list'),col('upsell_product_desc'))
#st.dataframe(data=my_dataframe, use_container_width=True)

#convert snowpark dataframe to pandas dataframe so we can use Loc function
pd_df = my_dataframe.to_pandas()
#st.dataframe(pd_df)
#st.stop()

catalog_list = st.selectbox("Choose Color", my_dataframe, index=none)

if catalog_list:
    catalog_string = ''
    #catalog_string = catalog_list
    price = pd_df.loc[pd_df['color_or_style'] == catalog_list, 'price'].iloc[0]
    st.subheader(catalog_list + ' Color Selected!')
        #smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/"+search_on)
        #st.text(smoothiefroot_response.json())
        #sf_df = st.dataframe(data=smoothiefroot_response.json(),width="content")
    st.write(catalog_list)

   # my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            #values ('""" + ingredients_string + """','""" + name_on_order + """')"""

    #st.write(my_insert_stmt)

    #time_to_insert = st.button("Submit")

  
    
    #if time_to_insert:
        #session.sql(my_insert_stmt).collect()
        #st.success('Your Smoothie is ordered, '+ name_on_order +' !')
