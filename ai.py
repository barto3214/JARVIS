import numpy as np
from sklearn.linear_model import LinearRegression

# Dane wejściowe (godziny nauki)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
# Wyniki na egzaminie
y = np.array([2, 4, 5, 4, 5])

# Tworzymy model regresji liniowej
model = LinearRegression()

# Trenujemy model na danych
model.fit(X, y)

# Przewidujemy wynik dla 6 godzin nauki
X_new = np.array([[6]])
y_pred = model.predict(X_new)

print(f"Przewidywana wartość dla 6 godzin nauki: {y_pred[0]}")
#--------------------------------------------------------------------------#
import numpy as np
from sklearn.linear_model import LinearRegression

# Dane wejściowe (godziny nauki)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
# Wyniki na egzaminie
y = np.array([2, 4, 5, 4, 5])

# Tworzymy model regresji liniowej
model = LinearRegression()

# Trenujemy model na danych
model.fit(X, y)

# Pobieramy współczynniki
w0 = model.intercept_
w1 = model.coef_[0]

print(f"w0 (intercept): {w0}")
print(f"w1 (slope): {w1}")
