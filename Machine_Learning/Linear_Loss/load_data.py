from sklearn.datasets import load_diabetes
from sklearn.utils import shuffle

diabetes = load_diabetes()

data, target = diabetes.data, diabetes.target

data, target = shuffle(data, target, random_state=42)

