# 🎓 Deep Learning Project - Complete Showcase Guide

## 📋 Project: Multi-Modal Restaurant Quality Prediction
### Course: Deep Learning & Neural Networks - Fall 2026
### Faculty of Computer Science & AI, Helwan National University

---

## 🚀 Before You Start: Quick Verification

Open your laptop and do this first to make sure everything works:

### Step 1: Open the Project Folder
```bash
# Open a terminal (Ctrl+Alt+T)
cd ~/Desktop/testing\ the\ final\ version\ of\ DL
ls
```
You should see these files:
```
01_Data_Scraping.ipynb   05_Model_3_LSTM.ipynb
02_Data_Preprocessing.ipynb  06_Model_4_Transformer.ipynb
03_Model_1_DNN.ipynb    07_Model_5_MultiModal.ipynb
04_Model_2_CNN.ipynb    08_Model_Comparison.ipynb
README.md               SHOWCASE_GUIDE.md
requirements.txt        Final_Analysis_Report.pdf
dataset/                restaurant_images/
```

### Step 2: Start Jupyter Notebook
```bash
jupyter notebook
```
Your browser will open with the Jupyter interface showing all the files.

### Step 3: Verify Everything Runs (Optional - already run for you)
Open each notebook and click `Cell > Run All` to verify.
Or just open them one by one and view the already-run outputs.

---

## 📖 PART 1: How to Present the Project (Step by Step)

### 🔹 1.1 Opening Slide / Introduction (2 minutes)

**What to say:**
> "Good morning Professor. Our project is called **Multi-Modal Restaurant Quality Prediction**.
> We chose this domain because restaurants are something everyone can relate to, and they naturally
> have multiple data types: the menu (tabular), customer reviews (text), and food photos (images).
> This let us build **5 different deep learning models**, one for each team member."

**What to show:**
- Open the project folder in your file manager
- Point to the README.md file
- Say: "We have 7 notebooks, starting from data collection all the way to model comparison"

**Tips:**
- Speak clearly, don't rush
- Make eye contact with the professor
- You don't need to memorize - just explain it like you're telling a friend

### 🔹 1.2 Show Notebook 01: Data Generation (2 minutes)

**What to do:**
1. Click on `01_Data_Scraping.ipynb` in Jupyter
2. Scroll through the outputs (they're already run)

**What to say:**
> "This notebook creates our dataset. We generated **150 restaurants** with different cuisines,
> price ranges, and neighborhoods. We downloaded **real food images from Unsplash** (a free photo website),
> and wrote **36 unique review templates** - 12 positive, 12 neutral, 12 negative.
> 
> Initially we planned to scrape from a real review website, but modern sites block automated scraping.
> So we created realistic synthetic data instead, which is still a valid approach since it's our own
> custom dataset - not from Kaggle."

**Key points to show:**
- Scroll to where it says "Generated 150 restaurants" ✓
- Scroll to where it shows the table with restaurant data ✓
- Scroll to where images are downloaded ✓

### 🔹 1.3 Show Notebook 02: Data Preprocessing (1 minute)

**What to do:**
1. Click on `02_Data_Preprocessing.ipynb`
2. Point to the data splitting section

**What to say:**
> "This notebook prepares the data for our models. We split into **80% training (120 samples)**
> and **20% testing (30 samples)**. We encode text using a tokenizer, and resize images to 
> **224x224 pixels** for the CNN.
> 
> **Important fix:** We originally made a mistake where we included the rating as both input AND
> target. We fixed this - `rating_scaled` is now completely removed from the input features."

### 🔹 1.4 Show Notebook 03: DNN Model (your notebook!) (3 minutes)

**What to do:**
1. Click on `03_Model_1_DNN.ipynb`
2. Scroll through the cells slowly

**What to say:**
> "This is my model - the **Deep Neural Network**. It takes 4 features as input:
> - Price range (encoded as numbers)
> - Cuisine type (encoded as numbers)  
> - Neighborhood (encoded as numbers)
> - Number of reviews (scaled)
> 
> And it predicts the **restaurant rating** (from 2.5 to 5.0).
>
> The architecture has **3 hidden layers** with 64, 32, and 16 neurons.
> I used **ReLU activation** because it's standard for hidden layers.
> **Dropout** (0.3 and 0.2) prevents overfitting since we only have 120 training samples.
> **Early stopping** stops training when validation loss stops improving.
>
> The results: **Test MAE of 0.94**, which means on average, our prediction is off by about
> 0.94 rating points. That's not amazing accuracy, but it's an honest result without
> any data leakage."

**If professor asks "Why these numbers?" say:**
> "I chose 64 → 32 → 16 as a funnel shape. The idea is to gradually compress the information.
> 64 neurons in the first layer capture complex patterns, 32 refine them, and 16 extract
> the most important features before making the final prediction."

**If professor asks about ReLU:**
> "ReLU is Rectified Linear Unit. It outputs the input directly if positive, and zero otherwise.
> It's popular because it's simple and doesn't suffer from the vanishing gradient problem
> that sigmoid has."

**Show them:**
- The model summary showing the layers ✓
- The training loss graph (it should show loss decreasing) ✓
- The test results at the bottom ✓

### 🔹 1.5 Show Notebook 04: CNN Model (2 minutes)

**What to do:**
1. Click on `04_Model_2_CNN.ipynb`
2. Scroll to the model summary

**What to say:**
> "The CNN model uses **MobileNetV2**, which is pre-trained on ImageNet (1.2 million images).
> This is **transfer learning** - we take a model that already knows how to recognize
> general features (edges, shapes, textures) and adapt it for our specific task.
>
> The task is **binary classification**: is this restaurant high-tier or low-tier?
> The accuracy is around **67%**, which is better than random guessing (50%) but not great.
> This is expected because our images are generic food photos from Unsplash, not actual
> restaurant-specific images."

**Show them:**
- The MobileNetV2 architecture in the output ✓
- The confusion matrix (showing how many were correctly classified) ✓

### 🔹 1.6 Show Notebook 05: LSTM Model (2 minutes)

**What to do:**
1. Click on `05_Model_3_LSTM.ipynb`
2. Scroll to the classification report

**What to say:**
> "The LSTM model handles **text sentiment analysis**. It reads customer reviews and classifies
> them as positive, neutral, or negative. It uses **Bidirectional LSTM** layers, which means
> it reads the review both forwards AND backwards to capture more context.
>
> Accuracy is **93%**, which is quite good. But note it struggles with the 'Negative' class
> because we have very few negative examples in our dataset."

**Show them:**
- The Bidirectional LSTM architecture ✓
- The classification report showing precision/recall ✓
- The confusion matrix ✓

### 🔹 1.7 Show Notebook 06: Transformer Model (2 minutes)

**What to do:**
1. Click on `06_Model_4_Transformer.ipynb`
2. Point to the PositionalEncoding class

**What to say:**
> "The Transformer model also does sentiment analysis, but uses **self-attention** instead of
> recurrence. It processes all words simultaneously rather than one at a time like LSTM.
>
> **We added sinusoidal positional encoding**, which tells the model the position of each word.
> Without this, the Transformer treats the sentence as a bag of words - order doesn't matter.
> With positional encoding, it understands that 'not good' is different from 'good not'.
>
> It achieves **100% accuracy** on our test set."

**Show them:**
- The PositionalEncoding class ✓
- The TransformerEncoder class ✓
- The model summary ✓
- The confusion matrix (perfect prediction) ✓

### 🔹 1.8 Show Notebook 07: Multi-Modal Model (2 minutes)

**What to do:**
1. Click on `07_Model_5_MultiModal.ipynb`
2. Scroll to the model combining section

**What to say:**
> "This is our **innovation model** - it combines TWO types of data: images AND tabular data.
> A CNN branch processes images (using MobileNetV2), and a DNN branch processes the
> 4 structured features. These are then **concatenated** and passed through dense layers
> to predict the rating.
>
> This achieves **MAE of 0.52**, which is significantly better than the DNN alone (0.94).
> This proves that **combining multiple data types gives better results** - the model learns
> from both visual appearance AND restaurant attributes."

**Show them:**
- The architecture diagram showing two branches merging ✓
- The comparison: Multi-Modal (0.52) vs DNN (0.94) ✓

### 🔹 1.9 Show Notebook 08: Model Comparison (3 minutes)

**What to do:**
1. Click on `08_Model_Comparison.ipynb`
2. Scroll to the comparison table

**What to say:**
> "This notebook compares all 5 models side by side. Here's what we found:
>
> | Model | Task | Best Metric |
> |-------|------|-------------|
> | **DNN** | Rating Regression | MAE = 0.94 |
> | **CNN** | Tier Classification | Accuracy = 67% |
> | **LSTM** | Sentiment Analysis | Accuracy = 93% |
> | **Transformer** | Sentiment Analysis | Accuracy = 100% |
> | **Multi-Modal** | Rating Regression | MAE = 0.52 |
>
> Key insight: **The Multi-Modal model performs best** because it can use information from
> both images AND structured data. This is how humans actually assess restaurants -
> we look at the food AND consider factors like price and location."

**Show them:**
- The comparison table ✓
- The bar charts showing accuracy and MAE ✓
- The strengths & weaknesses table ✓

### 🔹 1.10 Closing & Questions (2-3 minutes)

**What to say:**
> "To summarize our project:
> 1. We built a multi-modal restaurant quality prediction system
> 2. We implemented 5 different deep learning architectures
> 3. We fixed critical issues like data leakage and missing positional encoding
> 4. We showed that combining multiple data types (multi-modal) gives the best results
>
> **What we learned:**
> - Data quality is more important than model complexity
> - Simple models (DNN) can work well when features are relevant
> - Transfer learning (MobileNetV2) saves enormous training time
> - Transformers need positional encoding to understand word order
> - Multi-modal fusion is a powerful technique for real-world applications"

---

## ❓ PART 2: Common Professor Questions & Answers

### Q: Why did you choose 150 restaurants? Why not more?
> **Answer:** "We chose 150 as a balance between having enough data and keeping training time manageable.
> Since this is a course project meant for understanding concepts, the professor emphasized
> understanding over accuracy. 150 samples let each model train in under 5 minutes while still
> demonstrating all the key concepts."

### Q: Why is CNN accuracy only 67%?
> **Answer:** "The images we downloaded are generic food photos from Unsplash, not actual restaurant
> photos tied to quality. A restaurant with great food and a restaurant with bad food both have
> similar-looking food photos. That's why the accuracy is barely above chance."

### Q: What is data leakage and how did you fix it?
> **Answer:** "Data leakage means information from the target leaks into the input features.
> We had `rating_scaled` - a normalized version of the rating - as an input feature while trying
> to predict the rating itself. That's like giving a student the answer key and testing if they
> can find it. We fixed it by simply removing that column from the input features."

### Q: What's the difference between LSTM and Transformer?
> **Answer:** "LSTM processes text sequentially - word by word - using recurrent connections.
> Transformer uses self-attention to look at ALL words at once and figure out which ones
> are important. Transformer is faster to train (parallel processing) but needs positional
> encoding to understand word order. LSTM naturally handles order but is slower."

### Q: Why is Multi-Modal better than DNN alone?
> **Answer:** "The Multi-Modal model has access to image features from the CNN branch,
> which gives it additional information that the DNN doesn't have. Even though the images
> alone aren't great predictors, when combined with tabular features, they provide useful
> supplementary signals that improve the overall prediction."

### Q: What would you improve if you had more time?
> **Answer:** "We would:
> 1. Expand the dataset to 500+ restaurants
> 2. Add more diverse review texts
> 3. Implement image data augmentation (rotation, flipping)
> 4. Add cross-validation for more reliable metrics
> 5. Try actual web scraping from a real restaurant site"

---

## 📊 PART 3: Final Model Results (For Reference)

All models have been trained and saved. Here are the final numbers:

| Model | Input Type | Task | Key Metric | Parameters |
|-------|-----------|------|-----------|------------|
| **DNN** | 4 tabular features | Predict Rating (1-5) | MAE = **0.94** | 2,945 |
| **CNN (MobileNetV2)** | Images (224x224) | High/Low Tier | Accuracy = **67%** | 2.4M (mostly frozen) |
| **LSTM (Bidirectional)** | Reviews (tokenized) | Positive/Neutral/Negative | Accuracy = **93%** | 429K |
| **Transformer** | Reviews + Positional Encoding | Positive/Neutral/Negative | Accuracy = **100%** | 362K |
| **Multi-Modal** | Images + Tabular | Predict Rating (1-5) | MAE = **0.52** | 2.3M (mostly frozen) |

---

## 📁 PART 4: Project Files Reference

| File | Purpose |
|------|---------|
| `01_Data_Scraping.ipynb` | Generate dataset, download images, create reviews |
| `02_Data_Preprocessing.ipynb` | Encode, normalize, split data for all models |
| `03_Model_1_DNN.ipynb` | Deep Neural Network for rating prediction |
| `04_Model_2_CNN.ipynb` | CNN with MobileNetV2 for tier classification |
| `05_Model_3_LSTM.ipynb` | Bidirectional LSTM for sentiment analysis |
| `06_Model_4_Transformer.ipynb` | Transformer with positional encoding for sentiment |
| `07_Model_5_MultiModal.ipynb` | Multi-modal (CNN + DNN) for rating prediction |
| `08_Model_Comparison.ipynb` | Compare all 5 models side by side |
| `README.md` | Project overview and instructions |
| `Final_Analysis_Report.pdf` | Detailed analysis report (LaTeX) |
| `SHOWCASE_GUIDE.md` | This file - your presentation guide |
| `dataset/` | CSV data and processed .npy files |
| `dataset/processed/` | Saved models (.keras), encoders (.pkl) |
| `restaurant_images/` | 150 restaurant/food images |

---

## ⚡ PART 5: Quick Troubleshooting

**Problem:** Jupyter notebook won't open
**Fix:** Run `pip install notebook` in terminal, then `jupyter notebook` again

**Problem: "Module not found" error**
**Fix:** Run `pip install -r requirements.txt` in the project folder

**Problem: No images in restaurant_images folder**
**Fix:** Run notebook 01 again (Cell > Run All)

**Problem: Model files are missing**
**Fix:** Run notebooks 03-07 in order

**Problem: Kernel keeps dying**
**Fix:** Close other programs to free RAM. The CNN and Multi-Modal need ~4GB RAM.

---

## 💡 PART 6: Tips for a Great Presentation

### DO:
- ✅ Speak slowly and clearly
- ✅ Point to specific outputs in the notebook
- ✅ Explain WHY you made each decision
- ✅ Admit limitations honestly ("our images aren't perfect")
- ✅ Show that you understand the concepts
- ✅ Use the architecture justifications we added to each notebook

### DON'T:
- ❌ Read directly from slides/notebooks
- ❌ Pretend to know something you don't
- ❌ Ignore mistakes - explain what you learned from them
- ❌ Rush through the presentation

### Your main talking points for YOUR model (DNN):
1. **Input:** 4 features (price, cuisine, neighborhood, review count)
2. **Architecture:** 64 → 32 → 16 neurons with dropout
3. **Why these choices:** Funnel shape compresses information gradually
4. **Regularization:** Dropout prevents overfitting on small dataset
5. **Training:** Early stopping when validation loss plateaus
6. **Result:** MAE of 0.94 (predicts rating within ~1 point)
7. **Data leakage fix:** Removed rating_scaled from input

---

## ✅ PART 7: Final Checklist Before Presentation

- [ ] All notebooks open and showing outputs
- [ ] Dataset files (.csv) are in the dataset folder
- [ ] 150 images in restaurant_images folder
- [ ] All 5 models are trained and saved (.keras files)
- [ ] Model comparison notebook (08) shows results
- [ ] README is up to date
- [ ] Laptop is charged / plugged in
- [ ] Jupyter notebook is running
- [ ] Project folder is organized and clean
- [ ] You've practiced explaining YOUR model (DNN) at least 3 times

---

## 🎯 Good Luck!

Remember: The professor wants to see that you UNDERSTAND what you built, not that you got perfect accuracy. Explaining the data leakage fix actually shows MORE understanding than if you had gotten it right the first time.

**You've got this! 💪**
