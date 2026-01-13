import python packages
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


cnx=st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.catalog_for_website").select(col('COLOR_OR_STYLE'),col('PRICE'),  col('FILE_NAME'), col('FILE_URL'), col('SIZE_LIST'),col('UPSELL_PRODUCT_DESC'))
#convert snowpark dataframe to pandas dataframe so we can use Loc function
pd_df = my_dataframe.to_pandas()

catalog_list = st.selectbox("Choose Color", pd_df['COLOR_OR_STYLE'], index=None,)

st.write(catalog_list)
fileName = pd_df.loc[pd_df['COLOR_OR_STYLE'] == catalog_list, 'FILE_NAME']
fileimage = pd_df.loc[pd_df['COLOR_OR_STYLE'] == catalog_list, 'FILE_URL']
st.write(fileName)
st.write(fileimage)

