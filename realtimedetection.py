import cv2
import numpy as np
from keras.models import load_model

# Charger le modèle Keras
model = load_model("facialemotionmodel.h5")

# Charger le fichier de cascade haar pour la détection de visage
haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)

# Définir une fonction pour extraire les caractéristiques de l'image
def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 48, 48, 1)
    return feature / 255.0

# Capturer la vidéo depuis la webcam
webcam = cv2.VideoCapture(0)

# Dictionnaire des étiquettes d'émotions
labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}

while True:
    # Lire une image depuis la webcam
    i, im = webcam.read()
    
    # Vérifier si l'image a été correctement lue
    if im is not None:
        # Convertir l'image en niveaux de gris
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        
        # Détecter les visages dans l'image
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        # Parcourir les visages détectés
        for (p, q, r, s) in faces:
            # Extraire le visage de l'image en niveaux de gris
            face_image = gray[q:q+s, p:p+r]
            
            # Dessiner un rectangle autour du visage sur l'image originale
            cv2.rectangle(im, (p, q), (p+r, q+s), (255, 0, 0), 2)
            
            # Redimensionner l'image du visage à la taille attendue par le modèle
            face_image = cv2.resize(face_image, (48, 48))
            
            # Extraire les caractéristiques du visage pour la prédiction
            features = extract_features(face_image)
            
            # Faire la prédiction d'émotion
            pred = model.predict(features)
            
            # Obtenir l'étiquette prédite de l'émotion
            prediction_label = labels[pred.argmax()]
            
            # Ajouter l'étiquette prédite sur l'image
            cv2.putText(im, str(prediction_label), (p-10, q-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))
        
        # Afficher l'image avec les visages détectés et les étiquettes prédites
        cv2.imshow("Output", im)
        
        # Attendre l'appui sur la touche 'Esc' pour quitter
        if cv2.waitKey(1) == 27:
            break

# Libérer la capture vidéo et fermer toutes les fenêtres
webcam.release()
cv2.destroyAllWindows()
