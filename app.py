import streamlit as st
import pandas as pd
import plotly.express as px
import pickle

# Set page configuration
st.set_page_config(
    page_title="Customer Segmentation and Recommendation System",
    layout="wide"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Style for the main heading */
    .main-heading {
        font-size: 48px;
        font-weight: bold;
        color: #FF7F50;
        text-align: center;
        margin-bottom: 10px;
    }

    /* Style for the subheading */
    .subheading {
        font-size: 20px;
        color: #555;
        text-align: center;
        margin-bottom: 40px;
    }

    /* Style for metrics */
    [data-testid="metric-container"] {
        background-color: #f9f9f9;
        border: 2px solid #FF7F50;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }

    [data-testid="metric-container"] .metric-label {
        font-size: 18px;
        color: #FF6347;
    }

    [data-testid="metric-container"] .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load your dataset
@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\hp\Downloads\Online-Retail.csv")

df = load_data()

# Main heading and subheading
st.markdown('<div class="main-heading">Customer Clustering ✨</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subheading">Discover valuable insights into customer behavior using our clustering algorithm!</div>',
    unsafe_allow_html=True,
)

# Tabs for sections
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Cluster Insights", "3D Visualization", "Random Sample Data","Recommendations"])

# --- TAB 1: Overview ---
with tab1:
    st.subheader("Overview of Dataset and Metrics")
    # Calculate key metrics
    num_products = df['Description'].nunique()
    num_customers = df['CustomerID'].nunique()
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    average_money_spent = df['TotalPrice'].mean()
    top_country = df['Country'].value_counts().idxmax()

    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Number of Products", num_products)
    col2.metric("Number of Customers", num_customers)
    col3.metric("Average Money Spent", f"${average_money_spent:,.2f}")
    col4.metric("Top Country", top_country)


    # Add Tech Stack description
    st.markdown("---")
    st.markdown("### Tech Stack Used")
    st.markdown(
        """
        **Programming Language**  
        - **Python**

        **Libraries and Tools**  
        - **Data Analysis and Processing**  
          - Pandas, NumPy, Scikit-learn, SciPy  
        - **Visualization**  
          - Matplotlib, Seaborn  

        **Application Framework**  
        - Streamlit: For creating the web application interface and making the project interactive.  

        **Dataset**  
        - **Transactional dataset from the UCI Machine Learning Repository**: Original data source used for segmentation.  

        **Deployment**  
        - **AWS**: To host and deploy the Streamlit application (assuming deployment is planned).
        """
    )



# --- TAB 2: Cluster Insights ---
with tab2:
    st.subheader("Detailed Cluster Profiles")

    clusters = [1, 2, 3]  # Replace with actual cluster numbers
    cluster_profiles = {
    1: {
        "title": "🎯 Profile: Sporadic Shoppers with a Preference for Weekend Shopping",
        "description": """- Customers in this cluster tend to spend less, with a lower number of transactions and products purchased.
- Slight tendency to shop during the weekends (very high Day_of_Week value).
- Spending trend is relatively stable but on the lower side, with low monthly spending variation (low Monthly_Spending_Std).
- Low cancellation frequency and rate.
- Average transaction value is on the lower side, indicating smaller purchases per transaction."""
    },
    2: {
        "title": "🎯 Profile: Infrequent Big Spenders with a High Spending Trend",
        "description": """- Moderate spending level but infrequent transactions (high Days_Since_Last_Purchase and Average_Days_Between_Purchases).
- High spending trend, indicating increasing spending over time.
- Prefer shopping late in the day (high Hour value), mainly residing in the UK.
- Moderate number of transaction cancellations.
- Relatively high average transaction value, indicating substantial purchases."""
    },
    3: {
        "title": "🎯 Profile: Frequent High-Spenders with a High Rate of Cancellations",
        "description": """- High total spending, purchasing a wide variety of unique products.
- Frequent transactions but high cancellation frequency and rate.
- Low average time between purchases, shopping early in the day (low Hour value).
- Monthly spending shows high variability, making spending patterns less predictable.
- Low spending trend, suggesting decreasing spending over time despite high spending levels."""
    }
}

    selected_cluster = st.selectbox("Select a Cluster to View Details:", clusters)

    if selected_cluster in cluster_profiles:
        profile = cluster_profiles[selected_cluster]
        st.markdown(f"#### {profile['title']}")
        st.markdown(profile["description"])
    else:
        st.write("No details available for the selected cluster.")


# --- TAB 3: 3D Visualization ---
with tab3:
    st.subheader("Cluster 3D Visualization")
    # Load the pickled Plotly figure
    try:
        with open(r"C:\Users\hp\Downloads\cluster_3d_plot.pkl", "rb") as file:
            loaded_fig = pickle.load(file)
        st.plotly_chart(loaded_fig, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading 3D visualization: {e}")


top_products = {
    0: [
        ("WORLD WAR 2 GLIDERS ASSTD DESIGNS", 5992),
        ("ASSORTED COLOUR BIRD ORNAMENT", 4739),
        ("ASSORTED COLOURS SILK FAN", 4280),
        ("WHITE HANGING HEART T-LIGHT HOLDER", 4125),
        ("JUMBO BAG RED RETROSPOT", 3133),
        ("VICTORIAN GLASS HANGING T-LIGHT", 3120),
        ("POPART WOODEN PENCILS ASST", 3100),
        ("AGED GLASS SILVER T-LIGHT HOLDER", 3035),
        ("MINI PAINT SET VINTAGE", 2916),
        ("PACK OF 72 RETROSPOT CAKE CASES", 2867),
    ],
    1: [
        ("PACK OF 12 LONDON TISSUES", 15356),
        ("WORLD WAR 2 GLIDERS ASSTD DESIGNS", 13264),
        ("JUMBO BAG RED RETROSPOT", 11319),
        ("ASSORTED COLOUR BIRD ORNAMENT", 9821),
        ("SMALL CHINESE STYLE SCISSOR", 9234),
        ("VICTORIAN GLASS HANGING T-LIGHT", 8135),
        ("WHITE HANGING HEART T-LIGHT HOLDER", 8037),
        ("PACK OF 72 RETROSPOT CAKE CASES", 7685),
        ("GIRLS ALPHABET IRON ON PATCHES", 6720),
        ("COLOUR GLASS T-LIGHT HOLDER HANGING", 6539),
    ],
    2: [
        ("ESSENTIAL BALM 3.5G TIN IN ENVELOPE", 5676),
        ("ASSORTED COLOUR BIRD ORNAMENT", 5598),
        ("BROCADE RING PURSE", 5037),
        ("WHITE HANGING HEART T-LIGHT HOLDER", 4616),
        ("WORLD WAR 2 GLIDERS ASSTD DESIGNS", 4335),
        ("PACK OF 72 RETROSPOT CAKE CASES", 3663),
        ("SMALL CHINESE STYLE SCISSOR", 3643),
        ("JUMBO BAG RED RETROSPOT", 3548),
        ("ASSORTED COLOURS SILK FAN", 2760),
        ("MINI PAINT SET VINTAGE", 2556),
    ],
}
 
 
with tab4: 
    # Path to your pickled file
    file_path = r"C:\Users\hp\Downloads\random_customer_recommendations.pkl"

    # Try loading the pickled data
    try:
        with open(file_path, "rb") as file:
            # Load the pickled data
            data = pickle.load(file)
        
        # Check if the loaded data is a DataFrame
        if isinstance(data, pd.DataFrame):
            #st.success("Data loaded successfully!")
            st.write("Sample Data:")
            st.dataframe(data.head(10))  # Display first 10 rows of the DataFrame
        else:
            st.warning("The loaded data is not a DataFrame. Please check the file format.")
    except Exception as e:
        st.error(f"Error loading data: {e}")


# Initialize a default value for `cluster`
cluster = None  # Cluster will be defined after form submission

# Sidebar for customer recommendation system
st.sidebar.header("Customer Recommendation System 🛍️")
st.sidebar.write("Fill in your details to find your cluster and get recommendations:")

# Define questions and their numeric ranges
questions = {
    "Days Since Last Purchase": (0, 60),
    "Total Transactions": (0, 50),
    "Total Products Purchased": (0, 100),
    "Total Spend": (0, 1000),
    "Average Transaction Value": (0, 200),
    "Unique Products Purchased": (0, 50),
    "Average Days Between Purchases": (0, 30),
    "Cancellation Frequency": (0, 10),
    "Monthly Spending Mean": (0, 1000),
}

# Define thresholds for scoring (Low, Moderate, High)
thresholds = {
    "Days Since Last Purchase": [20, 40],
    "Total Transactions": [15, 30],
    "Total Products Purchased": [30, 70],
    "Total Spend": [300, 700],
    "Average Transaction Value": [50, 150],
    "Unique Products Purchased": [10, 30],
    "Average Days Between Purchases": [10, 20],
    "Cancellation Frequency": [3, 6],
    "Monthly Spending Mean": [300, 700],
}

# Collect user inputs for each question
scores = []
with st.sidebar.form(key="customer_form"):
    for question, value_range in questions.items():
        # Display a slider for the question
        response = st.slider(
            question,
            min_value=value_range[0],
            max_value=value_range[1],
            step=1,
        )
        
        # Determine the score based on thresholds
        low, moderate = thresholds[question]
        if response <= low:
            scores.append(0)  # Low
        elif response <= moderate:
            scores.append(1)  # Moderate
        else:
            scores.append(2)  # High

    # Submit button for form
    submitted = st.form_submit_button("Submit")

if submitted:
    # Calculate the total score
    total_score = sum(scores)

    # Determine the cluster based on total score
    if total_score <= 6:
        cluster = 1  # Low engagement
    elif 7 <= total_score <= 13:
        cluster = 2  # Moderate engagement
    else:
        cluster = 3  # High engagement

    # Display the cluster result
    st.sidebar.write(f"### Based on your input:")
    st.sidebar.write(f"- **You belong to Cluster:** 🎯 Cluster {cluster}")

# Recommendations tab (tab5)
with tab5:
    if cluster is not None:  # Ensure cluster is defined before rendering recommendations
        with st.expander(f"🎯 Recommendations for Cluster {cluster}", expanded=True):
            st.write(f"### Top 10 Recommended Products for Cluster {cluster}:")
            for product, quantity in top_products[cluster]:
                st.write(f"- 🌟 **{product}** (Sold: {quantity} units)")
    else:
        st.warning("Please fill out the form in the sidebar to determine your cluster and get recommendations.")
