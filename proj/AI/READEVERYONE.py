import streamlit
import numpy
import pandas
import matplotlib.pyplot

streamlit.title("**I**ntelligent **S**ystem Project")

# magic command using ifelse condition (define type value)
# st.write
streamlit.header("> st.write")
streamlit.text("st.write(*args, unsafe_allow_html=False, **kwargs)\nEX.")

streamlit.header(":blue[Text]", divider="gray")
streamlit.write('''
            # st.title
            ## st.header
            ### st.subheader
            **bold**
                
            *italic*
            >blackQuate
            1. A
            2. B
            - C
            - D
            
                
            $$\sum_{i}x$$
            

            &mdash;\

                
            :+1:
                
            :material/icon:

            `code`

            :red[c]:orange[o]:green[l]:blue[o]:violet[r]
            
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:
                
            [Google](http://www.google.com)
            
            |Name|Age|
            |----------|----------|
            |Bam|20|
            
            ```
            {
                "Name" : "Bam",
                "Age" : 20
            }
            ```
            :blue[color]:blue-background[background]

                ''')
streamlit.caption("capti:blue[on]:sunglasses:")
streamlit.code(
    '''def code():
    print("code format")'''
, language="python")
streamlit.slider("slider", 0, 100, (25, 75))

# streamlit.echo()
def get_user_name():
    return 'Bam'
with streamlit.echo():

    def get_punctuation():
        return '!!!'
    
    greeting = "Hi there, "
    name = get_user_name()
    punctuation = get_punctuation()

    streamlit.write(greeting, name, punctuation)
cantSee = 'this one'

streamlit.latex(r'''
    [\Lambda\Alpha\Tau\Epsilon\Chi] \Longrightarrow
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

streamlit.code("st.help(pandas.DataFrame) #help")
streamlit.code("pandas.read_csv #help")
streamlit.code("st #help")
class Dog:
  '''A typical dog. #quickly inspect an object'''
  def __init__(self, breed, color):
    self.breed = breed
    self.color = color
  def bark(self):
    return 'Woof!'
fido = Dog("poodle", "white")
streamlit.help(fido)

streamlit.html("<p><span style='text-decoration: line-through red;'>HTML</span>!</p>")
streamlit.divider()

streamlit.header(":blue[Data]")
# styler && dataframe
streamlit.dataframe(
    pandas.DataFrame(
       numpy.random.randn(3, 5),
       columns = ("col %d" % i for i in range(5))
    ).style.highlight_max(axis=0)
)

# config dataframe via column_config, hide_index, or column_orde
import random
streamlit.dataframe(
    pandas.DataFrame({
        'nationality': ["Thai", "Korean[S]", "Korean[N]"],
        'url': ["https://en.wikipedia.org/wiki/Thailand", "https://en.wikipedia.org/wiki/Korea", "https://en.wikipedia.org/wiki/Korea" ],
        'stars': [random.randint(0, 1000) for _ in range(3)],
        'views_history': [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }),
    column_config={
      "name": "Visuli.", ###
        "stars": streamlit.column_config.NumberColumn( ##
            "Github Stars", #
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": streamlit.column_config.LinkColumn("URL"),
        "views_history": streamlit.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)

# normalization for visualization
from datetime import date
streamlit.dataframe(
   pandas.DataFrame({
      "Date": [date(2024, 1, 1), date(2024, 2, 1), date(2024, 3, 1)],
      "Total": [13429, 23564, 23452],
   }).set_index("Date"),
   column_config={
      "_index": streamlit.column_config.DateColumn("Month", format="MMM YYYY"),
      "Total": streamlit.column_config.NumberColumn("Total ($)"),
   }
)

streamlit.data_editor([
    {"command": "streamlit.selectbox", "priority": 0, "is_widget": True},
    {"command": "emoji.selectbox", "priority": 0, "is_widget": False},
    {"command": "streamlit.selectbox", "priority": 0, "is_widget": True},
    ]
)