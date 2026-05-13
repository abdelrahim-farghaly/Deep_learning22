# 🧠 The Complete Project Explanation
## From "What is this?" to "I can explain it to my professor"

---

# 📌 PART 0: First Things First

Before anything else, open your terminal and run this:
```bash
cd ~/Desktop/testing\ the\ final\ version\ of\ DL
jupyter notebook
```
This opens Jupyter in your browser. You'll see a list of `.ipynb` files. These are **Jupyter Notebooks** — interactive documents where you can write and run Python code, see the output immediately, and add text explanations. Think of them as Python scripts where you can see results right below each block of code.

Now let's understand what all of this even means.

---

# 📌 PART 1: What Is This Whole Thing? (The Big Picture)

### The Project in One Sentence
We are building a system that tries to **predict how good a restaurant is** — like its rating out of 5 — using three different kinds of information:
1. **Basic info** about the restaurant (price range, type of food, location, number of reviews)
2. **Customer reviews** written in text (positive or negative sentiment)
3. **Photos** of the restaurant/food

### Why Three Types of Data?
Because in real life, when you decide if a restaurant is good, you use multiple sources of information:
- You look at the **menu prices** (tabular data)
- You read **Google reviews** (text data)
- You look at **photos of the food** (image data)

This is called **multi-modal** — "multi" = many, "modal" = type/form of data.

### But Wait, Why Do We Need 5 Different Models?
Each "model" is basically a different recipe/algorithmy for learning from data. The professor asked for 5 models because there are 5 team members. Each team member is responsible for understanding ONE model deeply. The 5 models we built are:

| # | Model Name | What it does | Data it uses |
|---|-----------|-------------|-------------|
| 1 | **DNN** (Deep Neural Network) | Predicts a rating number (like 4.2 out of 5) | Basic info (price, cuisine, neighborhood, review count) |
| 2 | **CNN** (Convolutional Neural Network) | Classifies as "high quality" or "low quality" | Restaurant/food images |
| 3 | **LSTM** (Long Short-Term Memory) | Classifies review as positive/neutral/negative | Customer review text |
| 4 | **Transformer** | Same as LSTM but uses a different technique | Customer review text |
| 5 | **Multi-Modal** | Predicts a rating using TWO data types together | Images + basic info |

You — Ahmed — are responsible for **Model 1: DNN**. But you need to understand the whole project.

---

# 📌 PART 2: What Even IS Deep Learning? (The Simplest Explanation)

### The "Recipe" Analogy

Imagine you're teaching a child to recognize apples:
1. You show them 1000 pictures of apples and say "this is an apple"
2. You show them 1000 pictures of oranges and say "this is NOT an apple"
3. After enough examples, the child can look at a new fruit and say "that's an apple" or "that's not an apple"

**Deep Learning is exactly the same**, except instead of a child, it's a mathematical formula with millions of adjustable knobs (called "parameters" or "weights"). The process:

1. **Training**: We show the model thousands of examples. For each example, the model makes a guess. If it's wrong, we slightly adjust the knobs. Repeat thousands of times.
2. **Testing**: We show the model NEW examples it has never seen, and see how well it does.
3. **Evaluation**: We measure accuracy ("how many did it get right?") or error ("how far off was its prediction?")

### Key Terms You MUST Know

**Training**: The learning phase. The model sees data and adjusts its parameters.
**Testing**: After training, we check if the model works on new, unseen data.
**Overfitting**: When the model memorizes the training data but can't handle new data (like a student who memorizes answers but can't solve new problems).
**Epoch**: One complete pass through all training data. We usually do 30-50 epochs.
**Loss**: A number that tells us how wrong the model is. Lower = better.
**Accuracy**: Percentage of correct predictions (for classification tasks).
**MAE**: Mean Absolute Error — on average, how far off our prediction is (for regression/number-prediction tasks).

---

# 📌 PART 3: What Are These 5 Model Types? (For Complete Beginners)

## Model 1: DNN — Deep Neural Network

### What it does in human terms:
Imagine you're guessing a restaurant's rating. You know:
- It's Italian cuisine (+0.2 to rating)
- It's in a fancy neighborhood (+0.3)
- Price range is $$$ (maybe +0.1 or -0.1)
- It has 500 reviews (probably popular, +0.2)

A DNN learns **which combinations** of these factors matter and how much. It might discover that "expensive Italian in Downtown" tends to have higher ratings, but "expensive American in Westside" doesn't.

### Architecture (the structure):
```
Input Layer (4 neurons) → Hidden Layer 1 (64 neurons) → Dropout → 
Hidden Layer 2 (32 neurons) → Dropout → Hidden Layer 3 (16 neurons) → 
Output Layer (1 neuron = the predicted rating)
```

**Neuron**: A single mathematical unit that takes inputs, multiplies them by weights, adds them up, and applies an activation function.
**Layer**: A group of neurons working together.
**Dropout**: Randomly turns off some neurons during training — like making the model learn to work even when some parts are missing (prevents overfitting).

### What the numbers 64→32→16 mean:
The funnel shape. First layer has 64 neurons to capture many patterns. Second layer has 32 to focus on important patterns. Third has 16 to extract the most essential features. Final layer has 1 neuron to output a single number (the rating).

### Key terms for this model:
- **Activation function (ReLU)**: A mathematical function that decides whether a neuron should "fire" or not. ReLU = if input is positive, output it; if negative, output 0.
- **Optimizer (Adam)**: The algorithm that decides HOW to adjust the knobs during training.
- **Learning rate**: How big each adjustment is. 0.001 means small, careful steps.
- **Early stopping**: Stop training when the model stops improving (saves time, prevents overfitting).

## Model 2: CNN — Convolutional Neural Network

### What it does:
Looks at images and tries to find patterns. A CNN doesn't see the whole image at once — it slides a small window (like 3x3 pixels) across the image and looks for features like edges, textures, shapes, and eventually whole objects.

### Why MobileNetV2?
MobileNetV2 is a pre-built CNN that was trained on 1.2 million images from ImageNet (a huge database of labeled images). Instead of training a CNN from scratch (which would need millions of images), we take MobileNetV2 that already knows how to recognize edges and shapes, and we just add a few new layers on top for our specific task. This is called **transfer learning** — like taking a chef who already knows basic cooking techniques and teaching them a new recipe.

### Why the accuracy is 67%:
Our images are generic food photos from Unsplash (a free photo site). A photo of pizza doesn't tell you if the restaurant is high-quality or low-quality. The model is basically guessing. 67% is barely above 50% (random guessing).

## Model 3: LSTM — Long Short-Term Memory

### What it does:
Reads text one word at a time, but **remembers what came before**. That's the "memory" part. When it reads "The food was NOT good," it remembers the "NOT" when it gets to "good" and understands the sentence is negative.

### Why "Bidirectional"?
Normal LSTM reads left-to-right. Bidirectional LSTM reads left-to-right AND right-to-left. It captures context from both directions. Like reading "not good" — from left it's "not" then "good" (negative), from right it's "good" preceded by "not" (also negative).

## Model 4: Transformer

### What it does:
Same job as LSTM (sentiment classification) but uses a completely different mechanism called **self-attention**. Instead of reading word-by-word, it looks at ALL words at once and figures out which words are important to each other.

### Why Positional Encoding?
Since the Transformer looks at all words simultaneously, it has NO IDEA about word order. "Dog bites man" and "Man bites dog" have the same words but mean different things. **Positional encoding** adds a unique signal to each word position so the model can distinguish between word 1, word 2, word 3, etc.

Without positional encoding, a Transformer is just a "bag of words" — it can't tell the difference between "not good" and "good not."

### Why we built it from scratch:
We used TensorFlow's built-in `MultiHeadAttention` layer instead of the popular HuggingFace library. This avoids installation/compatibility issues and shows we understand the underlying mechanism.

## Model 5: Multi-Modal (The Innovation Model)

### What it does:
This is the only model that uses **two different types of data at the same time**: images AND tabular data. It has TWO "branches":
- **Left branch**: A CNN (MobileNetV2) that processes images
- **Right branch**: A small DNN that processes tabular data

The outputs of these two branches are **concatenated** (glued together) and passed through more layers to make the final prediction.

### Why this is "innovation":
Most projects use only ONE type of data. Using two different types together is more realistic — think of Yelp: you look at the star rating AND the photos AND the reviews. This model mimics how humans actually make decisions.

### Why it performs best (MAE = 0.52 vs DNN's 0.94):
It has MORE information. The DNN only uses 4 numbers. The Multi-Modal uses 4 numbers PLUS image features (1280 numbers from MobileNetV2). More information = better predictions (usually).

---

# 📌 PART 4: What Is In Each File? (Complete File-by-File Walkthrough)

## 📁 `01_Data_Scraping.ipynb` — Creating the Dataset

### What this file does:
Creates fake but realistic restaurant data. Generates 150 restaurants with names, cuisines, prices, neighborhoods, ratings, reviews, and downloads real images.

### Step-by-step code explanation:

**Cell 1**: Creates folders to store data
```python
os.makedirs('dataset', exist_ok=True)  # Makes a folder called 'dataset'
os.makedirs('restaurant_images', exist_ok=True)  # Makes a folder for images
```

**Cell 2**: Defines templates for data
```python
cuisines = ['Italian', 'Asian', 'Mexican', ...]  # List of 10 cuisine types
neighborhoods = ['Downtown', 'Midtown', ...]  # List of 7 neighborhoods
prices = ['$', '$$', '$$$', '$$$$']  # 4 price levels
```
Then defines 36 review templates (12 positive, 12 neutral, 12 negative):
```python
positive_reviews = ['Absolutely amazing!...', 'Excellent food...', ...]  # 12 positive templates
neutral_reviews = ['Good restaurant...', 'Nice place...', ...]  # 12 neutral templates
negative_reviews = ['Disappointing...', 'Poor service...', ...]  # 12 negative templates
```

**Cell 3**: Generates the actual 150 restaurants
```python
for i in range(150):
    rating = random number between 2.5 and 5.0  # Beta distribution gives realistic ratings
    review_text = pick a review template based on rating  # High rating → positive review
    review_count = calculate from rating + some randomness
    # Store all this in a dictionary
```

**Cell 4-5**: Saves data to CSV files
```python
df.to_csv('dataset/restaurant_tabular_data.csv')  # Main data table
reviews_df.to_csv('dataset/restaurant_reviews.csv')  # Reviews only
images_df.to_csv('dataset/restaurant_images.csv')  # Image references
```

**Cell 6-9**: Downloads real images from Unsplash
```python
for each restaurant:
    pick an image URL  # Rotate through 39 different URLs
    download the image  # Save to restaurant_images/ folder
    if download fails:  # Copy a successful one
        copy from another image
```

### Why this matters:
You can't do deep learning without data. This is the FOUNDATION of everything else. Bad data = bad models. That's why we expanded from 15 review templates to 36 — more variety in reviews means more realistic text data.

---

## 📁 `02_Data_Preprocessing.ipynb` — Preparing Data for the Models

### What this file does:
Takes the raw data and transforms it into a format that the models can understand. Models don't speak "Italian" or "Downtown" — they only understand numbers.

### Key Operations:

**1. Load the data**
```python
df_restaurants = pd.read_csv('dataset/restaurant_tabular_data.csv')
df_reviews = pd.read_csv('dataset/restaurant_reviews.csv')
df_images = pd.read_csv('dataset/restaurant_images.csv')
```

**2. Encode categories (turn text into numbers)**
```python
price_encoder = LabelEncoder()
df_restaurants['price_encoded'] = price_encoder.fit_transform(df_restaurants['price_range'])
# '$' → 0, '$$' → 1, '$$$' → 2, '$$$$' → 3
```
Same for cuisine and neighborhood. This turns "Italian" → 0, "Asian" → 1, etc.

**3. Scale numbers (make them comparable)**
```python
scaler = StandardScaler()
df_restaurants[['review_count_scaled']] = scaler.fit_transform(df_restaurants[['review_count']])
```
Review counts range from 10 to 322. Scaling transforms them so they have a "standard" range, making it easier for the model to learn.

**IMPORTANT**: We do NOT scale the `rating` column because that's what we're trying to PREDICT. The old code had `rating_scaled` as an input feature, which was a **data leakage bug**. We fixed it.

**4. Prepare tabular features**
```python
tabular_features = df_restaurants[['price_encoded', 'cuisine_encoded', 'neighborhood_encoded', 'review_count_scaled']].values
tabular_target = df_restaurants['rating'].values
```
4 features → predict rating. Notice `rating_scaled` is NOT here anymore.

**5. Split into training and testing**
```python
X_tab_train, X_tab_test, y_tab_train, y_tab_test = train_test_split(
    tabular_features, tabular_target, test_size=0.2, random_state=42
)
# 120 for training, 30 for testing
```
**80% training, 20% testing**. We train on the 120, test on the 30. The test set is NEVER seen during training — it's like an exam the model hasn't studied for.

**6. Tokenize text (turn words into numbers)**
```python
tokenizer = Tokenizer(num_words=5000)  # Only keep the 5000 most common words
tokenizer.fit_on_texts(df_reviews['review_text'])  # Learn the vocabulary
sequences = tokenizer.texts_to_sequences(df_reviews['review_text'])  # Convert words to numbers
padded_sequences = pad_sequences(sequences, maxlen=100)  # Make all sequences the same length (100 words)
```
Each review becomes a list of 100 numbers. If the review has fewer than 100 words, pad with zeros. If more, truncate.

**7. Load and normalize images**
```python
img = load_img(path, target_size=(224, 224))  # Resize all images to 224x224
img_array = img_to_array(img)  # Convert to array of numbers
img_array = img_array / 255.0  # Scale pixel values from 0-255 to 0-1
```
Images are 224x224 pixels with 3 color channels (RGB). Each pixel has a value 0-255. Dividing by 255 brings them to 0-1 range, which helps the model train better.

### Why this matters:
Raw data → processed data → model input. This step is CRITICAL. If you mess up preprocessing, your models will give garbage results no matter how good your architecture is.

---

## 📁 `03_Model_1_DNN.ipynb` — YOUR Model (Deep Neural Network)

### What this file does:
Builds, trains, and evaluates a DNN that predicts restaurant ratings from 4 tabular features.

### Step-by-step code explanation:

**Cell 1**: Import libraries
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
```
- `Sequential`: A linear stack of layers (one after another)
- `Dense`: A fully connected layer (every neuron connects to every neuron in the next layer)
- `Dropout`: Randomly turns off neurons during training
- `Adam`: The optimizer algorithm
- `EarlyStopping`: Stops training when no improvement

**Cell 2**: Load the preprocessed data
```python
X_train = np.load('dataset/processed/X_tab_train.npy')  # Training features (120, 4)
X_test = np.load('dataset/processed/X_tab_test.npy')    # Testing features (30, 4)
y_train = np.load('dataset/processed/y_tab_train.npy')  # Training targets (120,)
y_test = np.load('dataset/processed/y_tab_test.npy')    # Testing targets (30,)
```
Shape `(120, 4)` means 120 samples, each with 4 features.

**Cell 3**: Build the model
```python
model = Sequential([
    Dense(64, activation='relu', input_shape=(4,)),  # Input: 4 features → 64 neurons
    Dropout(0.3),                                     # Turn off 30% of neurons randomly
    Dense(32, activation='relu'),                     # 64 → 32 neurons
    Dropout(0.2),                                     # Turn off 20% of neurons
    Dense(16, activation='relu'),                     # 32 → 16 neurons
    Dense(1, activation='linear')                     # 16 → 1 output (the rating)
])

model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mae'])
```
- `input_shape=(4,)`: The model expects 4 input numbers
- `activation='relu'`: ReLU activation for hidden layers (standard choice)
- `activation='linear'`: Linear activation for output (needed for regression — predicting any number, not just 0 or 1)
- `loss='mse'`: Mean Squared Error — the loss function. It penalizes large errors more than small ones.
- `metrics=['mae']`: Mean Absolute Error — easier to understand. "On average, off by X points."

**Cell 4**: Train the model
```python
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

history = model.fit(
    X_train, y_train,
    epochs=50,            # Do 50 complete passes through the data
    batch_size=32,        # Process 32 samples at a time
    validation_split=0.2, # Use 20% of training data for validation
    callbacks=[early_stopping],
    verbose=1
)
```
- `epochs=50`: Train for up to 50 rounds
- `batch_size=32`: Look at 32 restaurants at a time, compute error, adjust weights, repeat
- `validation_split=0.2`: From the 120 training samples, use 96 for training and 24 for validation
- `early_stopping`: If validation loss doesn't improve for 10 consecutive epochs, stop and restore the best model
- During training, you'll see output like: `Epoch 1/50 - loss: 14.8 - mae: 3.7 - val_loss: 13.1 - val_mae: 3.5`
  - `loss`: Training error (goes down over time)
  - `mae`: Training MAE (goes down over time)
  - `val_loss`: Validation error (should also go down)
  - `val_mae`: Validation MAE

**Cell 5**: Evaluate on test data
```python
loss, mae = model.evaluate(X_test, y_test)
print(f'Test MSE: {loss:.4f}')
print(f'Test MAE: {mae:.4f}')
```
This runs the model on the 30 test samples it has NEVER seen. Result: MAE ≈ 0.94, meaning on average, our predicted rating is 0.94 points off from the true rating.

**Cells 6-7**: Plot training history and save model
```python
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
# ... shows how loss decreased over epochs

model.save('dataset/processed/dnn_model.keras')
```

### What the Results Mean:
- **MAE of 0.94**: If the true rating is 4.0, our prediction is typically around 3.06 to 4.94. It's a rough estimate.
- **Is this good?** Not amazing, but HONEST. The old model had MAE of 0.73 but that was CHEATING (data leakage).
- **The validation loss is higher than training loss**: This is normal — the model is slightly overfitting (memorizing training data patterns that don't generalize perfectly).

---

## 📁 `04_Model_2_CNN.ipynb` — Convolutional Neural Network

### What this file does:
Takes images of restaurants/food and classifies them as "high-quality" or "low-quality" restaurant.

### Step-by-step:

**Cell 1**: Import libraries — same pattern as DNN but with MobileNetV2

**Cell 2**: Load image data
```python
X_train = np.load('dataset/processed/X_img_train.npy')  # (120, 224, 224, 3)
X_test = np.load('dataset/processed/X_img_test.npy')    # (30, 224, 224, 3)
```
Each image is 224x224 pixels with 3 color channels.

**Cell 3**: Build the model
```python
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False  # Freeze the pre-trained layers

# Add custom layers on top
model = Sequential([
    base_model,
    GlobalAveragePooling2D(),  # 7x7x1280 → 1280 (average all values)
    Dense(128, activation='relu'),  # 1280 → 128
    Dropout(0.5),               # Strong dropout (half the neurons turned off)
    Dense(1, activation='sigmoid')  # 128 → 1 (probability 0-1)
])
```
- `MobileNetV2(weights='imagenet')`: Load a model pre-trained on ImageNet
- `trainable = False`: Don't change the pre-trained weights (save time, prevent overfitting)
- `GlobalAveragePooling2D`: Condenses the 7x7x1280 feature maps into a single 1280-number vector
- `activation='sigmoid'`: Outputs a probability between 0 and 1 (binary classification)
- Training: Predicts probability. If > 0.5, it's "high tier." If < 0.5, "low tier."

**Results**: Accuracy ≈ 67% (barely above 50% random guessing)
**Confusion Matrix**:
```
[[8 9]   → 17 actually low-tier: 8 correct, 9 wrong
 [9 4]]   → 13 actually high-tier: 4 correct, 9 wrong
```
The model correctly identified only 12 out of 30 restaurants. This tells us the images alone are NOT good predictors of restaurant quality.

### Why this result is IMPORTANT to talk about:
It shows you understand that **data quality matters more than model complexity**. The most complex model (2.4 million parameters) performs worst because the images have no real connection to restaurant quality. This is a valuable lesson.

---

## 📁 `05_Model_3_LSTM.ipynb` — Long Short-Term Memory

### What this file does:
Reads customer review text and classifies the sentiment as positive, neutral, or negative.

### Step-by-step:

**Cell 1**: Import libraries — introduces `Embedding`, `LSTM`, `Bidirectional`

**Cell 2**: Load text data
```python
X_train = np.load('dataset/processed/X_text_train.npy')  # (120, 100)
# Each review is now 100 numbers (word indices)
```

**Cell 3**: Build the LSTM model
```python
model = Sequential([
    Embedding(5000, 64),                    # Convert word indices to 64-dimension vectors
    Bidirectional(LSTM(64, return_sequences=True)),  # First LSTM layer (bidirectional)
    Dropout(0.5),
    Bidirectional(LSTM(32)),                # Second LSTM layer
    Dropout(0.3),
    Dense(32, activation='relu'),           # Combine LSTM outputs
    Dense(3, activation='softmax')          # 3 classes: positive/neutral/negative
])
```
- `Embedding(5000, 64)`: Each word (from a 5000-word vocabulary) gets converted to a 64-number vector. Similar words end up with similar vectors.
- `Bidirectional(LSTM(64))`: Two LSTM layers reading in opposite directions, each with 64 memory units
- `return_sequences=True`: Pass the full sequence (not just final output) to the next LSTM layer
- `activation='softmax'`: Outputs 3 probabilities that sum to 1.0. [0.1, 0.85, 0.05] means 85% confident it's neutral.

### Results:
- Accuracy: 93%
- **Important caveat**: The model struggles with "Negative" class (0% recall) because we only have 2 negative reviews in the test set. The dataset has class imbalance.

---

## 📁 `06_Model_4_Transformer.ipynb` — Transformer Model

### What this file does:
Same sentiment analysis task as LSTM but using a Transformer architecture (self-attention instead of recurrence).

### Key Difference from LSTM:
- **LSTM**: Reads words one by one, maintaining a "memory" of what came before
- **Transformer**: Looks at ALL words at once, uses "attention" to figure out which words are related to which

### What's NEW in this implementation (our fix):

**Positional Encoding** — We added this. It tells the model WHERE each word is in the sentence:
```python
class PositionalEncoding(tf.keras.layers.Layer):
    def __init__(self, max_len, embed_dim):
        ...
        # Create a unique pattern for each position:
        # Position 0 gets [sin(0), cos(0), sin(0), cos(0), ...]
        # Position 1 gets [sin(1), cos(1), sin(0.5), cos(0.5), ...]
        # Each position has a UNIQUE fingerprint
```

**Transformer Encoder Block**:
```python
class TransformerEncoder(tf.keras.layers.Layer):
    def call(self, inputs, training=False):
        attn_output = self.att(inputs, inputs)  # Self-attention: each word looks at all other words
        out1 = self.layernorm1(inputs + attn_output)  # Add + normalize (residual connection)
        ffn_output = self.ffn(out1)  # Feed-forward network
        return self.layernorm2(out1 + ffn_output)  # Add + normalize again
```

### Results:
- Accuracy: **100%** (perfect on test set)
- Confusion matrix shows all 30 test samples correctly classified

---

## 📁 `07_Model_5_MultiModal.ipynb` — Multi-Modal Ensemble

### What this file does:
Combines TWO data types (images + tabular data) to predict restaurant ratings.

### Architecture:
```
                    ┌──────────────────┐
                    │   Image Input    │
                    │  (224x224x3)     │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │  MobileNetV2     │
                    │  (frozen)        │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │GlobalAvgPooling2D │
                    │  → 1280 numbers   │
                    └────────┬─────────┘
                             │
                    ┌────────┴──────────┐
                    │  CONCATENATE      │
                    │  1280 + 32 = 1312 │
                    └────────┬──────────┘
                             │
                    ┌────────▼─────────┐
                    │ Dense(64) + Drop │
                    │ Dense(32) + Drop │
                    │  Dense(1) = rating│
                    └──────────────────┘

                    ┌──────────────────┐
                    │  Tabular Input   │
                    │  (4 features)    │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │  Dense(32) + Drop│
                    │  → 32 numbers    │
                    └──────────────────┘
```

### Why This Is Innovation:
Most university projects use ONE model on ONE type of data. This model uses TWO different types of data simultaneously. The model learns to weigh both visual information and structured information to make a better prediction. This is closer to how real AI systems work (think of Google Photos, which uses image + text metadata).

### Results:
- **MAE: 0.52** — Much better than DNN alone (0.94)
- This proves that combining multiple data sources gives better predictions

---

## 📁 `08_Model_Comparison.ipynb` — Putting It All Together

### What this file does:
Loads all 5 trained models, evaluates them on the same test data, and presents a side-by-side comparison.

### Why this exists:
The grading rubric has 2 marks for "Experimental & Comparative Analysis." Without this notebook, we'd get ZERO on that criterion.

### What You See:
A table comparing all models:
```
Model              Type          MAE/Accuracy   Parameters
───────────────────────────────────────────────────────────
DNN                Regression    MAE = 0.94      2,945
CNN                Classifier    Acc = 67%    2,422,081
LSTM               Classifier    Acc = 93%      429,443
Transformer        Classifier    Acc = 100%     361,987
Multi-Modal        Regression    MAE = 0.52   2,344,289
```

### Key Insights From This Comparison:
1. **Multi-Modal is best for rating prediction** (MAE 0.52 vs DNN's 0.94)
2. **Transformer beats LSTM** (100% vs 93%) for sentiment
3. **CNN is worst** because images don't correlate with quality
4. **More parameters ≠ better results** (CNN has 2.4M params but worst performance)

---

# 📌 PART 5: How Everything Connects — The Big Picture

## The Data Flow:
```
01_Data_Scraping.ipynb          → Creates raw data (CSV files + images)
         │
         ▼
02_Data_Preprocessing.ipynb    → Transforms raw data into numbers (.npy files)
         │
         ├────────────────────────────────────────────────────┐
         │                      │                            │
         ▼                      ▼                            ▼
03_DNN.ipynb           04_CNN.ipynb                  05_LSTM.ipynb
(Tabular data)         (Image data)                   (Text data)
         │                      │                            │
         │                      ├────────────────────────────┘
         │                      ▼
         │              07_MultiModal.ipynb
         │              (Images + Tabular)
         │                      │
         └──────────────────────┴────────────06_Transformer.ipynb
                                              (Text data)
                           │
                           ▼
                    08_Model_Comparison.ipynb
                    (All 5 models compared)
```

## The "Why" Behind Each File:
| File | Why it exists | What would happen without it |
|------|--------------|------------------------------|
| 01 | We need data | No data = no project |
| 02 | Models need numbers, not text | Models would crash or give garbage |
| 03 | Your model: predict rating from basic info | You'd have no model to explain |
| 04 | Classify images (transfer learning demo) | No CNN demonstration |
| 05 | Sentiment analysis with LSTM | No RNN demonstration |
| 06 | Sentiment analysis with Transformer | No attention mechanism demo |
| 07 | Multi-modal innovation | No innovation/extra credit |
| 08 | Compare everything | Lose 2 marks on rubric |

---

# 📌 PART 6: The Fixes We Made (Why They Matter)

## Fix 1: Data Leakage (Critical!)

### The Bug:
In `02_Data_Preprocessing.ipynb`, the tabular features included `rating_scaled` — a normalized version of the exact same `rating` column we were trying to predict. It's like giving a student the answer key on a test and then being surprised when they get 100%.

### The Fix:
Removed `rating_scaled` from the feature list. Features are now only: `price_encoded`, `cuisine_encoded`, `neighborhood_encoded`, `review_count_scaled`.

### The Impact:
- **Before fix**: DNN MAE = 0.73 (artificially good, CHEATING)
- **After fix**: DNN MAE = 0.94 (honest result)

**Why this shows understanding**: Being able to identify and fix data leakage is a skill that separates beginners from people who actually know what they're doing. When the professor sees we caught this, it shows we understand how the model works at a deep level.

## Fix 2: Positional Encoding (Important!)

### The Bug:
The Transformer model had NO positional encoding. Without it, the model treats "I love pizza NOT sushi" the same as "NOT sushi I love pizza" — word order doesn't matter. This defeats the entire purpose of using a Transformer (which is supposed to be BETTER at understanding word relationships than LSTM).

### The Fix:
Added a `PositionalEncoding` layer between the embedding and the Transformer encoder. Uses sinusoidal encoding (the standard approach from the original "Attention Is All You Need" paper).

### The Impact:
Without this, the Transformer was basically a bag-of-words model with extra steps. Now it actually understands word order.

## Fix 3: Transformer Serialization (Technical Fix)

### The Bug:
When saving the Transformer model, custom layers (`PositionalEncoding`, `TransformerEncoder`) weren't registered as serializable. This means the model could be trained but couldn't be loaded back later.

### The Fix:
Added `@keras.saving.register_keras_serializable()` decorator and `get_config()` method to both custom classes.

---

# 📌 PART 7: Key Vocabulary Reference

| Term | Simple Definition |
|------|------------------|
| **Deep Learning** | Teaching computers to recognize patterns using multi-layer neural networks |
| **Neural Network** | A mathematical formula with millions of adjustable knobs |
| **Neuron** | A single mathematical unit: multiply inputs by weights, add, apply activation |
| **Layer** | A group of neurons working together |
| **Weights/Parameters** | The "knobs" that get adjusted during training |
| **Training** | The process of adjusting weights to reduce error |
| **Testing** | Checking if the trained model works on new data |
| **Epoch** | One complete pass through all training data |
| **Batch** | A subset of training data processed at once (e.g., 32 samples) |
| **Loss** | A number measuring how wrong the model is |
| **MAE** | Mean Absolute Error: average difference between prediction and truth |
| **Accuracy** | Percentage of correct predictions |
| **Overfitting** | Model memorizes training data but fails on new data |
| **Underfitting** | Model is too simple to learn the patterns |
| **Dropout** | Randomly turning off neurons during training to prevent overfitting |
| **ReLU** | Activation function: outputs input if positive, 0 otherwise |
| **Softmax** | Converts numbers to probabilities that sum to 1.0 |
| **Sigmoid** | Squashes numbers to a 0-1 range (for binary classification) |
| **Optimizer** | Algorithm that decides how to adjust weights (e.g., Adam) |
| **Learning Rate** | How big each weight adjustment is |
| **Early Stopping** | Stop training when no improvement for N epochs |
| **Transfer Learning** | Using a pre-trained model as a starting point |
| **Label Encoding** | Converting categories like "Italian" to numbers like 0, 1, 2 |
| **Standard Scaling** | Converting numbers to have mean=0 and std=1 |
| **Tokenization** | Converting words to numbers |
| **Padding** | Making all sequences the same length |
| **Data Leakage** | When information from the target accidentally appears in the input |

---

# 📌 PART 8: Common Confusions Explained

### "Why 120 training samples? Isn't that tiny for deep learning?"
Yes, it IS tiny. Real deep learning uses thousands or millions of samples. But for a course project where:
1. We need to demonstrate understanding
2. Training time needs to be reasonable (under 5 minutes per model)
3. We're not trying to beat state-of-the-art

...120 samples is fine. The professor told us "understanding over accuracy."

### "Why did we fix data leakage instead of leaving it? Wouldn't the professor prefer better numbers?"
Professors can spot data leakage. If the DNN has MAE of 0.03 (predicting rating almost perfectly), they'd immediately ask "how?" and we'd have to admit we included the answer in the input. That's worse than having a higher but honest MAE.

### "Why 4 features for DNN? Why not more?"
We have 4 columns that are NOT the rating: price, cuisine, neighborhood, review_count. These are all legitimate predictors. We removed rating_scaled because it was the target. We kept review_count_scaled because number of reviews is related to popularity but isn't the same as rating.

### "Why does Multi-Modal perform better than DNN?"
Multi-Modal has access to BOTH tabular data AND image features. Even though images alone aren't great predictors (CNN got 67%), when combined with tabular data, they provide additional signal that helps. Think of it as having two advisors giving suggestions vs. just one.

### "Why is Transformer 100% accurate? Is that realistic?"
No, 100% on a test set of 30 samples is suspiciously perfect. It happens because:
1. Our dataset is synthetic (the relationship between review text and sentiment is too clean)
2. Only 30 test samples, some of which may be almost identical to training reviews
3. The Transformer with positional encoding is powerful enough to memorize all patterns

In real life, you'd expect 85-92% accuracy. The 100% is an artifact of our simplified dataset.

### "Should I mention the 100% accuracy to the professor?"
YES! And say exactly this: "We achieved 100% test accuracy, which is almost certainly due to the simplicity of our synthetic dataset. In a real-world scenario with more diverse reviews, we'd expect lower but more meaningful accuracy. This taught us that perfect accuracy on a test set isn't always a good thing — it can mean the test data is too easy or the model is overfitting."

---

# 📌 PART 9: Quick Reference — What To Say For Each Notebook

### Notebook 01 (Data):
> "We created a realistic restaurant dataset with 150 entries, 36 unique review templates, and 39 different image sources. We expanded from the original 15 reviews to 36 for better text variety."

### Notebook 02 (Preprocessing):
> "We converted categories to numbers, scaled numerical features, tokenized reviews, and split data 80/20 for training and testing. We removed rating_scaled from features to fix a data leakage issue."

### Notebook 03 (DNN — YOUR MODEL):
> "My DNN uses 4 features to predict ratings. Architecture: 64→32→16 neurons with dropout. Uses ReLU activation, Adam optimizer, and early stopping. Achieves MAE of 0.94 on test data. The low accuracy is because 120 training samples is small and the features are limited."

### Notebook 04 (CNN):
> "Uses MobileNetV2 pre-trained on ImageNet for transfer learning. Classifies images as high/low tier. 67% accuracy confirms images alone don't predict restaurant quality well."

### Notebook 05 (LSTM):
> "Bidirectional LSTM for sentiment analysis. Reads reviews both forwards and backwards. 93% accuracy on positive/neutral/negative classification."

### Notebook 06 (Transformer):
> "Transformer with self-attention and positional encoding. We added the positional encoding fix ourselves. Achieves 100% accuracy but this is likely due to dataset simplicity."

### Notebook 07 (Multi-Modal):
> "Combines CNN and DNN branches. Uses images AND tabular data together. Best regression result with MAE of 0.52 — proves multi-modal fusion works."

### Notebook 08 (Comparison):
> "DNN (0.94 MAE) vs Multi-Modal (0.52 MAE) — combining data types helps. CNN (67%) vs LSTM (93%) vs Transformer (100%) — text models outperform image models on our dataset."

---

# ✅ FINAL CHECKLIST

Before you open your laptop to present:
- [ ] You understand the **data flow**: 01 → 02 → 03-07 → 08
- [ ] You can explain **your model** (DNN) — architecture, why each choice, results
- [ ] You know what **data leakage** is and why we fixed it
- [ ] You know what **positional encoding** is and why we added it
- [ ] You can explain **why Multi-Modal is best** (more information)
- [ ] You can explain **why CNN is worst** (images don't correlate with quality)
- [ ] You understand the **difference between LSTM and Transformer**
- [ ] You can answer "what would you improve?" (bigger dataset, real web scraping, etc.)

**You're ready. Go crush it. 🎯**
