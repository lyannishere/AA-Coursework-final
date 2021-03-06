import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier


st.write("""
# Hello, Pick Your Parameters
This app predicts the **Iris flower** type!
""")

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVCIopZDdSOTDSrVDOE0umr8o772qA_rlfqh84UG2-7_Xe6-OkWh6dTemk8jS9SLYDhw&usqp=CAU")
st.sidebar.header('Use the sidebar to predict your input parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Input parameters')
st.write(df)

iris = pd.read_csv('https://raw.githubusercontent.com/lyannishere/AA-Coursework-final/main/IRIS.csv')
X = iris.drop('species',axis=1)
Y = iris.species

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
# st.write(['Iris-setosa','Iris-versicolor','Iris-virginica'])
st.write(pd.Series(['setosa','versicolor','virginica']))

st.image("data:image/jpeg;base64,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")


st.subheader('Prediction')
#st.write(iris.target_names[prediction])
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
