import streamlit as st

if 'smart_budget' not in st.session_state:
    st.session_state.smart_budget = []

def add_item():
    col1, col2, col3 = st.columns(3)
    with col1:
        item_name = st.text_input("Enter the name of the item:")
    with col2:
        item_price = st.number_input("Enter the price of the item:", min_value=0.0, step=0.01)
    with col3:
        item_category = st.text_input("Enter the category of the item:")
    
    if st.button("Add Item"):
        if item_name and item_category:
            item = {"id": len(st.session_state.smart_budget) + 1, "name": item_name, "price": item_price, "category": item_category}
            st.session_state.smart_budget.append(item)
            st.success(f"{item_name} added successfully!")
        else:
            st.error("Please fill in all fields.")
    

def view_items():
    if not st.session_state.smart_budget:
        st.warning("No items in the budget.")
        return
    for item in st.session_state.smart_budget:
        st.write(f"Name: {item['name']}, Price: ${item['price']}, Category: {item['category']}")

def total_spent():
    total = sum(item["price"] for item in st.session_state.smart_budget)
    st.write(f"Total Spent: ${total}")

def view_specific_category():
    category = st.text_input("Enter the category you want to view:")
    if st.button("Search"):
        found = False
        for item in st.session_state.smart_budget:
            if item["category"].lower() == category.lower():
                st.write(f"Name: {item['name']}, Price: ${item['price']}, Category: {item['category']}")
                found = True
        if not found:
            st.error(f"No items found in category: {category}")
def delete_item():
    item_name = st.text_input("Enter the name of the item to delete:")
    if st.button("Delete Item"):
        for item in st.session_state.smart_budget:
            if item["name"] == item_name:
                st.session_state.smart_budget.remove(item)
                st.success(f"Item '{item_name}' deleted successfully!")
                return
        st.error(f"No item found with name: {item_name}") 

st.title("Smart Budget Tracker")

menu = st.sidebar.selectbox("Menu", ["Add Item", "View Items", "Total Spent", "View Specific Category", "Delete Item"])

if menu == "Add Item":
    add_item()
elif menu == "View Items":
    view_items()
elif menu == "Total Spent":
    total_spent()
elif menu == "View Specific Category":
    view_specific_category()
elif menu == "Delete Item":
    delete_item()

