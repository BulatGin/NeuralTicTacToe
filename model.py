import pandas
from sklearn import preprocessing
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

MODEL_PERSIST_FILE_NAME = 'model.pkl'


def prepare_data():
    # loading data
    data = pandas.read_csv('dataset_50_tic-tac-toe.csv')
    x = data.iloc[1:, 0:9]
    y = data.iloc[1:, 9:10]
    print('Data set loaded')
    # x dummy coding
    x = pandas.get_dummies(x, columns=["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"])
    # apply labels for y
    le = preprocessing.LabelEncoder()
    y = y.apply(le.fit_transform)
    # split train and test
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
    # scaling
    scaler = StandardScaler()
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)
    print('Data prepared')
    return x_train, x_test, y_train, y_test


def test_model(model, x_test, y_test):
    predictions = model.predict(x_test)

    print(confusion_matrix(y_test, predictions))
    print(classification_report(y_test, predictions))


def train_new_model():
    x_train, x_test, y_train, y_test = prepare_data()

    mlp = MLPClassifier(hidden_layer_sizes=(27,), max_iter=10000)
    mlp.fit(x_train, y_train.values.ravel())

    test_model(mlp, x_test, y_test)

    return mlp


def get_model():
    try:
        model = joblib.load(MODEL_PERSIST_FILE_NAME)
        return model
    except FileNotFoundError:
        model = train_new_model()
        joblib.dump(model, MODEL_PERSIST_FILE_NAME)
        return model
