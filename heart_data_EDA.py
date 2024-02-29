import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objs as go

pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

heart_data = pd.read_csv("C:\\Users\\olehs\\Desktop\\heart_failure_clinical_records_dataset.csv")
print(heart_data.head())

# Are age and sex indicators for death event?

hist_data=[heart_data['age'].values]
group_labels=['age']
fig = ff.create_distplot(hist_data, group_labels)
fig.update_layout(
    title_text='Age Distribution plot')
fig.show()

fig = px.box(heart_data, x='sex', y='age', points='all')
fig.update_layout(
    title_text='Gender wise Age Spread - Male = 1 Female =0')
fig.show()

# Analysis in age on survival status

surv = heart_data[heart_data['DEATH_EVENT']==0]['age']
not_surv = heart_data[heart_data['DEATH_EVENT']==1]['age']
hist_data = [surv,not_surv]
group_labels = ['Survived', 'Not Survived']
fig = ff.create_distplot(hist_data, group_labels, bin_size=0.5)
fig.update_layout(
    title_text='Analysis in Age on Survival Status')
fig.show()

# Analysis in age and gender on survival status

fig = px.violin(heart_data, y='age', x='sex', color='DEATH_EVENT', box=True, points='all', hover_data=heart_data.columns)
fig.update_layout(title_text='Analysis in Age and Gender on Survival Status')
fig.show()

# Analysis in age and smoking on survival status

fig = px.violin(heart_data, y='age', x='smoking', color='DEATH_EVENT', box=True, points='all', hover_data=heart_data.columns)
fig.update_layout(title_text='Analysis in Age and Smoking on Survival Status')
fig.show()

# Analysis on age and diabetes on survival status

fig = px.violin(heart_data, y='age', x='diabetes', color='DEATH_EVENT', box=True, points='all', hover_data=heart_data.columns)
fig.update_layout(title_text='Analysis in Age and Diabetes on Survival Status')
fig.show()

# Analysis on creatinine phosphokinase, ejection fraction, platelets, etc on survival status

fig = px.histogram(heart_data, x='creatinine_phosphokinase', color='DEATH_EVENT', marginal='violin', hover_data=heart_data.columns)
fig.show()

fig = px.histogram(heart_data, x='ejection_fraction', color='DEATH_EVENT', marginal='violin', hover_data=heart_data.columns)
fig.show()

fig = px.histogram(heart_data, x='platelets', color='DEATH_EVENT', marginal='violin', hover_data=heart_data.columns)
fig.show()

fig = px.histogram(heart_data, x='serum_creatinine', color='DEATH_EVENT', marginal='violin', hover_data=heart_data.columns)
fig.show()

fig = px.histogram(heart_data, x='serum_sodium', color='DEATH_EVENT', marginal='violin',hover_data=heart_data.columns)
fig.show()

# Analysis on diabetes on survival status

labels = ['No Diabetes','Diabetes']
diabetes_yes = heart_data[heart_data['diabetes']==1]
diabetes_no = heart_data[heart_data['diabetes']==0]
diabetes_yes_survi = diabetes_yes[heart_data["DEATH_EVENT"]==0]
diabetes_yes_not_survi = diabetes_yes[heart_data["DEATH_EVENT"]==1]
diabetes_no_survi = diabetes_no[heart_data["DEATH_EVENT"]==0]
diabetes__no_not_survi = diabetes_no[heart_data["DEATH_EVENT"]==1]

labels = ['Diabetes Yes - Survived','Diabetes Yes - Not Survived', 'Diabetes NO - Survived', 'Diabetes NO - Not Survived']
values = [len(diabetes_yes[heart_data["DEATH_EVENT"]==0]),len(diabetes_yes[heart_data["DEATH_EVENT"]==1]),
         len(diabetes_no[heart_data["DEATH_EVENT"]==0]),len(diabetes_no[heart_data["DEATH_EVENT"]==1])]
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
fig.update_layout(
    title_text="Analysis on Survival - Diabetes")
fig.show()

# Heatmap

plt.figure(figsize=(10,10))
sns.heatmap(heart_data.corr(), vmin=-1, cmap='coolwarm', annot=True);
plt.show()