"""
Dry Bean Type Classification - Streamlit App
This is a machine learning deployment application for classifying bean types
based on physical characteristics using a trained Random Forest model.
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Ellipse
import io

# Set page configuration
st.set_page_config(
    page_title="Bean Type Classifier",
    page_icon="🫘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .prediction-box {
        background-color: #d4edda;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #28a745;
        margin: 20px 0;
    }
    .error-box {
        background-color: #f8d7da;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #f5c6cb;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Function to generate bean images (MUST BE DEFINED FIRST)
def generate_bean_image(bean_type):
    """Generate a visual representation of a bean"""
    fig, ax = plt.subplots(figsize=(3, 3), facecolor='white')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    
    bean_shapes = {
        'Seker': {'width': 3, 'height': 3.2, 'color': '#FFE4B5', 'rotation': 0},
        'Barbunya': {'width': 3.5, 'height': 3, 'color': '#FF69B4', 'rotation': 0},
        'Bombay': {'width': 3, 'height': 3.8, 'color': '#2F4F4F', 'rotation': 15},
        'Cali': {'width': 4, 'height': 2.8, 'color': '#D2691E', 'rotation': 20},
        'Dermosan': {'width': 3.5, 'height': 3.2, 'color': '#FF8C00', 'rotation': 10},
        'Horoz': {'width': 4.5, 'height': 2.5, 'color': '#F5DEB3', 'rotation': 25},
        'Sira': {'width': 2.8, 'height': 3, 'color': '#8B4513', 'rotation': 5}
    }
    
    bean = bean_shapes.get(bean_type, bean_shapes['Seker'])
    ellipse = Ellipse((5, 5), bean['width'], bean['height'], 
                      angle=bean['rotation'], 
                      facecolor=bean['color'],
                      edgecolor='#333333', linewidth=2)
    ax.add_patch(ellipse)
    
    # Add highlight for 3D effect
    highlight = Ellipse((4.5, 5.5), bean['width']*0.4, bean['height']*0.3,
                        angle=bean['rotation'],
                        facecolor='white', alpha=0.4)
    ax.add_patch(highlight)
    
    # Add shadow
    shadow = Ellipse((5.1, 4.7), bean['width']*0.9, bean['height']*0.1,
                     angle=bean['rotation'],
                     facecolor='gray', alpha=0.2)
    ax.add_patch(shadow)
    
    return fig

# App title and description
st.title("🫘 Dry Bean Type Classification")
st.markdown("---")

# Add a welcome banner with visual info
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("📊 Total Bean Varieties", "7")
with col2:
    st.metric("🎯 Model Accuracy", "95%+")
with col3:
    st.metric("📈 Training Samples", "13,611")

st.write("""
### 🤖 Automated Bean Classification System
This application uses machine learning to automatically classify dry beans into 
7 different varieties based on their physical characteristics. Simply enter the 
measurements of a bean, and the model will predict its type instantly!
""")

# Display all bean types in a gallery
st.subheader("🫘 All Bean Varieties at a Glance")
bean_types = ['Seker', 'Barbunya', 'Bombay', 'Cali', 'Dermosan', 'Horoz', 'Sira']
gallery_cols = st.columns(7)

for idx, (col, bean_type) in enumerate(zip(gallery_cols, bean_types)):
    with col:
        bean_fig = generate_bean_image(bean_type)
        st.pyplot(bean_fig, use_container_width=True)
        plt.close(bean_fig)
        st.caption(f"**{bean_type}**", unsafe_allow_html=True)

st.markdown("---")

# Display Bean Varieties Gallery in Sidebar
st.sidebar.markdown("## 🫘 Bean Varieties Gallery")
st.sidebar.markdown("---")

bean_info = {
    'Seker': {
        'emoji': '🔵',
        'shape': 'Small, Round',
        'color': 'Light',
        'size': 'Small',
        'characteristics': 'Very round, compact shape'
    },
    'Barbunya': {
        'emoji': '🔴',
        'shape': 'Medium, Round',
        'color': 'Pink/Red',
        'size': 'Medium',
        'characteristics': 'Pink reddish colored'
    },
    'Bombay': {
        'emoji': '⚫',
        'shape': 'Large, Oval',
        'color': 'Black',
        'size': 'Large',
        'characteristics': 'Black, darker appearance'
    },
    'Cali': {
        'emoji': '🟤',
        'shape': 'Medium, Kidney',
        'color': 'Light Brown',
        'size': 'Medium',
        'characteristics': 'Kidney-shaped, light colored'
    },
    'Dermosan': {
        'emoji': '🟠',
        'shape': 'Medium, Oval',
        'color': 'Orange-red',
        'size': 'Medium',
        'characteristics': 'Medium sized, reddish'
    },
    'Horoz': {
        'emoji': '⬜',
        'shape': 'Large, Elongated',
        'color': 'Light',
        'size': 'Large',
        'characteristics': 'Largest variety, elongated'
    },
    'Sira': {
        'emoji': '🟫',
        'shape': 'Small, Oval',
        'color': 'Dark Brown',
        'size': 'Small',
        'characteristics': 'Small, dark brown color'
    }
}

# Create tabs for bean information
bean_tabs = st.sidebar.tabs(bean_info.keys())
for tab, (bean_type, info) in zip(bean_tabs, bean_info.items()):
    with tab:
        # Display bean image
        bean_fig = generate_bean_image(bean_type)
        st.pyplot(bean_fig, use_container_width=True)
        plt.close(bean_fig)
        
        st.write(f"### {info['emoji']} {bean_type}")
        st.write(f"**Shape:** {info['shape']}")
        st.write(f"**Color:** {info['color']}")
        st.write(f"**Size:** {info['size']}")
        st.write(f"**Characteristics:** {info['characteristics']}")

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip:** Select bean characteristics below and click 'Classify Bean' to get predictions!")

# Load models and scaler
@st.cache_resource
def load_models():
    try:
        model = joblib.load('best_rf_model.pkl')
        scaler = joblib.load('scaler.pkl')
        label_encoder = joblib.load('label_encoder.pkl')
        return model, scaler, label_encoder
    except FileNotFoundError:
        st.error("❌ Model files not found! Please ensure the following files are in the same directory:")
        st.error("- best_rf_model.pkl")
        st.error("- scaler.pkl")
        st.error("- label_encoder.pkl")
        st.stop()

# Load feature names
@st.cache_resource
def load_feature_columns():
    try:
        with open('feature_columns.txt', 'r') as f:
            features = [line.strip() for line in f.readlines()]
        return features
    except FileNotFoundError:
        return [
            'Area', 'Perimeter', 'MajorAxisLength', 'MinorAxisLength',
            'AspectRatio', 'Eccentricity', 'ConvexArea', 'EquivalentDiameter',
            'Extent', 'Solidity', 'Roundness', 'Compactness',
            'ShapeFactor1', 'ShapeFactor2', 'ShapeFactor3', 'ShapeFactor4'
        ]

# Load all resources
model, scaler, label_encoder = load_models()
feature_columns = load_feature_columns()

# Bean type descriptions
bean_descriptions = {
    'Seker': '🫘 Seker beans - Small, round shape',
    'Barbunya': '🫘 Barbunya beans - Pink/reddish colored',
    'Bombay': '🫘 Bombay beans - Black colored, large',
    'Cali': '🫘 Cali beans - Light colored, kidney-shaped',
    'Dermosan': '🫘 Dermosan beans - Medium sized',
    'Horoz': '🫘 Horoz beans - Large, elongated',
    'Sira': '🫘 Sira beans - Small, dark colored'
}

# Create two columns for layout
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📊 Enter Bean Measurements")
    st.write("Input the physical characteristics of the bean:")
    
    # Add a visual guide for features
    with st.expander("📖 Feature Guide - What do these measurements mean?"):
        feature_guide = pd.DataFrame({
            'Feature': ['Area', 'Perimeter', 'MajorAxisLength', 'MinorAxisLength', 'AspectRatio', 
                       'Eccentricity', 'Roundness', 'Compactness', 'Solidity'],
            'Description': [
                'Total pixels inside bean boundary',
                'Length of bean border/circumference',
                'Length of longest line through bean',
                'Length perpendicular to major axis',
                'Ratio between major and minor axis',
                'How elliptical the bean is (0=circle)',
                'Measure of bean roundness (1=perfect)',
                'Ratio of diameter to major axis',
                'Ratio of bean to convex hull (1=solid)'
            ]
        })
        st.dataframe(feature_guide, use_container_width=True, hide_index=True)
    
    # Create input fields
    input_data = {}
    
    # Create 4 columns of inputs
    input_cols = st.columns(2)
    
    feature_ranges = {
        'Area': (10000, 90000),
        'Perimeter': (300, 850),
        'MajorAxisLength': (200, 450),
        'MinorAxisLength': (75, 290),
        'AspectRatio': (0.7, 4.5),
        'Eccentricity': (0.1, 0.94),
        'ConvexArea': (11000, 92000),
        'EquivalentDiameter': (115, 340),
        'Extent': (0.5, 1.0),
        'Solidity': (0.9, 1.0),
        'Roundness': (0.5, 1.0),
        'Compactness': (0.5, 0.95),
        'ShapeFactor1': (0.2, 0.8),
        'ShapeFactor2': (0.2, 0.8),
        'ShapeFactor3': (0.2, 0.95),
        'ShapeFactor4': (0.1, 0.9)
    }
    
    for i, feature in enumerate(feature_columns):
        col_idx = i % 2
        min_val, max_val = feature_ranges.get(feature, (0, 100))
        # Convert to float for consistency
        min_val = float(min_val)
        max_val = float(max_val)
        default_val = (min_val + max_val) / 2
        step_val = (max_val - min_val) / 50
        
        with input_cols[col_idx]:
            input_data[feature] = st.number_input(
                label=feature,
                min_value=min_val,
                max_value=max_val,
                value=default_val,
                step=step_val,
                help=f"Range: {min_val:.1f} - {max_val:.1f}"
            )

with col2:
    st.subheader("🤖 Prediction Results")
    st.write("Click the button below to classify the bean:")
    
    if st.button("🚀 Classify Bean", use_container_width=True, type="primary"):
        try:
            # Prepare data for prediction
            input_df = pd.DataFrame([input_data])
            input_scaled = scaler.transform(input_df)
            
            # Make prediction
            prediction_encoded = model.predict(input_scaled)[0]
            confidence = model.predict_proba(input_scaled)[0].max()
            prediction_proba = model.predict_proba(input_scaled)[0]
            
            # Decode prediction
            predicted_class = label_encoder.inverse_transform([prediction_encoded])[0]
            
            # Display results
            st.markdown(f"""
            <div class="prediction-box">
                <h2 style="color: #28a745; margin: 0;">✅ Predicted Bean Type</h2>
                <h1 style="color: #1a4d2e; margin: 10px 0;">{predicted_class}</h1>
                <p><strong>Description:</strong> {bean_descriptions.get(predicted_class, 'Unknown bean type')}</p>
                <p><strong>Confidence Score:</strong> <span style="font-size: 1.3em; color: #28a745;"><strong>{confidence*100:.2f}%</strong></span></p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display bean image
            col_img, col_info = st.columns([1, 1])
            with col_img:
                st.markdown("### 🎨 Visual Bean Representation")
                bean_fig = generate_bean_image(predicted_class)
                st.pyplot(bean_fig, use_container_width=True)
                plt.close(bean_fig)
            
            with col_info:
                st.markdown("### 📋 Prediction Details")
                st.success(f"**Predicted Type:** {predicted_class}")
                st.info(f"**Confidence:** {confidence*100:.2f}%")
                st.write(f"**Description:** {bean_descriptions.get(predicted_class, 'N/A')}")
            
            # Show confidence for all classes
            st.subheader("📈 Prediction Probabilities")
            
            prob_df = pd.DataFrame({
                'Bean Type': label_encoder.classes_,
                'Probability': prediction_proba,
                'Percentage': prediction_proba * 100
            }).sort_values('Probability', ascending=False)
            
            st.bar_chart(prob_df.set_index('Bean Type')['Percentage'])
            
            # Display detailed table
            st.dataframe(
                prob_df.style.format({'Probability': '{:.4f}', 'Percentage': '{:.2f}%'}),
                use_container_width=True,
                hide_index=True
            )
            
        except Exception as e:
            st.markdown(f"""
            <div class="error-box">
                <h3>❌ Error during prediction</h3>
                <p>{str(e)}</p>
            </div>
            """, unsafe_allow_html=True)

# Footer section
st.markdown("---")

# Create tabs for additional information
info_col1, info_col2, info_col3 = st.columns(3)

with info_col1:
    st.subheader("📚 About Dataset")
    st.info("""
    **Dataset Size:** 13,611 samples
    
    **Bean Varieties:** 7 types
    
    **Features:** 16 physical characteristics
    
    **Collection:** Computer vision using camera systems
    """)

with info_col2:
    st.subheader("🤖 Model Details")
    st.info("""
    **Algorithm:** Random Forest Classifier
    
    **Test Accuracy:** 95%+
    
    **Cross-Validation:** 5-fold
    
    **Class Handling:** SMOTE for imbalance
    """)

with info_col3:
    st.subheader("✨ Key Features")
    st.info("""
    ✅ Real-time Classification
    
    ✅ High Accuracy (>95%)
    
    ✅ 16 Physical Characteristics
    
    ✅ Production-Ready Model
    """)

st.markdown("---")
st.subheader("🎯 Model Architecture & Performance")

# Display model information
model_info_col1, model_info_col2 = st.columns(2)

with model_info_col1:
    st.write("### 📊 Feature Categories:")
    st.write("""
    **Shape Descriptors:**
    - Area, Perimeter, Major/Minor Axis Length
    - Aspect Ratio, Eccentricity
    
    **Boundary Features:**
    - Convex Area, Solidity
    - Extent, Roundness
    
    **Mathematical Features:**
    - Equivalent Diameter, Compactness
    - Shape Factors 1-4
    """)

with model_info_col2:
    st.write("### 🏆 Model Algorithms Trained:")
    st.write("""
    1. Logistic Regression
    2. Decision Tree Classifier
    3. **Random Forest (Best)** ⭐
    4. Support Vector Machine (SVM)
    5. K-Nearest Neighbors (KNN)
    6. Naive Bayes
    7. Gradient Boosting Classifier
    """)

st.markdown("---")
st.subheader("💼 Business Impact")

impact_cols = st.columns(4)
with impact_cols[0]:
    st.metric("⚡ Speed", "Real-time", "Instant predictions")
with impact_cols[1]:
    st.metric("🎯 Accuracy", "95%+", "High precision")
with impact_cols[2]:
    st.metric("💰 Cost", "Automated", "Reduces labor")
with impact_cols[3]:
    st.metric("📈 Scale", "Unlimited", "Any volume")

st.markdown("---")
st.caption("🫘 Dry Bean Classifier v1.0 | Powered by Machine Learning | Accuracy: 95%+ | Model: Random Forest")
