pip import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
from PIL import Image



img = Image.open("netflix_PNG10.png")
st.set_page_config(
    page_title="Netflix Dashboard",
    page_icon=img,
    layout = "wide",
)

@st.cache
def load_data():
    df = pd.read_csv('cleaned/titles.csv')
    df_credits = pd.read_csv('cleaned/credits.csv')
    df_movie = pd.read_csv('cleaned/movie_tc.csv')
    df_show = pd.read_csv('cleaned/show_tc.csv')
    return df,df_credits,df_movie,df_show

# load the data
df,df_credits,df_movie,df_show = load_data()

def _max_width_():
    max_width_str = f"max-width: 1400px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


_max_width_()

col1, mid, col2 = st.columns([1,1,60])
with col1:
    st.image('netflix_PNG10.png',width=65)
with col2:
    st.title('etflix Demographics')

with st.expander("ℹ️ - About this project", expanded=True):
    st.markdown("### Background:")
    st.write("-  The title of our project is ‘Netflix Demographics’. The motivation behind choosing this project is the large amount of data that the 2 datasets namely credits, and titles has on various attributers which will help us to visualize and provide insights on the topic for the Netflix use. The titles dataset has over 5000 records with attributes such as character, role, name, person id, whereas the titles dataset has over 70000 records with attributes such as genres, release year, age certification, runtime, production countries. This project helps us to make inferences and provide answers to understand the distribution of the movies and tv shows based on release year, top 15 contributing countries on Netflix, total content added across all years up to 2019, etc. The project’s main goal is to visualize the large amount of data to assist the users in analyzing the data and answering their questions. The data will be displayed to user in different ways, which will also help the user in better decision making and helps to identify the patterns in the data. We have presented our visualizations with help of Map views, Bar graph and line graphs. The Map view will allow the users to see the geospatial data and thus making the data easier to understand. We’ve also used the bar graphs and line graphs to show the relationship between the two different attributes and added the filters to filter the data based on various categories within the visualizations.")
    st.markdown("### How we built our project ?")
    st.write(
        """     
-   As part of the project, The two datasets are cleaned and transformed into various different datasets to meet our requirements. 
    They are as follow: 
    1. credits (treated the null values)
    2. titles (treated the null values)
    3. show_titles (titles are divided into type = show)
    4. movie_titles (titles are divided into type = movie and removed seasosn column from the dataset)
    5. movie_tc (movie_title and credits are merged using ids) 
    6. show_tc (show_title and credits are merged using ids0 
    7. popuar_movie (Removed the null imdb_id's and replvisualizationsaced the other null values with their mean)  
    8. popular_show (Removed the null imdb_id's and replaced the other null values with their mean)
-	We've used these datasets and built some interactive dashboards in Tableau and integrated those into the streamlit.     
-   We also dicussed few questions and tried to answer using  that are designed using a package callled Plotly.        
"""
    )
    st.markdown("### Tools and Packages:")
    st.write("""
-    Tableau
-    Python
-    Packages:
     1. streamlit
     2. pandas
     3. numpy
     4. plotly.express
     5. Pillow
    """)

    st.markdown("### Links and Ref:")
    st.write("-  Check out this for all the dashboards that are created for this project : https://public.tableau.com/app/profile/jayanth.telu")
    st.write("-  Check this out for the source code : https://github.com/Jayanth-Dileep/Netflix_EDA/blob/main/project.py")
    st.markdown("")

col1, mid, col2 = st.columns([1,1,60])
with mid:
    st.markdown("")
st.markdown("## 🌐 Raw Data")
   
st.markdown("")
see_data = st.expander('You can click here to see the raw data first 👉')
with see_data:
    if st.button("titles.csv"):
        st.dataframe(data=df.reset_index(drop=True))
    if st.button("credits.csv"):
        st.dataframe(data=df_credits.reset_index(drop=True))
st.text('')
col1, mid, col2 = st.columns([1,1,60])
with mid:
    st.markdown("")


html_Overall = """
<div class='tableauPlaceholder' id='viz1670178911855' style='position: relative'><noscript><a href='#'><img alt='Netflix Dashnoard ' 
        src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ne&#47;NetflixDashboard_16701341279220&#47;NetflixDashboard&#47;1_rss.png' 
        style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'>
    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
    <param name='embed_code_version' value='3' />
    <param name='site_root' value='' />
    <param name='name' value='NetflixDashboard_16701341279220&#47;NetflixDashboard' />
    <param name='tabs' value='no' /><param name='toolbar' value='yes' />
    <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ne&#47;NetflixDashboard_16701341279220&#47;NetflixDashboard&#47;1.png' />
    <param name='animate_transition' value='yes' />
    <param name='display_static_image' value='yes' />
    <param name='display_spinner' value='yes' />
    <param name='display_overlay' value='yes' />
    <param name='display_count' value='yes' />
    <param name='language' value='en-US' /></object>
</div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1670178911855');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if ( divElement.offsetWidth > 800 ) { 
        vizElement.style.width='1000px';
        vizElement.style.height='827px';
    } else if ( divElement.offsetWidth > 500 ) { 
        vizElement.style.width='1000px';
        vizElement.style.height='827px';
    } else { 
        vizElement.style.width='100%';
        vizElement.style.height='1377px';}
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
"""

html_Movies = """
<div class='tableauPlaceholder' id='viz1670180064325' style='position: relative'><noscript><a href='#'><img alt='Netflix Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ne&#47;Netflix_Movies_16701349170730&#47;Netflix_Movies&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Netflix_Movies_16701349170730&#47;Netflix_Movies' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ne&#47;Netflix_Movies_16701349170730&#47;Netflix_Movies&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1670180064325');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='1527px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""

html_Shows = """
<div class='tableauPlaceholder' id='viz1670180110385' style='position: relative'><noscript><a href='#'><img alt='Netflix Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ne&#47;Netflix_Shows_16701291134380&#47;NetflixShows&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Netflix_Shows_16701291134380&#47;NetflixShows' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ne&#47;Netflix_Shows_16701291134380&#47;NetflixShows&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1670180110385');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='1527px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""

st.markdown("## 📈 Dashboards")

Overall_data = st.expander('You can click here to see the EDA on Overall Data 👉')
with Overall_data:
    st.title('Insights on the Overall Data')
    components.html(html_Overall, width=1130, height=800)
    
Movie_Data = st.expander('You can click here to see the EDA on Movies Data 👉')
with Movie_Data:
        st.header('Insights on Movies')
        components.html(html_Movies, width=1130, height=800)
Show_Data = st.expander('You can click here to see the EDA on Shows Data 👉')
with Show_Data:
    st.header('Insights on Shows')
    components.html(html_Shows, width=1130, height=800)


st.markdown("## 📋 Questions ⁉ ##")

question1 = st.expander('Which Age_certifications have more shows and movies ?')
with question1:
    options = st.selectbox('Select which type of content you want to know?',df['type'].unique())
    if options == 'SHOW':
        df_group = df_show.groupby('age_certification').size().reset_index(name='counts')
        df_filtered = df_group[df_group['age_certification'] != 'Not Available']
        fig = px.bar(
        df_filtered,
        x="age_certification",
        y="counts",
        color="age_certification",
        color_discrete_sequence=px.colors.sequential.PuBuGn,
        text="counts",)
        fig.update_layout(
        font = dict(size=20,family="Franklin Gothic"))
        st.plotly_chart(fig)
    elif options == 'MOVIE':
        df_group = df_movie.groupby('age_certification').size().reset_index(name='counts')
        df_filtered = df_group[df_group['age_certification'] != 'Not Available']
        fig = px.bar(
        df_filtered,
        x="age_certification",
        y="counts",
        color="age_certification",
        color_discrete_sequence=px.colors.sequential.PuBuGn,
        text="counts",)
        fig.update_layout(
        font = dict(size=20,family="Franklin Gothic"))
        st.plotly_chart(fig)

question2 = st.expander('Which Genres have more shows and movies ?')
with question2:
    options = st.selectbox('Select which type of content you want to know?',df['type'].unique(), key='question_genres')
    if options == 'SHOW':
        df_group = df_show.groupby('genres').size().reset_index(name='counts')
        df_filtered = df_group[df_group['genres'] != 'Not Available']
        fig = px.bar(
        df_filtered,
        x="genres",
        y="counts",
        color="genres",
        color_discrete_sequence=px.colors.sequential.PuBuGn,
        text="counts",)
        fig.update_layout(
        xaxis_title="Genres",
        yaxis_title="Count",
        font = dict(size=20,family="Franklin Gothic"))
        st.plotly_chart(fig)
    elif options == 'MOVIE':
        df_group = df_movie.groupby('genres').size().reset_index(name='counts')
        df_filtered = df_group[df_group['genres'] != 'Not Available']
        fig = px.bar(
        df_filtered,
        x="genres",
        y="counts",
        color="genres",
        color_discrete_sequence=px.colors.sequential.PuBuGn,
        text="counts",)
        fig.update_layout(
        xaxis_title="Genres",
        yaxis_title="Count",
        font = dict(size=20,family="Franklin Gothic"))
        st.plotly_chart(fig)

question3 = st.expander('What are top 10 countries that often contribute to the content in Netflix')
with question3:
    country_count = df['production_countries'].value_counts().head(10)
    fig = px.bar(y=country_count.values, 
             x=country_count.index, 
             color = country_count.index,
             color_discrete_sequence=px.colors.sequential.PuBuGn,
             text=country_count.values,
             title= 'Top 10 countries that often contribute to Netflix',
             template= 'plotly_dark')
    fig.update_layout(
        xaxis_title="Countries",
        yaxis_title="Count",
        font = dict(size=20,family="Franklin Gothic"))
    st.plotly_chart(fig)

question4 = st.expander('Which genre has the greater imdb score ?')
with question4:
    genres_imdb=df.groupby('genres')[['imdb_score']].mean().reset_index()
    fig=px.bar(x=genres_imdb["genres"],
          y=genres_imdb["imdb_score"],
          color=genres_imdb["genres"],
          color_discrete_sequence=px.colors.sequential.PuBuGn,
          text=genres_imdb["imdb_score"],
          title= 'Distribution IBMD Score by Geners',
          template= 'plotly_dark')
    fig.update_layout(xaxis_title="Genres",
                 yaxis_title="IMDB Score",
                 font=dict(size=15, family="Franklin Gothic"))
    st.plotly_chart(fig)