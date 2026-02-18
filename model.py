import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv('dataset.csv')
X = data[['area']]
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Changed model to Decision Tree
model = DecisionTreeRegressor()
model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)
print("Decision Tree MAE:", mean_absolute_error(y_test, predictions))