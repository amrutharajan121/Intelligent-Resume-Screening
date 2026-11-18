import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# --------------------------------------------------
# 1. LOAD DATASET
# --------------------------------------------------

df = pd.read_csv(
    "notebooks/resume_dataset.csv",
    encoding="utf-8",
    engine="python"
)

print("Dataset loaded successfully!")
print("Total resumes:", len(df))


# --------------------------------------------------
# 2. REMOVE EMPTY VALUES
# --------------------------------------------------

df = df.dropna(subset=["resume", "role"])

print("\nAfter removing empty rows:", len(df))


# --------------------------------------------------
# 3. CHECK ROLES
# --------------------------------------------------

print("\nRoles in dataset:")
print(df["role"].value_counts())


# --------------------------------------------------
# 4. PREPARE DATA
# --------------------------------------------------

X = df["resume"].astype(str)
y = df["role"].astype(str)


# --------------------------------------------------
# 5. TF-IDF
# --------------------------------------------------

tfidf = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2)
)

X_tfidf = tfidf.fit_transform(X)


# --------------------------------------------------
# 6. SPLIT DATA
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# --------------------------------------------------
# 7. TRAIN MODEL
# --------------------------------------------------

model = LogisticRegression(
    max_iter=2000
)

model.fit(X_train, y_train)


# --------------------------------------------------
# 8. PREDICTION
# --------------------------------------------------

y_pred = model.predict(X_test)


# --------------------------------------------------
# 9. EVALUATION
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\n================================")
print("MODEL TRAINING COMPLETED")
print("================================")

print("\nAccuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# --------------------------------------------------
# 10. SAVE MODEL
# --------------------------------------------------

joblib.dump(
    model,
    "notebooks/resume_role_model.pkl"
)

joblib.dump(
    tfidf,
    "notebooks/tfidf_vectorizer.pkl"
)


# --------------------------------------------------
# 11. DISPLAY SUPPORTED ROLES
# --------------------------------------------------

print("\n================================")
print("SUPPORTED ROLES")
print("================================")

for role in model.classes_:
    print("-", role)


print("\n================================")
print("FILES SAVED SUCCESSFULLY")
print("================================")

print("resume_role_model.pkl")
print("tfidf_vectorizer.pkl")