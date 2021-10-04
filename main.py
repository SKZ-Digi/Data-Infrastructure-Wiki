import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from PIL import Image
import os
import base64
st.set_page_config(page_title="IOT Middleware Selection ",layout="wide")
#for image rendering with link, magic from https://discuss.streamlit.io/t/href-on-image/9693/4
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache(allow_output_mutation=True)
def get_img_with_href(local_img_path, target_url,width="1"):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}" target="_blank">
            <img style="width: {width}%" src="data:image/{img_format};base64,{bin_str} " />
        </a>'''
    return html_code
#-------------------------------------------------------------------------------------------------------
#Logo_html = get_img_with_href('Logo.PNG', 'https://www.nweurope.eu/projects/project-search/di-plast-digital-circular-economy-for-the-plastics-industry/',width="100")
#st.sidebar.markdown(Logo_html, unsafe_allow_html=True)


list_categories_money_inital=["<25.000 €","<50.000 €","<100.000 €",">100000 €"]
list_categories_money_anual=["<25.000 €","<50.000 €","<100.000 €",">100000 €"]
list_categories_workload_initial=["<160 hrs €","<480 hrs","<960 hrs",">960 hrs "]
list_categories_workload_anual=["<160 hrs €","<480 hrs","<960 hrs",">960 hrs "]



#st.sidebar.image(image, width=250)
st.sidebar.title('IOT MiddleWare Selection')



money_initial=st.sidebar.selectbox("Initial Budget",list_categories_money_inital,help="Please select your initial software budget​")
money_anual=st.sidebar.selectbox("Anual Budget",list_categories_money_anual,help="Please select your anual software budget​")
time_initiall=st.sidebar.selectbox("Workload initial ",list_categories_workload_initial,help="Please select your initial available workload")
time_anual=st.sidebar.selectbox("Workload anual ",list_categories_workload_anual,help="Please select your anual available workload")

col1 ,col2,col3= st.columns((5,1,5))


with col1:
    list_products=["ProduktA", "ProduktB","ProduktC"]
    st.header("Product Information", anchor=None)
    money_initial=st.selectbox("Recommended Products",list_products,help="Choose Product​")
    st.header("Description", anchor=None)
    txt = st.write('DUMMY TEXT!!! The industrial internet of things (IIoT) refers to interconnected sensors, instruments, and other devices networked together with computers industrial applications, including manufacturing and energy management. This connectivity allows for data collection, exchange, and analysis, potentially facilitating improvements in productivity and efficiency as well as other economic benefits.[1] The IIoT is an evolution of a distributed control system (DCS) that allows for a higher degree of automation by using cloud computing to refine and optimize the process controls.')
    st.subheader("License")
    st.write("License information")
    st.write(f"[www.cybus.io](www.cybus.io)")


with col3:  
    st.header("Short Overview ")
    st.header("Pros", anchor=None)  
    st.write("* pro1")
    st.write("* pro2")
    st.write("* pro3")
    st.header("Cons", anchor=None)  
    st.write("* con1")
    st.write("* con2")
    st.write("* con2")


