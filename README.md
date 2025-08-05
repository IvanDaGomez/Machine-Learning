# Machine Learning repository

## Overview

With this repository I've created and learned about neural network architectures, including Transformers, Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and Reinforcement Learning models. Additionally, it explores QR code generation and augmentation techniques.

## Project Structure

```
NN/
├── firstTransformer/         # Transformer model implementation
│   ├── data/                 # Dataset files (English-Spanish translations, vocab)
│   ├── mixed/                # Transformer utilities and components
│   │   ├── attention/
│   │   ├── utils/
│   │   ├── decoder.py
│   │   ├── embedding.py
│   │   ├── encoder.py
│   │   ├── feed_forward.py
│   │   ├── layer_normalization.py
│   │   ├── positional_encoding.py
│   │   ├── transformer.py
│   ├── main.py               # Transformer model execution
│
├── models/                   # Trained models and architecture files
├── text/                     # Training checkpoints and text processing
├── weights/                  # Saved weights for different models
│   ├── firstConvolutional...
│   ├── firstRecurrentWeights
│
├── QRs/                      # QR code related scripts
├── .gitignore                # Ignore unnecessary files
├── firstClassifier.py        # Neural network classifier
├── firstData.py              # Data preprocessing script
├── firstTry.py               # Initial experiment script
├── QR.py                     # QR code generator
├── README.md                 # Project documentation
```

## Features

- **Transformer Model**: Implements self-attention, positional encoding, and multi-head attention for NLP tasks.
- **Convolutional and Recurrent Networks**: Includes CNNs for image processing and RNNs for sequential data analysis.
- **Reinforcement Learning**: Experiments with reinforcement learning techniques.
- **QR Code Processing**: QR code generation and augmentation.

## Datasets

- **English-Spanish translation dataset** stored in `data/`
- Vocabulary JSON file: `data/vocab.json`

## Future Improvements

- Implement BERT-based NLP models
- Expand reinforcement learning applications
- Enhance dataset preprocessing for better training results

## License

This project is licensed under the MIT License.
# AI
