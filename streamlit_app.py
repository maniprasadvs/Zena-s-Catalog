# Import python packages
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
my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website").select(col('COLOR_OR_STYLE'),col('PRICE'),  col('FILE_NAME'), col('FILE_URL'), col('SIZE_LIST'),col('UPSELL_PRODUCT_DESC'))
#st.dataframe(data=my_dataframe, use_container_width=True)

#convert snowpark dataframe to pandas dataframe so we can use Loc function
pd_df = my_dataframe.to_pandas()
#st.dataframe(pd_df)
#st.stop()

catalog_list = st.selectbox("Choose Color", pd_df['COLOR_OR_STYLE'], index=None,)

st.write(catalog_list)
fileName = pd_df.loc[pd_df['COLOR_OR_STYLE'] == catalog_list, 'FILE_NAME']
fileimage = pd_df.loc[pd_df['COLOR_OR_STYLE'] == catalog_list, 'FILE_URL']
st.write(fileName)
st.write(fileimage)
image = fileimage + '/' + fileName
#st.image(image)
price = pd_df.loc[pd_df['COLOR_OR_STYLE'] == catalog_list, 'PRICE']
size=fileimage = pd_df.loc[pd_df['COLOR_OR_STYLE'] == catalog_list, 'SIZE_LIST']
desc = pd_df.loc[pd_df['COLOR_OR_STYLE'] == catalog_list, 'UPSELL_PRODUCT_DESC']
st.write('Price :', price)
st.write(desc)

   # my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            #values ('""" + ingredients_string + """','""" + name_on_order + """')"""

    #st.write(my_insert_stmt)

    #time_to_insert = st.button("Submit")

  
    
    #if time_to_insert:
        #session.sql(my_insert_stmt).collect()
        #st.success('Your Smoothie is ordered, '+ name_on_order +' !')
