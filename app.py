import streamlit as st
from db import create_table, get_inventory, add_product, update_quantity
from alerts import check_and_alert
from forecast import forecast_demand

st.set_page_config(page_title="Smart AI Inventory", layout="wide")

create_table()
st.title("📦 Smart AI Inventory System")

menu = ["View Inventory", "Add Product", "Update Quantity", "Alerts", "Forecast Demand"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "View Inventory":
    data = get_inventory()
    st.subheader("Current Inventory")
    st.table(data)

elif choice == "Add Product":
    st.subheader("Add New Product")
    name = st.text_input("Product Name")
    qty = st.number_input("Quantity", min_value=0)
    threshold = st.number_input("Alert Threshold", min_value=0)
    if st.button("Add"):
        add_product(name, qty, threshold)
        st.success("✅ Product added.")

elif choice == "Update Quantity":
    st.subheader("Update Product Quantity")
    id_ = st.number_input("Product ID", min_value=1)
    qty = st.number_input("New Quantity", min_value=0)
    if st.button("Update"):
        update_quantity(id_, qty)
        st.success("✅ Quantity updated.")

elif choice == "Alerts":
    st.subheader("Inventory Alerts")
    check_and_alert()
    st.info("📧 Email alert sent for low-stock products.")

elif choice == "Forecast Demand":
    st.subheader("Demand Forecast")
    prod = st.text_input("Enter Product Name")
    if st.button("Forecast"):
        try:
            pred = forecast_demand(product_name=prod)
            st.write(f"📈 Predicted next demand for {prod}: **{pred}** units")
        except:
            st.warning("⚠️ Insufficient data or product not found.")
