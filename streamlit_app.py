import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load model
kmeans = joblib.load('kmeans_model.pkl')

# Title
st.title("🏬 Mall Customer Segmentation App")

st.write("Predict which type of customer you are based on your spending habits!")

# --- Sidebar Inputs ---
st.sidebar.header('Enter Customer Details')

annual_income = st.sidebar.number_input('Annual Income (k$)', min_value=0, max_value=200, value=50)
spending_score = st.sidebar.number_input('Spending Score (1-100)', min_value=0, max_value=100, value=50)

# Predict button
if st.sidebar.button('Predict Customer Cluster'):
    input_data = np.array([[annual_income, spending_score]])
    cluster = kmeans.predict(input_data)[0]

    # Feature 1: Show Cluster Details
    st.subheader("🧠 Prediction Result")
    st.success(f"The customer belongs to Cluster: {cluster}")

    # Explain cluster meaning
    st.subheader("📊 Cluster Meaning")
    if cluster == 0:
        st.info("🛒 Cluster 0: Low income, low spending — Budget Shoppers.")
    elif cluster == 1:
        st.info("💳 Cluster 1: High income, high spending — VIP Customers!")
    elif cluster == 2:
        st.info("🎯 Cluster 2: Average income, average spending — Regular Customers.")
    elif cluster == 3:
        st.info("🛍️ Cluster 3: High income, low spending — Potential Luxury Customers.")
    else:
        st.info("📉 Cluster 4: Low income, high spending — Impulsive Shoppers.")

    # Feature 2: Display Cluster Visualization
    st.subheader("📈 Cluster Visualization")

    # Let's create some dummy data for visualization purpose
    # (In real app you should load original training data!)
    np.random.seed(42)
    dummy_income = np.random.randint(10, 100, 200)
    dummy_score = np.random.randint(1, 100, 200)
    dummy_data = np.array(list(zip(dummy_income, dummy_score)))
    dummy_labels = kmeans.predict(dummy_data)

    plt.figure(figsize=(8,6))
    plt.scatter(dummy_data[:,0], dummy_data[:,1], c=dummy_labels, cmap='viridis', s=50, alpha=0.6)
    plt.scatter(input_data[:,0], input_data[:,1], c='red', marker='X', s=200, label='You')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.title('Customer Segments')
    plt.legend()
    st.pyplot(plt)

    # Feature 4: Recommended Actions Based on Cluster
    st.subheader("📋 Recommended Business Actions")

    if cluster == 0:
        st.warning("💡 Offer budget-friendly promotions or loyalty rewards to retain them.")
    elif cluster == 1:
        st.success("💎 Provide premium services, personalized offers, and exclusive memberships.")
    elif cluster == 2:
        st.info("🎟️ Encourage more spending via discounts, limited-time deals, or events.")
    elif cluster == 3:
        st.warning("🧐 Analyze why high-income customers are spending less. Offer luxury upsells.")
    else:
        st.warning("🛍️ Educate on smart spending, offer value bundles, and promotions.")

# Add small footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit.")
