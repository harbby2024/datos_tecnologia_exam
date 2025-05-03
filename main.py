import streamlit as st
import pandas as pd
import numpy as np

# Título de la aplicación
st.title("Análisis Básico de Ventas")

# Cargar el dataset
# TODO: Carga el archivo 'sales_data.csv'
data= np.random.seed(42)
dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
products = ["Laptop", "Phone", "Tablet", "Headphones"]
categories = ["Electronics", "Accessories"]
data = {
    "Date": np.random.choice(dates, 50),
    "Product": np.random.choice(products, 50),
    "Category": np.random.choice(categories, 50),
    "Price": np.random.uniform(50, 500, 50).round(2),
    "Quantity": np.random.randint(1, 5, 50)
}
df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]
df.to_csv("sales_data.csv", index=False)

# Mostrar dataset completo
st.subheader("Datos Completos")
# TODO: Muestra el DataFrame
st.dataframe(data)

# Filtros en la barra lateral
st.sidebar.header("Filtros")
# TODO: Crea un selectbox para elegir una categoría
categorias = category=df['Category'].unique()
categorias = st.sidebar.selectbox("Selecciona una categoría", category)

# TODO: Crea un slider para el rango de precios
min_price = float(data['Price'].min())
max_price = float(data['Price'].max())
price_range = st.sidebar.slider("Rango de precio", min_price, max_price, (min_price, max_price))

# Aplicar filtros
# TODO: Filtra el DataFrame por categoría y rango de precios
filtered_df = df[
    (df['Category'] == categorias) &
    (df['Price'] >= price_range[0]) &
    (df['Price'] <= price_range[1])
]
# Mostrar datos filtrados
st.subheader("Datos Filtrados")
# TODO: Muestra el DataFrame filtrado y el número de registros
st.dataframe(filtered_df)
st.write(f"Total de registros: {len(filtered_df)}")

# Estadísticas
st.subheader("Estadísticas")

if not filtered_df.empty:
    total_sales=filtered_df["Price"].sum()
    avg_price=filtered_df["Price"].mean()
    st.metric("Total de Ventas", value=f"${total_sales:,.2f}")
    st.metric("Precio Promedio", value=f"${avg_price:,.2f}")
else:
    st.write("No hay datos")




