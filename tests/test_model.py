from src.model import load_model

def test_model_prediction_shape():
    model = load_model()
    sample_input = [[1.2, 3.4, 5.6]]
    prediction = model.predict(sample_input)
    assert prediction.shape[0] == 1
