import pandas as pd
import numpy as np
import glob
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1️⃣ قراءة جميع CSV files
files = glob.glob("*.csv")

data_list = []
for file in files:
    print("Loading:", file)
    df = pd.read_csv(file)
    df.columns = df.columns.str.strip()  # remove spaces in column names
    data_list.append(df)

data = pd.concat(data_list, ignore_index=True)
print("Original Shape:", data.shape)

# 2️⃣ Balanced Sampling (max 20000 per class)
samples = []
for label in data["Label"].unique():
    subset = data[data["Label"] == label]
    if len(subset) > 20000:
        subset = subset.sample(20000, random_state=42)
    samples.append(subset)
data = pd.concat(samples).reset_index(drop=True)
print("After Sampling:", data.shape)

# 3️⃣ Encoding categorical features
X = data.drop("Label", axis=1)
y = data["Label"]

encoder = LabelEncoder()
for col in X.columns:
    if X[col].dtype == "object":
        X[col] = encoder.fit_transform(X[col])

# 4️⃣ Clean INF/NAN
X = X.replace([np.inf, -np.inf], np.nan)
mask = X.notnull().all(axis=1)
X = X[mask]
y = y[mask]

# 5️⃣ Convert Label to binary (optional, stronger result)
y = y.apply(lambda x: 0 if x == "BENIGN" else 1)

# 6️⃣ Scaling
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 7️⃣ Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 8️⃣ SVM Model
model = SVC(kernel="rbf", C=2, gamma="scale")  # RBF kernel gives strong results
model.fit(X_train, y_train)

# 9️⃣ Prediction & Evaluation
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))
print("\nClassification Report:\n", classification_report(y_test, pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, pred))