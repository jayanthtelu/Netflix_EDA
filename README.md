# Netflix_EDA

* **About the project:** <br>
The title of our project is ‘Netflix Demographics’. <br>
The motivation behind choosing this project is the large amount of data that the 2 datasets namely credits, and titles has on various attributers which will help us to visualize and provide insights on the topic for the Netflix use. The titles dataset has over 5000 records with attributes such as character, role, name, person id, whereas the titles dataset has over 70000 records with attributes such as genres, release year, age certification, runtime, production countries. This project helps us to make inferences and provide answers to understand the distribution of the movies and tv shows based on release year, top 15 contributing countries on Netflix, total content added across all years up to 2019, etc. The project’s main goal is to visualize the large amount of data to assist the users in analyzing the data and answering their questions. The data will be displayed to user in different ways, which will also help the user in better decision making and helps to identify the patterns in the data. We have presented our visualizations with help of Map views, Bar graph and line graphs. The Map view will allow the users to see the geospatial data and thus making the data easier to understand. We’ve also used the bar graphs and line graphs to show the relationship between the two different attributes and added the filters to filter the data based on various categories within the visualizations.<br>

* **How we built our project ?**<br>
As part of the project, The two datasets are cleaned and transformed into various different datasets to meet our requirements. <br>
They are as follow:<br>
 >credits (treated the null values)<br>
 >titles (treated the null values)<br>
 >show_titles (titles are divided into type = show)<br>
 >movie_titles (titles are divided into type = movie and removed seasosn column from the dataset)<br>
 >movie_tc (movie_title and credits are merged using ids)<br>
 >show_tc (show_title and credits are merged using ids) <br>
 >popuar_movie (Removed the null imdb_id's and replvisualizationsaced the other null values with their mean) <br>
 >popular_show (Removed the null imdb_id's and replaced the other null values with their mean) <br>
We've used these datasets and built some interactive dashboards in Tableau and integrated those into the streamlit.<br>
We also dicussed few questions and tried to answer using that are designed using a package callled Plotly.<br>
* **Tools and Packages:**<br>
   >Tableau<br>
   >Python<br>
   >Packages:<br>
    >>streamlit<br>
    >>pandas<br>
    >>numpy<br>
    >>plotly.express<br>
    >>Pillow<br>
* **Links and Ref:**<br>
   Check out this for all the dashboards that are created for this project : https://public.tableau.com/app/profile/jayanth.telu<br><br>

**URL: https://rb.gy/cdhqtl**<br>
