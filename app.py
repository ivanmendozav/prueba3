# Librerias
import streamlit as st
import plotly.express as px
from utils import import_data,fromKaggle
import pandas as pd
from scipy import stats

# Importar datos y presentar una muestra
st.title("Razas de Gatos")
st.header("Descripción de la Base de Datos")
st.write("Los siguientes datos pertenecen a gatos de tres diferentes razas(Ragdoll, Maine coon y Angora), junto con sus características. El estudio presentado en este documento pretende compararlos y explicar sus diferencias.")
#fromKaggle()
df = import_data()
st.dataframe(df)
print(df.columns)

# Barras de gatos por raza
st.subheader("Número de gatos por raza")
tbl = df['Raza'].value_counts()
print(tbl.index)
fig = px.bar(x=tbl.index, y=tbl.values, color=tbl.index)
st.plotly_chart(fig)

# Histograma de Edad
st.subheader("Edad de los gatos")
fig = px.histogram(df, x="Edad Meses")
st.plotly_chart(fig)

# Razas por pais
st.subheader("Razas por país")
st.markdown("**Tabla de Contigencia**")
tbl = pd.crosstab(df["Pais"], df["Raza"])
st.dataframe(tbl)
if st.toggle("Realizar prueba estadística",key="Chi"):
    st.markdown("**Prueba de Chi-Cuadrado:**")
    res = stats.chi2_contingency(tbl)
    st.write(f"Estadistico: {res.statistic:.3f}, Valor P: {res.pvalue}")

# Correlacion numerica lineal
st.subheader("Correlación entre Peso y Longitud de cuerpo")
fig = px.scatter(df, x="Peso", y="Longitud Cuerpo", color="Raza")
st.plotly_chart(fig)
if st.toggle("Realizar prueba estadística",key="Pearson"):
    st.markdown("**Prueba de Pearson:**")
    res = stats.pearsonr(df["Peso"],df["Longitud Cuerpo"])
    st.write(f"Estadistico: {res.statistic:.3f}, Valor P: {res.pvalue}")

# Agrupar por categorica
st.subheader("Horas de Sueño por Raza")
fig = px.box(df, x="Raza", y="Horas Sueño")
st.plotly_chart(fig)
if st.toggle("Realizar prueba estadística",key="Kruskal"):
    st.markdown("**Pruebas de Normalidad entre razas (no pasa):**")    
    S,pvalue = stats.shapiro(df[df["Raza"]=="Ragdoll"]["Horas Sueño"])
    st.write(f"P Valor de Shapiro raza Ragdoll: {pvalue}")
    S,pvalue = stats.shapiro(df[df["Raza"]=="Maine coon"]["Horas Sueño"])
    st.write(f"P Valor de Shapiro raza Maine coon: {pvalue}")
    S,pvalue = stats.shapiro(df[df["Raza"]=="Angora"]["Horas Sueño"])
    st.write(f"P Valor de Shapiro raza Angora: {pvalue}")
    fig = px.histogram(df, x="Horas Sueño", color="Raza")
    st.plotly_chart(fig)
    st.markdown("**Prueba de Kruskal-Wallis**")
    K,pvalue = stats.kruskal(df[df["Raza"]=="Ragdoll"]["Horas Sueño"],
                df[df["Raza"]=="Maine coon"]["Horas Sueño"],
                df[df["Raza"]=="Angora"]["Horas Sueño"])
    st.write(f"P Valor: {pvalue}")