**Customer Segmentation and Recommendation System**

📚** Overview**
This project focuses on customer segmentation and a recommendation system using unsupervised machine learning techniques. It transforms transactional data into actionable insights, enabling better marketing strategies and personalized product recommendations.

The system identifies customer clusters based on purchasing behaviors and provides recommendations tailored to each cluster. It is built using Python and displayed through an interactive Streamlit app for easy access and user interaction.

**🚀 Features**
1. Customer Segmentation
Segments customers based on purchasing patterns using clustering techniques like K-Means.
Visualizes clusters and their key characteristics.
2. Recommendation System
Allows users to input purchase behavior details through an interactive form.
Determines the user's cluster dynamically and recommends top products.
🛠️ Technologies Used
Python: Data processing and machine learning.
Streamlit: Building an interactive web app.
Pandas, Numpy: Data manipulation.
Matplotlib, Seaborn: Data visualization.
Scikit-learn: Unsupervised machine learning (e.g., K-Means clustering, PCA).
⚙️ Installation
Clone the repository:

git clone https://github.com/your-username/customer-segmentation-recommendation-system.git  
Navigate to the project directory:

cd customer-segmentation-recommendation-system  
Create and activate a virtual environment:

python -m venv streamlit-env  
source streamlit-env/bin/activate  # On Windows: streamlit-env\Scripts\activate 

Install dependencies:

pip install -r requirements.txt  
Run the Streamlit app:

streamlit run app.py  
🖥️ How to Use
Cluster Insights (Middle Panel)

Explore customer clusters and their visualizations.
Analyze cluster-specific information and top product recommendations.
Recommendation System (Sidebar)

Fill in details like days since last purchase, total spend, etc.
View your assigned cluster and receive personalized product recommendations.

📊 Data Overview
The dataset contains transactional records of a UK-based retailer from 2010 to 2011. Key steps in the data pipeline include:

Data Cleaning: Removing duplicates, handling outliers, and correcting anomalies.
Feature Engineering: Creating features such as RFM metrics, cancellation rates, and seasonality trends.
Clustering: Using K-Means to group customers based on purchasing behaviors.

📂 Project Structure
customer-segmentation-recommendation-system/  
├── data/                  # Dataset and processed files  
├── app.py                 # Main Streamlit app file  
├── clustering.py          # Scripts for clustering logic  
├── recommendation.py      # Scripts for recommendation system  
├── requirements.txt       # Project dependencies  
└── README.md              # Project documentation  


📈 Results

Customers are segmented into low, moderate, and high engagement clusters.
Tailored product recommendations boost potential sales and improve marketing strategies.
📝 Future Enhancements
Add more user-friendly visualizations for cluster comparison.
Integrate additional clustering algorithms for evaluation.
Support real-time transactional data updates.
🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

📧 Contact
For any queries or feedback, reach out via:

Email: mjaunjal06@gmail.com
GitHub: [MonikaJaunjal](https://github.com/MonikaJaunjal/)
