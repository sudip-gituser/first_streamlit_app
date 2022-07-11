import streamlit
streamlit.title('Writing my first Streamlit code in GitHub')
streamlit.title('I find this training very interesting and am really enjoying this')

streamlit.header('Here is the breakfast menu that I had today')
streamlit.text('🥣 Omega 3 & bueberry oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
