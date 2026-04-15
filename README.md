# NeuroTwin: Neural Digital Twin Dashboard

NeuroTwin is a high-performance neural digital twin platform that utilizes LSTM-based Variational Autoencoders (VAEs) to create interactive virtual replicas of complex, time-series-driven systems.

## 🚀 Key Features

- **LSTM-VAE Modeling**: Sophisticated latent space representation of complex sequential data.
- **Real-time Anomaly Detection**: Proactive monitoring for system health and unexpected behavior.
- **Predictive Analytics**: Forecasting future system states with deep learning.
- **What-If Simulations**: Interactive modeling of hypothetical scenarios to forecast system behavior under varying operational parameters.
- **Modern Dashboard**: A sleek UI built with PySide6 for intuitive data visualization and control.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aryan12375/Neurotwin.git
   cd Neurotwin
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

To launch the NeuroTwin Dashboard, run:

```bash
python -m ui.app
```

Or run the main training and evaluation script:

```bash
python main.py
```

## 🏗️ Project Structure

- `models/`: Neural network architectures (LSTM-VAE).
- `training/`: Training loops and logic.
- `inference/`: Prediction and what-if simulation logic.
- `ui/`: PySide6 dashboard components and layouts.
- `utils/`: Data loaders and anomaly detection algorithms.
- `data/`: Sample datasets for training and testing.

---
Built with ❤️ by [aryan12375](https://github.com/aryan12375)
