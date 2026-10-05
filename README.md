# handwritten-digit-recognizer
Handwritten digit recognition using a PyTorch multilayer perceptron (MLP)
featuring an interactive drawing interface, image preprocessing visualization
and responsive desktop/mobile layouts.
An end to end handwritten digit recognition application build with 
Pytorch.

The application allows users to draw a digit and see the model's prediction
while also visualizing the image processing pipeline.

## Demo
Desktop version 👉
https://github.com/user-attachments/assets/a78a4bc4-2151-4eec-99b2-004959b0eed4

Mobile version 👉
https://github.com/user-attachments/assets/7d7d8781-cd07-4a8b-af56-cdef11a652b7

## Screenshot

### Desktop
![Desktop UI](<img width="1491" height="955" alt="image" src="https://github.com/user-attachments/assets/8da2a074-0566-49c8-bfb3-36dcdd8ecd00" />)

### Mobile
![Mobile UI](<img width="817" height="1599" alt="WhatsApp Image 2026-10-05 at 10 27 59 PM" src="https://github.com/user-attachments/assets/79cea5c6-01fa-4d73-ac6f-66089a49b74e" />)

## Features
- Handwritten digit recognition
- Interactive drawing canvas
- Real-time image preprocessing visualization
- Desktop interface
- Responsive mobile interface
- PyTorch-based model interface

## How it works
 
The application processes the user's drawing through several stages
before passing it to the Model:

Drawing
→ Downscaling
→ Cropping
→ Padding
→ Model Input
→ Prediction

## Image Preprocessing

The input drawn by the user is transformed to match the format
expected by the model.

1. **Main Canvas** — User draws the digit.
2. **Downscaling** — The image is resized.
3. **Cropping** — Unnecessary empty regions are removed.
4. **Padding** — The digit is centered within the required input dimensions.

## Model

The model is a Multilayer Perceotron implemented using PyTorch.

### Architecture
Input
👉 Flatten
👉 Layer1
👉 ReLU
👉 Dropout
👉 Layer2
👉 ReLU
👉 Dropout
👉 ReLU
👉 Layer3
👉 Fully Connected
→ Output


## Training

**Dataset:** MNIST  
**Framework:** PyTorch  
**Loss Function:** [CrossEntropyLoss]  
**Optimizer:** [Adam]  
**Epochs:** [50]  
**Batch Size:** [64]  
**Test Accuracy:** [93%]

## Tech Stack

- Python
- PyTorch
- html, css, javascript
- Git / GitHub

## Running Locally

```bash
git clone https://github.com/sadiq152/handwritten-digit-recognizer.git

python app.py
then you can join locally hosted server
