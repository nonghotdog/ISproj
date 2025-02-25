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