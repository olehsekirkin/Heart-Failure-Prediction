import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X = df.drop(['death_event'], axis=1)  # Adjust based on your column names
y = df['death_event']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

log_reg_model = LogisticRegression(max_iter=1000)
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
gb_model = GradientBoostingClassifier(random_state=42)
svm_model = SVC()

log_reg_model.fit(X_train_scaled, y_train)
rf_model.fit(X_train_scaled, y_train)
gb_model.fit(X_train_scaled, y_train)
svm_model.fit(X_train_scaled, y_train)

predictions_log_reg = log_reg_model.predict(X_test_scaled)
predictions_rf = rf_model.predict(X_test_scaled)
predictions_gb = gb_model.predict(X_test_scaled)
predictions_svm = svm_model.predict(X_test_scaled)

accuracy_log_reg = accuracy_score(y_test, predictions_log_reg)
accuracy_rf = accuracy_score(y_test, predictions_rf)
accuracy_gb = accuracy_score(y_test, predictions_gb)
accuracy_svm = accuracy_score(y_test, predictions_svm)

print(f"Logistic Regression Model Accuracy: {accuracy_log_reg}")
print(f"Random Forest Classifier Accuracy: {accuracy_rf}")
print(f"Gradient Boosting Classifier Accuracy: {accuracy_gb}")
print(f"Support Vector Machine Accuracy: {accuracy_svm}")
