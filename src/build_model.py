'''
@file: build_model.py
@description: Módulo de construção e compilação do modelo CNN com Transfer Learning (VGG16)
@author: André Rizzo
'''

import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalFocalCrossentropy

def build_model(input_shape=(224, 224, 3), num_classes=4):
    '''
    Constrói o modelo CNN com base no VGG16 pré-treinado (sem as top layers).

    Args:
        input_shape (tuple): Formato da imagem de entrada.
        num_classes (int): Número de classes de saída.

    Returns:
        model (tf.keras.Model): Modelo compilado.
    '''
    # Carregar VGG16 sem as camadas densas (top) e com pesos da ImageNet
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=input_shape)

    # Congelar as camadas convolucionais do VGG16
    for layer in base_model.layers:
        layer.trainable = False

    # Adicionar novas camadas densas customizadas
    x = base_model.output
    x = Flatten()(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.5)(x)
    predictions = Dense(num_classes, activation='softmax')(x)

    model = Model(inputs=base_model.input, outputs=predictions)
    return model


def compile_model(model, learning_rate=0.0001):
    '''
    Compila o modelo com otimizador Adam e categorical crossentropy.

    Args:
        model (tf.keras.Model): Modelo a ser compilado.
        learning_rate (float): Taxa de aprendizado do otimizador.

    Returns:
        model (tf.keras.Model): Modelo compilado.
    '''
    optimizer = Adam(learning_rate=learning_rate)
    model.compile(
        optimizer=optimizer,
        loss=CategoricalFocalCrossentropy(),
        metrics=['accuracy']
    )
    return model
