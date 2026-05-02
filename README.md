🛡️ DDoS Detection — SVM Classifier
Détection d'attaques réseau (DDoS, PortScan, Brute Force...) avec un modèle SVM kernel RBF, entraîné sur le dataset CIC-IDS 2017.

🚀 Démarrage rapide
bashpip install -r requirements.txt
python ddos_svm.py

Ouvrir ddos_svm_dashboard_v2.html dans le navigateur pour visualiser les résultats.

📊 Résultats

Métrique            Valeur 
Accuracy            97.42 %
F1-Score (Attack)   98 %
Recall (Attack)     99.4 %
False Negatives     117
False Positives     500

⚙️ Configuration du modèle
pythonSVC(kernel="rbf", C=2, gamma="scale")

78 features réseau extraites par CICFlowMeter
119 616 échantillons — 80% train / 20% test
Classification binaire : BENIGN = 0 / ATTACK = 1


📁 Structure
├── ddos_svm.py
├── requirements.txt
├── ddos_svm_dashboard_v2.html
└── data/
    ├── Friday-Afternoon-DDos.csv
    ├── Friday-Afternoon-PortScan.csv
    ├── Friday-Morning.csv
    ├── Monday-WorkingHours.csv
    ├── Thursday-Afternoon-Infilteration.csv
    ├── Thursday-Morning-WebAttacks.csv
    ├── Tuesday-WorkingHours.csv
    └── Wednesday-workingHours.csv

🗃️ Dataset
CIC-IDS 2017 — Canadian Institute for Cybersecurity
2,8M flux réseau capturés sur 5 jours : DDoS, DoS, PortScan, Brute Force, Web Attacks, Infiltration, Botnet.
🔗 https://www.unb.ca/cic/datasets/ids-2017.html
