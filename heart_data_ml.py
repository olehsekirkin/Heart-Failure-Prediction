import numpy as np
import pandas as pd
import snowflake.connector
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import xgboost as xgb

X = df.drop(['patient_id', 'death_event'], axis=1)  # Excluding 'patient_id'
y = df['death_event']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Logistic Regression model
log_reg_model = LogisticRegression(max_iter=1000)
log_reg_model.fit(X_train_scaled, y_train)

# Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train)

# Gradient Boosting Machine (XGBoost)
xgb_model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
xgb_model.fit(X_train_scaled, y_train)

# Support Vector Machine
svm_model = SVC()
svm_model.fit(X_train_scaled, y_train)

predictions_log_reg = log_reg_model.predict(X_test_scaled)
predictions_rf = rf_model.predict(X_test_scaled)
predictions_xgb = xgb_model.predict(X_test_scaled)
predictions_svm = svm_model.predict(X_test_scaled)

accuracy_log_reg = accuracy_score(y_test, predictions_log_reg)
accuracy_rf = accuracy_score(y_test, predictions_rf)
accuracy_xgb = accuracy_score(y_test, predictions_xgb)
accuracy_svm = accuracy_score(y_test, predictions_svm)

print(f"Logistic Regression Model Accuracy: {accuracy_log_reg}")
print(f"Random Forest Classifier Accuracy: {accuracy_rf}")
print(f"Gradient Boosting Machine (XGBoost) Accuracy: {accuracy_xgb}")
print(f"Support Vector Machine Accuracy: {accuracy_svm}")
