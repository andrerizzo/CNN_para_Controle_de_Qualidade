# **Using Convolutional Neural Networks (CNNs) for Quality Control**

## **Overview**
This project implements an **Automated Quality Control** solution based on **Computer Vision**. Using **Convolutional Neural Networks (CNNs)** and **Transfer Learning**, the system detects and classifies defects in product images, replacing traditional manual inspection with a more efficient and accurate process.

The dataset used in this study:  
🔗 [Tomatoes Dataset (Kaggle)](https://www.kaggle.com/datasets/enalis/tomatoes-dataset)

The final model was able to identify the following tomato classes:
- 🍅 Green  
- 🍅 Ripe  
- 🍅 Old  
- 🍅 Damaged

---

## **Project Goals**
- Automate the quality inspection process  
- Detect and classify defects with high accuracy  
- Reduce time and errors related to manual inspection  

---

## **Technologies Used**
- **Language:** Python  
- **Main Libraries:**
  - TensorFlow / Keras
  - Scikit-learn
  - Pandas / NumPy
  - Matplotlib / Seaborn
- **Pretrained Model:** VGG-16 (Transfer Learning)
- **Development Environment:** Google Colab

---

## **Project Architecture**

### 1. Image Preprocessing
- Resizing to 224x224 pixels  
- Pixel normalization to the [0, 1] range  

### 2. CNN Modeling (VGG-16)
- Use of a pretrained model with frozen convolutional layers  
- Removal of original dense layers  
- Addition of new dense layers for classification (4 output neurons, softmax activation)  
- **Fine-tuning** of top layers

### 3. Training and Validation
- Dataset split: 60% Train, 20% Validation, 20% Test  
- Optimizer: Adam  
- Loss function: Categorical Crossentropy  
- Evaluation metrics: Accuracy and Loss

### 4. Results
- 📈 **Final Accuracy:** 98%  
- ⚡ **Average Inference Time:** ~20ms per image  
- ⏱️ **Estimated Time Reduction:** ~70% compared to manual inspection  

### 5. Next Steps
- Develop a simple GUI for use by non-technical users  
- Evaluate alternative pretrained models for improved performance

---

### 👨‍💻 About the Author

**André Rizzo**  
📊 Senior Data Scientist | Statistician | MBA in AI & Big Data (USP)  
🧠 Specialist in Machine Learning, Deep Learning, and Statistical Modeling  
📍 Rio de Janeiro, Brazil  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andrerizzo1)  
[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-181717?logo=github&logoColor=white)](https://github.com/andrerizzo)  
[![Email](https://img.shields.io/badge/Email-andrerizzo@hotmail.com-D14836?logo=gmail&logoColor=white)](mailto:andrerizzo@hotmail.com)
