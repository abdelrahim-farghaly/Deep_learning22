# Multi-Modal Restaurant Quality Predictor

A university project demonstrating multi-modal machine learning using a realistic restaurant dataset.

## Project Overview

This project uses a multi-modal approach to predict restaurant quality by combining:
- **Tabular Data**: Price range, cuisine type, neighborhood, ratings, review counts
- **Text Data**: Customer reviews for sentiment analysis
- **Image Data**: Restaurant/food images for visual classification

## Key Features

- **Realistic Dataset**: 150+ restaurants with realistic tabular, text, and image data
- **Multi-Modal Dataset**: Combines tabular, text, and image data for comprehensive prediction
- **5 Different Models**: Each demonstrating a different ANN technique
- **Transfer Learning**: Using pre-trained MobileNetV2 for image classification
- **Innovation**: Multi-modal ensemble combining CNN and tabular features

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab

### Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Open Jupyter Notebook:
```bash
jupyter notebook
```

## Project Structure

```
.
├── requirements.txt                  # Python dependencies
├── 01_Data_Scraping.ipynb          # Data generation (realistic restaurant data)
├── 02_Data_Preprocessing.ipynb     # Data cleaning and normalization
├── 03_Model_1_DNN.ipynb           # Deep Neural Network (tabular)
├── 04_Model_2_CNN.ipynb           # CNN with Transfer Learning (images)
├── 05_Model_3_LSTM.ipynb          # LSTM for sentiment analysis (text)
├── 06_Model_4_Transformer.ipynb    # Transformer for sentiment (text)
├── 07_Model_5_MultiModal.ipynb    # Multi-modal ensemble
├── dataset/                         # Data folder
│   ├── restaurant_tabular_data.csv
│   ├── restaurant_reviews.csv
│   ├── restaurant_images.csv
│   └── processed/                  # Preprocessed data
└── restaurant_images/               # Downloaded images
```

## Usage

Run the notebooks in order:

1. **01_Data_Scraping.ipynb** - Generates realistic restaurant data and downloads images
2. **02_Data_Preprocessing.ipynb** - Cleans and normalizes the data
3. **03_Model_1_DNN.ipynb** - DNN for rating prediction from tabular data
4. **04_Model_2_CNN.ipynb** - CNN for high/low tier classification from images
5. **05_Model_3_LSTM.ipynb** - LSTM for sentiment classification from reviews
6. **06_Model_4_Transformer.ipynb** - Transformer for sentiment classification
7. **07_Model_5_MultiModal.ipynb** - Multi-modal ensemble combining images and tabular data

## Models

### 1. DNN (Deep Neural Network)
- **Input**: Tabular features (price, cuisine, neighborhood, rating, review count)
- **Architecture**: 3 hidden layers with dropout
- **Task**: Regression (predict restaurant rating)
- **Key Concepts**: Feedforward networks, regularization, early stopping

### 2. CNN with Transfer Learning
- **Input**: Restaurant/food images (224x224x3)
- **Architecture**: MobileNetV2 (pre-trained on ImageNet) + custom head
- **Task**: Binary classification (high-tier vs low-tier)
- **Key Concepts**: CNNs, transfer learning, fine-tuning, image classification

### 3. LSTM (Long Short-Term Memory)
- **Input**: Text reviews (tokenized and padded)
- **Architecture**: Bidirectional LSTM with embedding layer
- **Task**: Multi-class classification (positive/neutral/negative sentiment)
- **Key Concepts**: RNNs, LSTMs, bidirectional processing, word embeddings

### 4. Transformer
- **Input**: Text reviews (tokenized and padded)
- **Architecture**: Custom Transformer with MultiHeadAttention (TensorFlow native)
- **Task**: Multi-class classification (positive/neutral/negative sentiment)
- **Key Concepts**: Self-attention, multi-head attention, layer normalization
- **Note**: Uses TensorFlow's native layers to avoid HuggingFace compatibility issues

### 5. Multi-Modal Ensemble
- **Input**: Images + Tabular features
- **Architecture**: CNN branch + DNN branch concatenated
- **Task**: Regression (predict rating from both modalities)
- **Key Concepts**: Multi-modal learning, feature fusion, ensemble methods
- **Innovation**: Combines visual and structured data like real-world assessment

## Data Source

Due to anti-bot protection on modern websites (402 Payment Required errors), we generate a realistic restaurant dataset:
- **Approach**: Generate realistic restaurant data with proper structure and variety
- **Data Collected**: Restaurant names, ratings, cuisines, neighborhoods, reviews
- **Images**: Downloaded from Unsplash URLs (real food/restaurant images)
- **Reviews**: 36 unique review templates (12 per sentiment class) with realistic variation
- **Image Sources**: 40+ unique Unsplash image URLs for better diversity
- **Dataset Size**: 150 restaurants for manageable training time

## Requirements Satisfaction

✅ **Multi-modal data**: Tabular + Text + Images
✅ **Custom dataset**: Realistic restaurant data (not from Kaggle or ready-made datasets)
✅ **5 models for 5 team members**: Each model in separate notebook
✅ **Pre-trained models**: MobileNetV2 with transfer learning
✅ **Understanding over accuracy**: Focus on concepts and implementation
✅ **Innovation**: Multi-modal ensemble combining different data types
✅ **No data leakage**: rating_scaled removed from input features (fixed)
✅ **Positional encoding**: Added to Transformer model (fixed)
✅ **Comparative analysis**: New notebook 08 for model comparison
✅ **Architecture justifications**: Added to all 5 model notebooks

## Key Fixes Applied

1. **Data Leakage Fix**: Removed `rating_scaled` from tabular features in preprocessing. The DNN and Multi-Modal models previously had access to a scaled version of the target variable (rating), which invalidated results. Now features are: `price_encoded`, `cuisine_encoded`, `neighborhood_encoded`, `review_count_scaled`.

2. **Positional Encoding Added**: The Transformer model now includes sinusoidal positional encoding, which is essential for the model to understand word order. Without it, the Transformer treats input as a bag-of-words, defeating the purpose of using self-attention.

3. **Comparative Analysis Notebook**: New `08_Model_Comparison.ipynb` loads all 5 trained models, compares them on metrics, parameter counts, and provides side-by-side analysis with visual comparisons.

4. **Architecture Justifications**: Every model notebook now includes detailed explanations of architectural choices: why specific layer sizes, activation functions, dropout rates, and optimizers were chosen.

5. **Expanded Review Templates**: From 15 to 36 unique review texts (12 per sentiment class), providing more diverse text data for LSTM and Transformer models.

6. **Expanded Image Sources**: From 19 to 40+ image URLs, reducing duplication across restaurants.

7. **Confusion Matrices**: Added to CNN, LSTM, and Transformer notebooks for detailed error analysis.

## Notes

- All models are simplified for educational purposes
- Focus on understanding concepts over achieving high accuracy
- Dataset size is kept manageable (~150 restaurants) for quick training
- Images are downloaded from Unsplash URLs; placeholders used if downloads fail
- Transformer uses TensorFlow native layers (MultiHeadAttention) to avoid compatibility issues
- Due to anti-bot protection on modern websites, we generate realistic data instead of scraping
- **Important**: After pulling changes, re-run notebooks 02-07 in order to regenerate processed data and retrain models with fixes

## Team Member Responsibilities

Each team member should:
1. Understand their assigned model architecture (see architecture justifications in each notebook)
2. Be able to explain the key concepts
3. Know the hyperparameters and their effects
4. Understand the training process and results
5. Be able to discuss the comparative analysis in notebook 08

## Professor Requirements Met

- ✅ Custom dataset (not from Kaggle or ready-made datasets)
- ✅ Multi-modal data (3 types: tabular + text + images)
- ✅ Pre-trained models used (MobileNetV2 with transfer learning)
- ✅ Each team member has a distinct model to understand
- ✅ Innovation demonstrated (multi-modal ensemble combining images + tabular data)
- ✅ Focus on understanding, not just accuracy
- ✅ Comparative analysis between models
- ✅ Proper evaluation metrics for each task
- ✅ Architecture justifications with reasoning
- ✅ Confusion matrix analysis for classification models
