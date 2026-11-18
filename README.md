<div align="center">

# 😊 Facial Emotion Recognition

**Real-time facial emotion detection using Deep Learning & OpenCV**

[![Author](https://img.shields.io/badge/Author-Takwa%20Hafyen-2E86AB?style=flat-square&logo=github&logoColor=white)](https://github.com/takwahafyen)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Takwa%20Hafyen-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/takwa-hafyen-472264282)
[![Gmail](https://img.shields.io/badge/Gmail-takwa.hafyen@gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:takwa.hafyen@gmail.com)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.10%2B-orange?logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-2.10%2B-red?logo=keras&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.6%2B-green?logo=opencv&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A Convolutional Neural Network (CNN) trained to classify **7 human emotions** from facial images in real-time, enhanced with a **real-time psychological conseil panel** for each detected emotion.

</div>

---

## ✨ Key Feature — Psychological Conseil System

For every emotion detected, a **live sidebar panel** renders instantly with:

| Detected | Conseil | Mindset Tip |
|----------|---------|-------------|
| 😠 Angry | Take 3 deep breaths · Count to 10 · Step away | *Anger is energy — redirect it* |
| 🤢 Disgust | Acknowledge it · Ask if it's worth your energy · Set a boundary | *Your values are speaking to you* |
| 😨 Fear | 5-4-3-2-1 grounding · Box breathing (4-4-4) | *Fear is a signal, not a stop sign* |
| 😄 Happy | Enjoy fully · Share it · Write it down | *Happiness shared is happiness doubled* |
| 😐 Neutral | Use this clarity to plan · Check in with yourself | *Peace is productive* |
| 😢 Sad | It's okay to feel sad · Talk to someone you trust | *Every storm runs out of rain* |
| 😲 Surprise | Pause · Breathe · Process before reacting | *Life is full of unexpected gifts* |

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
│   ├── emotions_advice.py                 # 🆕 Psychological conseil engine (7 emotions)
│   ├── model.py                           # CNN architecture definition
│   ├── train.py                           # Training script
│   ├── predict.py                         # Single image prediction
│   └── realtime.py                        # 🆕 Webcam detection + conseil sidebar
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
git clone https://github.com/takwahafyen/facial-emotion-recognition.git
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

Made with ❤️ by [Takwa Hafyen](https://github.com/takwahafyen)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/takwa-hafyen-472264282)
[![Gmail](https://img.shields.io/badge/Email-Contact-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:takwa.hafyen@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/takwahafyen)

⭐ Star this repo if you found it helpful!

</div>
