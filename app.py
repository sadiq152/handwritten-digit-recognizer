from flask import Flask
from flask import Flask, request, jsonify, render_template
import torch
from model import MyNN
app = Flask(__name__)
model = MyNN()
model.load_state_dict(torch.load("MNIST_model.pth"))
model.eval()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/route', methods=['POST'])
def predict():
    data = request.get_json()
    tensor = torch.tensor(data, dtype=torch.float32).reshape(1, 1, 28, 28)
    with torch.no_grad():
        output = model(tensor)
        predicted = torch.argmax(output, dim=1)
    print(predicted.item())
    return jsonify({"predicted": predicted.item()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
