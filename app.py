import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import numpy as np
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.graph_objs as go
import plotly.express as px
import streamlit_option_menu as option_menu


with open("styles.css") as source_style:
    st.markdown(f"<style>{source_style.read()}</style>",
                unsafe_allow_html=True)


with st.sidebar:
  selected = option_menu.option_menu(menu_title="Main Menu", options=["Home", "EDA"])

if selected == "Home":
  st.markdown("""<div style="font-size: 30px; line-height: 1.4; font-weight: 500"> Monitoring the Water Quality in Bhopal Region using Satellite Imagery and GIS Techniques </div>""",
                unsafe_allow_html=True)
  
  st.markdown('\n')

  st.subheader('THE BACKGROUND:')

  st.markdown("""<p align = "justify">In the 1980s, the Bhopal region experienced one of the worst industrial disasters marked to date. The catastrophe raised awareness about industrial pollution. The water quality of the lakes in Bhopal has been significantly impacted by the 1984 gas tragedy. The release of toxic chemicals from the Union Carbide India Limited (UCIL) pesticide plant has contaminated the ground and surface water in the area, including the lakes. Tests conducted on the groundwater in communities situated around the Union Carbide factory in Bhopal have revealed high levels of pollutants such as heavy metals like lead, mercury, cadmium, Gamma HCH, Lindane, Beta HCH, Styrene, Mercury, Alpha HCH, Alpha Naphthol, Phosgene, Dichlorobenzene, etc.</p> <p align = "justify">In the years that followed, the Bhopal region dealt with environmental challenges, particularly regarding water quality. The lakes are also heavily polluted with volatile organic compounds (VOCs), such as benzene and toluene, pesticides, herbicides, and Polycyclic aromatic hydrocarbons, leading to a decline in fish and other aquatic life. The water is also not safe for swimming or other recreational activities.</p>""", unsafe_allow_html = True)

  st.markdown('\n')
  
  st.subheader('THE PROBLEM:')

  st.markdown("""<p align = "justify">Bhopal is also known as “The City of Lakes”, which indicates that Bhopal has a significant quantity of Lakes. People who live in the area are constantly in contact with chemicals assimilated in the water bodies during Gas Tragedy.  Surveys done by the Bhopal campaign groups have shown that their environment contains six of the persistent organic pollutants banned by the United Nations for their highly poisonous impacts on the environment and human health, which has now reached 42 areas in Bhopal and continues to spread. According to the Surveyors, the situation is getting worse, and second and third-generation children are being born with disabilities.</p> <p align = "justify">Apart from this, during the “Gas Tragedy”, MIC(methyl isocyanide) was released, which reacts with water exothermically and produces carbon dioxide, methylamine, dimethylurea, and/or trimethyl biuret, these chemicals cause adverse effects on human bodies while incorporating itself to water. Swiss lab results show chloroform concentrations as many as 3.5 times higher than drinking-water guidelines from the World Health Organization and U.S. EPA , and carbon tetrachloride at up to 2,400 times higher than the guidelines, which impels us to study various lakes of Bhopal.</p>""", unsafe_allow_html = True)

  st.markdown('\n')
  
  st.subheader('THE PROJECT GOALS:')

  st.markdown("""<p align = "justify">This study aims to develop a Machine Learning system for monitoring the water quality of multiple lakes in the Bhopal region using satellite imagery and GIS techniques. The objective is to assess the water quality, detect the probable causes of water pollution and predict the potential impacts of different pollution sources on the environment and human health. The study will use a combination of remote sensing techniques, image processing methods, and GIS tools to extract relevant information from satellite data. Additionally, the system will enable real-time monitoring of water quality, allowing for timely intervention in case of any deterioration in water quality.</p>""", unsafe_allow_html = True)

 
elif selected == "EDA":
  st.markdown("""<h style ="font-size: 30px; font-weight: 400"> Exploratory Data Analysis </h>""", unsafe_allow_html = True)
 
  st.sidebar.subheader("Visualisation Settings")


  chart_select = st.sidebar.selectbox(
    label = "Select the Lake",
    options = ['Hathaikheda Dam', 'Sarangpani Lake', 'Upper Lake', 'Lendiya Lake']
  )
  if chart_select == 'Hathaikheda Dam':
    df = pd.read_csv('Hathaikheda.csv')
    st.subheader('Hathaikheda Dam')   
    import folium
    from streamlit_folium import folium_static
    shape_tuple = [[23.250265289120904, 77.40540829355803], [23.250107568377107, 77.40497914011564], [23.24987098691169, 77.40454998667326], [23.249397822721765, 77.40394917185392], [23.249634405026583, 77.40296211893644], [23.250068138162035, 77.40188923533049], [23.25014699858056, 77.40124550516691], [23.25006813816203, 77.40030136759368], [23.250738450233026, 77.39922848398771], [23.250975030159537, 77.39828434641447], [23.25046243978831, 77.3976406162509], [23.249910417185077, 77.39802685434904], [23.249358392296827, 77.39879933054533], [23.249042948477634, 77.39957180674162], [23.248688073289212, 77.40017262156096], [23.248490919998734, 77.40068760569181], [23.248057181733795, 77.40128842051116], [23.247584011108767, 77.40214672739592], [23.247307994135603, 77.40261879618254], [23.247071407703988, 77.40334835703459], [23.2469136831831, 77.40407791788664], [23.246598233581782, 77.4051508014926], [23.245888469251092, 77.40480747873869], [23.245415290932417, 77.40429249460783], [23.245060406091877, 77.40356293375578], [23.244390065483675, 77.40274754221525], [23.244035177915574, 77.40214672739592], [23.24344369653732, 77.40150299723234], [23.242852212536526, 77.40154591257658], [23.243049374161522, 77.40227547342865], [23.243443696537323, 77.40283337290373], [23.24360142516129, 77.40334835703459], [23.24387744980447, 77.40407791788664], [23.244390065483675, 77.40472164805021], [23.244666088495027, 77.40523663218109], [23.24490267919301, 77.40588036234465], [23.24569131182231, 77.40635243113127], [23.246203920530995, 77.40738239939299], [23.246203920530995, 77.40798321421232], [23.24608562638846, 77.40849819834318], [23.247426287194042, 77.40858402903166], [23.248214904902426, 77.40901318247404], [23.248964087406257, 77.40944233591642], [23.25006813816203, 77.41000023539152], [23.250608695872465, 77.41072979624357], [23.250805846032197, 77.41012898142424], [23.25139729476258, 77.41060105021086], [23.25171273301285, 77.41111603434172], [23.251633873520237, 77.4121030872592], [23.25151558419388, 77.41287556345549], [23.251160715585222, 77.41381970102873], [23.25147615439511, 77.41377678568449], [23.252028170516947, 77.41364803965178], [23.252580184353608, 77.41326180155363], [23.252974478552105, 77.4126609867343], [23.253329342333874, 77.41177199151964], [23.25376306345126, 77.41155741479845], [23.25407849610504, 77.41108534601183], [23.25415735415188, 77.41065619256945], [23.254630501453526, 77.40958330896349], [23.25447278587288, 77.4090254094884], [23.254196783157816, 77.40889666345568], [23.253684205171215, 77.40859625604601], [23.253171625214122, 77.40812418725939], [23.252737902172907, 77.40773794916124], [23.252383036817132, 77.40726588037462], [23.25194931121088, 77.40675089624376], [23.251633873520237, 77.40615008142443], [23.251279005226362, 77.40567801263781], [23.250529835726965, 77.40584967401476], [23.250265289120904, 77.40540829355803]]

    # Create a Folium map
    m = folium.Map(location=[23.250265289120904, 77.40540829355803], zoom_start=15)

    # Add a marker to the map
    #folium.Marker([42.363600, -71.099500], popup="My Marker").add_to(m)

    # Add a polygon to the map using the shape tuple
    folium.Polygon(locations=shape_tuple, color='blue', fill_opacity=0.3).add_to(m)

    # Render the map in Streamlit
    folium_static(m)
      
  elif chart_select == 'Sarangpani Lake' :
    df = pd.read_csv('SarangpaniLakefinal.csv')
    st.subheader('Sarangpani Lake')
    coord = pd.DataFrame(np.random.randn(1, 2) / [50, 50] + [23.248495831047396, 77.34005483732471], columns=['lat', 'lon'])      
    st.map(coord)
    
  elif chart_select == 'Upper Lake' :
    df = pd.read_csv('UPlake.csv')
    st.subheader('Upper Lake')
    coord = pd.DataFrame(np.random.randn(1, 2) / [50, 50] + [23.248495831047396, 77.34005483732471], columns=['lat', 'lon'])      
    st.map(coord)
    
  elif chart_select == ('Lendiya Lake'):
    df = pd.read_csv('Lendiya.csv')
    st.subheader('Lendiya Lake')
    coord = pd.DataFrame(np.random.randn(1, 2) / [50, 50] + [23.248495831047396, 77.34005483732471], columns=['lat', 'lon'])      
    st.map(coord)


   
  show_data = st.sidebar.checkbox("Show dataset")

  if show_data:
    st.write(df)

  global numeric_columns
  try:
    numeric_columns  = list(df.select_dtypes(['float','int' ]).columns)
  except Exception as e:
    print(e)
    


  chart_select = st.sidebar.selectbox(
    label = "Select the Chart Type",
    options = ['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
  )

  if chart_select == 'Scatterplots':
    st.sidebar.subheader('Scatterplot Settings')
    try:
        x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
        plot = px.scatter(data_frame = df, x = x_values, y = y_values, color = "#FF6161")
        st.plotly_chart(plot, theme = None, use_container_width = True)
    except Exception as e:
        print(e)

  if chart_select == 'Lineplots':
    st.sidebar.subheader('Lineplots Settings')
    try:
        x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
        plot = px.area(data_frame = df, x = x_values, y = y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

  if chart_select == 'Boxplot':
    st.sidebar.subheader('Boxplot Settings')
    try:
        x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
        plot = px.box(data_frame = df, x = x_values, y = y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

  if chart_select == 'Histogram':
    st.sidebar.subheader('Histogram Settings')
    try:
        x_values = st.sidebar.selectbox('Select the variable to plot histogram', options = numeric_columns)
        bins = st.sidebar.slider("Select the number of bins", min_value=5, max_value=50, value=20, step=1)
        plot = px.histogram(data_frame = df, x = x_values, nbins=bins)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
