
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

fileName = pd_df.loc[pd_df['COLOR_OR_STYLE'] == catalog_list, 'FILE_NAME'].iloc[0]
fileimage = pd_df.loc[pd_df['COLOR_OR_STYLE'] == catalog_list, 'FILE_URL'].iloc[0]
img = Image.open(fileimage)
st.image(img)
price = pd_df.loc[pd_df['COLOR_OR_STYLE'] == catalog_list, 'PRICE'].iloc[0]
size = pd_df.loc[pd_df['COLOR_OR_STYLE'] == catalog_list, 'SIZE_LIST'].iloc[0]
desc = pd_df.loc[pd_df['COLOR_OR_STYLE'] == catalog_list, 'UPSELL_PRODUCT_DESC'].iloc[0]
st.write('Price: ', price)
st.write('Size Avaibale:', size)
st.write(Desc)

