## 🔍 Overview
![Capture](https://github.com/user-attachments/assets/48e9dc4b-85b8-495d-9fd3-fa06bff89f28)

**MaxGlaViT** is an advanced lightweight Vision Transformer model tailored for the early diagnosis of glaucoma stages from fundus images. Leveraging state-of-the-art attention mechanisms and convolutional modules, MaxGlaViT achieves unprecedented accuracy and efficiency.

---

## ✨ Key Features

- 🧠 **Enhanced Attention Mechanisms**:
  - Integrates **Efficient Channel Attention (ECA)** for improved feature recalibration in the stem block.
  - Utilizes **ConvNeXtV2** blocks in MaxViT architecture for advanced feature extraction.

- ⚡ **Optimized Model Design**:
  - Lightweight architecture with only **6.2M parameters**.
  - Scaled MaxViT architecture ensures computational efficiency while maintaining robust performance.

- 🎯 **High-Performance Metrics**:
  - Achieves **92.03% accuracy**, **92.13% F1-score**, and **87.12% Cohen’s kappa** on the HDV1 dataset.

---

## 📂 Dataset

The HDV1 dataset was utilized for evaluating the MaxGlaViT model. It includes **1,542 fundus images** categorized into three glaucoma stages:

- 👁️ **Advanced Glaucoma**: 467 images
- 👁️ **Early Glaucoma**: 289 images
- 👁️ **Normal (Healthy)**: 786 images

| **Class Name**  | **Training** | **Validation** | **Testing** | **Total** |
|------------------|--------------|----------------|-------------|-----------|
| Advanced         | 228          | 98             | 141         | 467       |
| Early            | 141          | 61             | 87          | 289       |
| Normal           | 385          | 165            | 236         | 786       |
| **Total**        | **754**      | **324**        | **464**     | **1542**  |

---

## 📊 Experimental Results

MaxGlaViT was benchmarked against **40 CNN** and **40 ViT models**. Below are some highlights:

### 📈 CNN Models

- **Xception**: Accuracy of **84.70%**, F1-score of **84.97%**
- **EfficientNetB6**: Accuracy of **84.91%**, F1-score of **85.25%**

### 🧠 ViT Models

- **MaxViT-Tiny**: Accuracy of **86.42%**, F1-score of **86.53%**
- **GCViT-Tiny**: Accuracy of **83.62%**, F1-score of **83.78%**

### 🏆 MaxGlaViT Performance

| **Model**                      | **Accuracy (%)** | **Precision (%)** | **Recall (%)** | **F1-Score (%)** | **Cohen’s Kappa** |
|--------------------------------|------------------|-------------------|----------------|------------------|-----------------|
| MaxViT-Scaled                 | 87.93            | 88.10             | 87.93          | 87.96            | 80.51           |
| MaxViT-Scaled + ECA           | 89.01            | 89.30             | 89.01          | 89.06            | 82.32           |
| MaxViT-Scaled + ConvNeXtV2    | 89.87            | 90.23             | 89.87          | 89.93            | 83.65           |
| **MaxGlaViT**                 | **92.03**        | **92.33**         | **92.03**      | **92.13**        | **87.12**       |

---

## 🛠️ Installation

### Prerequisites

- 🐍 **Python**: 3.11+
- 🧠 **TensorFlow**: 2.14.0
- 🛠️ **Keras**: 2.11.4
- ⚙️ **CUDA**: 12.7

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/MaxGlaViT.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧑‍💻 Meet the Team

### 👨‍🏫 Prof. Dr. Şakir Taşdemir
- **Affiliation**: Selçuk University, Computer Engineering Department
- **Expertise**: Deep learning, Vision Transformers, Medical Imaging
- 📧 **Email**: [stasdemir@selcuk.edu.tr](mailto:stasdemir@selcuk.edu.tr)

### 👩‍🏫 Assist. Prof. Dr. Kübra Uyar
- **Affiliation**: Alanya Alaaddin Keykubat University, Computer Engineering Department
- **Expertise**: Machine Learning, Computer Vision
- 📧 **Email**: [kubra.uyar@alanya.edu.tr](mailto:kubra.uyar@alanya.edu.tr)

### 👨‍🎓 Mustafa Yurdakul (PhD Candidate)
- **Affiliation**: Kırıkkale University, Computer Engineering Department
- **Expertise**: Vision Transformers, Attention Mechanisms
- 📧 **Email**: [mustafayurdakul@kku.edu.tr](mailto:mustafayurdakul@kku.edu.tr)

---

## 📬 Contact

For questions or collaborations, reach out to Mustafa Yurdakul at [mustafayurdakul@kku.edu.tr](mailto:mustafayurdakul@kku.edu.tr).

---

## 📝 License

This project is licensed under the **MIT License**. See the LICENSE file for details.

---

## 🤝 Acknowledgments

Special thanks to the contributors of the HDV1 dataset and the deep learning research community.

