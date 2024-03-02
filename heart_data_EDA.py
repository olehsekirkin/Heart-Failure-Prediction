from sqlalchemy import create_engine
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pymysql

engine = create_engine('mysql+pymysql://SQLUSERNAME:SQLPASSWORD*@localhost:3306/heart_prediction')

heart_data = pd.read_sql_table('heart_data', engine)

# Age Distribution plot

hist_data = [heart_data['age'].values]
group_labels = ['age']
fig = ff.create_distplot(hist_data, group_labels)
fig.update_layout(title_text='Age Distribution plot')
fig.show()

# Gender wise Age Spread

fig = px.box(heart_data, x='sex', y='age', points='all')
fig.update_layout(title_text='Gender wise Age Spread - Male = 1 Female = 0')
fig.show()

# Analysis in Age on Survival Status

surv = heart_data[heart_data['death_event']==0]['age']
not_surv = heart_data[heart_data['death_event']==1]['age']
hist_data = [surv, not_surv]
group_labels = ['Survived', 'Not Survived']
fig = ff.create_distplot(hist_data, group_labels, bin_size=0.5)
fig.update_layout(title_text='Analysis in Age on Survival Status')
fig.show()

# Analysis in Age and Gender on Survival Status

fig = px.violin(heart_data, y='age', x='sex', color='death_event', box=True, points='all', hover_data=heart_data.columns)
fig.update_layout(title_text='Analysis in Age and Gender on Survival Status')
fig.show()

# Analysis in age and smoking on survival status

fig = px.violin(heart_data, y='age', x='smoking', color='death_event', box=True, points='all', hover_data=heart_data.columns)
fig.update_layout(title_text='Analysis in Age and Smoking on Survival Status')
fig.show()

# Analysis on age and diabetes on survival status

fig = px.violin(heart_data, y='age', x='diabetes', color='death_event', box=True, points='all', hover_data=heart_data.columns)
fig.update_layout(title_text='Analysis in Age and Diabetes on Survival Status')
fig.show()

# Analysis on creatinine phosphokinase, ejection fraction, platelets, etc on survival status

fig = px.histogram(heart_data, x='creatinine_phosphokinase', color='death_event', marginal='violin', hover_data=heart_data.columns)
fig.show()

fig = px.histogram(heart_data, x='ejection_fraction', color='death_event', marginal='violin', hover_data=heart_data.columns)
fig.show()

fig = px.histogram(heart_data, x='platelets', color='death_event', marginal='violin', hover_data=heart_data.columns)
fig.show()

fig = px.histogram(heart_data, x='serum_creatinine', color='death_event', marginal='violin', hover_data=heart_data.columns)
fig.show()

fig = px.histogram(heart_data, x='serum_sodium', color='death_event', marginal='violin',hover_data=heart_data.columns)
fig.show()

labels = ['No Diabetes','Diabetes']
diabetes_yes = heart_data[heart_data['diabetes']==1]
diabetes_no = heart_data[heart_data['diabetes']==0]
diabetes_yes_survi = diabetes_yes[heart_data['death_event']==0]
diabetes_yes_not_survi = diabetes_yes[heart_data['death_event']==1]
diabetes_no_survi = diabetes_no[heart_data['death_event']==0]
diabetes__no_not_survi = diabetes_no[heart_data['death_event']==1]

labels = ['Diabetes Yes - Survived','Diabetes Yes - Not Survived', 'Diabetes NO - Survived', 'Diabetes NO - Not Survived']
values = [len(diabetes_yes[heart_data['death_event']==0]),len(diabetes_yes[heart_data['death_event']==1]),
         len(diabetes_no[heart_data['death_event']==0]),len(diabetes_no[heart_data['death_event']==1])]
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
fig.update_layout(
    title_text='Analysis on Survival - Diabetes')
fig.show()

# Heatmap

plt.figure(figsize=(10,10))
sns.heatmap(heart_data.corr(), vmin=-1, cmap='coolwarm', annot=True)
plt.show()
