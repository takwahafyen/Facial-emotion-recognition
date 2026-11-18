<div align="center">

# 😊 Facial Emotion Recognition

**Real-time facial emotion detection using Deep Learning & OpenCV**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.10%2B-orange?logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-2.10%2B-red?logo=keras&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.6%2B-green?logo=opencv&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A Convolutional Neural Network (CNN) trained to classify **7 human emotions** from facial images in real-time using a webcam or static images.

</div>

---

## 🎯 Emotions Detected

| Label | Emotion |
|-------|---------|
| 😠 | Angry |
| 🤢 | Disgust |
| 😨 | Fear |
| 😄 | Happy |
| 😐 | Neutral |
| 😢 | Sad |
| 😲 | Surprise |

---

## 🏗️ Project Structure

```
facial-emotion-recognition/
│
├── notebooks/
│   └── facial_emotion_recognition.ipynb   # Training & exploration notebook
│
├── src/
│   ├── model.py                           # CNN architecture definition
│   ├── train.py                           # Training script
│   ├── predict.py                         # Single image prediction
│   └── realtime.py                        # Webcam real-time detection
│
├── models/                                # Saved model weights (not tracked by git)
│   └── emotion_model.h5
│
├── data/                                  # Dataset (not tracked by git)
│   ├── train/
│   │   ├── angry/
│   │   ├── happy/
│   │   └── ...
│   └── test/
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## ⚙️ Tech Stack

- **Deep Learning:** TensorFlow / Keras
- **Computer Vision:** OpenCV
- **Data Processing:** NumPy, Pandas, scikit-learn
- **Visualization:** Matplotlib, Seaborn
- **Environment:** Jupyter Notebook / Python 3.8+

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/facial-emotion-recognition.git
cd facial-emotion-recognition
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the dataset

This project uses the **FER2013** dataset (35,887 grayscale 48×48 images).

> Download from [Kaggle — FER2013](https://www.kaggle.com/datasets/msambare/fer2013) and place it inside the `data/` folder.

```
data/
├── train/
│   ├── angry/
│   ├── disgust/
│   ├── fear/
│   ├── happy/
│   ├── neutral/
│   ├── sad/
│   └── surprise/
└── test/
    └── ...
```

### 5. Train the model

```bash
python src/train.py
```

### 6. Run real-time emotion detection (webcam)

```bash
python src/realtime.py
```

### 7. Or explore the notebook

```bash
jupyter notebook notebooks/facial_emotion_recognition.ipynb
```

---

## 🧠 Model Architecture

```
Input (48x48 Grayscale)
        ↓
Conv2D(32) → BatchNorm → ReLU → MaxPool → Dropout
        ↓
Conv2D(64) → BatchNorm → ReLU → MaxPool → Dropout
        ↓
Conv2D(128) → BatchNorm → ReLU → MaxPool → Dropout
        ↓
Flatten → Dense(256) → Dropout(0.5)
        ↓
Dense(7, Softmax) → Emotion Class
```

---

## 📊 Results

| Metric | Value |
|--------|-------|
| Training Accuracy | ~92% |
| Validation Accuracy | ~65% |
| Dataset | FER2013 (35,887 images) |
| Epochs | 50 |
| Optimizer | Adam (lr=0.0001) |

> *Note: FER2013 is a challenging dataset — human-level accuracy is ~65-70%.*

---

## 🗺️ Roadmap

- [x] CNN baseline model
- [x] Grayscale preprocessing pipeline
- [x] Real-time webcam inference
- [ ] Transfer learning with MobileNetV2
- [ ] Streamlit / Gradio web app
- [ ] Hugging Face Spaces deployment
- [ ] Multi-face detection support

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ and Python

⭐ Star this repo if you found it helpful!

</div>
