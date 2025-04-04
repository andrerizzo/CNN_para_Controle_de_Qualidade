'''
Arquivo: build_model.py
Descrição: Módulo de construção e compilação do modelo CNN com Transfer Learning (VGG16 e ResNet50)
Autor: André Rizzo


Functions:

    build_model_vgg16(input_shape, num_classes)
    compile_model_vgg16(model, learning_rate)

    build_model_vgg16_v2(input_shape, num_classes)
    compile_model_vgg16_v2(model, learning_rate)
    
    build_model_resnet50(input_shape, num_classes)
    compile_model_resnet50(model, learning_rate)

     build_model_resnet50_v2(input_shape, num_classes)
    compile_model_resnet50_v2(model, learning_rate)
'''

import tensorflow as tf
from tensorflow.keras.applications import VGG16, ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalFocalCrossentropy

'''
    Modelo VGG16 versão 1
        - Todas as camadas convolucionais congeladas utilizando os pesos originais.
        - Classificador com uma camada densa e 256 neurônios.
        - Softmax como função de ativação.
'''
def build_model_vgg16(input_shape=(224, 224, 3), num_classes=4):
    '''
    Constrói o modelo CNN com base no VGG16 pré-treinado (sem as top layers).

    Args:
        input_shape (tuple): Formato da imagem de entrada.
        num_classes (int): Número de classes de saída.

    Returns:
        model (tf.keras.Model): Modelo compilado.
    '''
    # Carregar VGG16 sem as camadas densas (top) e com pesos da ImageNet
    base_model_vgg16 = VGG16(weights='imagenet', include_top=False, input_shape=input_shape)

    # Congelar as camadas convolucionais do VGG16
    for layer in base_model_vgg16.layers:
        layer.trainable = False

    # Adicionar novas camadas densas customizadas
    x = base_model_vgg16.output
    x = Flatten()(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.5)(x)
    predictions_vgg16 = Dense(num_classes, activation='softmax')(x)

    model_vgg16 = Model(inputs=base_model_vgg16.input, outputs=predictions_vgg16)
    return model_vgg16



'''
    Modelo VGG16 versão 2
        - 20 camadas convolucionais descongeladas 
        - Demais camadas convolucionais utilizando os pesos originais.
        - Classificador com uma camada densa e 256 neurônios.
        - Softmax como função de ativação.
'''
def build_model_vgg16_v2(input_shape=(224, 224, 3), num_classes=4):
    '''
    Constrói o modelo CNN com base no VGG16 pré-treinado (sem as top layers).

    Args:
        input_shape (tuple): Formato da imagem de entrada.
        num_classes (int): Número de classes de saída.

    Returns:
        model (tf.keras.Model): Modelo compilado.
    '''
    # Carregar VGG16 sem as camadas densas (top) e com pesos da ImageNet
    base_model_vgg16_v2 = VGG16(weights='imagenet', include_top=False, input_shape=input_shape)

    # Congelar as camadas convolucionais do VGG16
    for layer in base_model_vgg16_v2.layers[-20:]:
        layer.trainable = True

    # Adicionar novas camadas densas customizadas
    x = base_model_vgg16_v2.output
    x = Flatten()(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.5)(x)
    predictions_vgg16_v2 = Dense(num_classes, activation='softmax')(x)

    model_vgg16_v2 = Model(inputs=base_model_vgg16_v2.input, outputs=predictions_vgg16_v2)
    return model_vgg16_v2


def compile_model_vgg16(model, learning_rate=0.0001):
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


# MODELO RESNET50

'''
    Modelo Resnet50 versão 1
        - Todas as camadas convolucionais congeladas utilizando os pesos originais.
        - Classificador com uma camada densa e 256 neurônios.
        - Softmax como função de ativação.
'''

def build_model_resnet50(input_shape=(224, 224, 3), num_classes=4):
    '''
    Constrói o modelo CNN com base no ResNet50 pré-treinado (sem as top layers).

    Args:
        input_shape (tuple): Formato da imagem de entrada.
        num_classes (int): Número de classes de saída.

    Returns:
        model_resnet50 (tf.keras.Model): Modelo compilado.
    '''
    # Carregar ResNet50 sem as camadas densas (top) e com pesos da ImageNet
    base_model_resnet50 = ResNet50(weights='imagenet', include_top=False, input_shape=input_shape)

    # Congelar as camadas convolucionais do VGG16
    for layer in base_model_resnet50.layers:
        layer.trainable = False

    # Adicionar novas camadas densas customizadas
    x = base_model_resnet50.output
    x = Flatten()(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.5)(x)
    predictions_resnet50 = Dense(num_classes, activation='softmax')(x)

    model_resnet50 = Model(inputs=base_model_resnet50.input, outputs=predictions_resnet50)
    return model_resnet50


'''
    Modelo ResNet50 versão 2
        - 20 camadas convolucionais descongeladas 
        - Demais camadas convolucionais utilizando os pesos originais.
        - Classificador com uma camada densa e 256 neurônios.
        - Softmax como função de ativação.
'''

def build_model_resnet50_v2(input_shape=(224, 224, 3), num_classes=4):
    '''
    Constrói o modelo CNN com base no ResNet50 pré-treinado (sem as top layers).

    Args:
        input_shape (tuple): Formato da imagem de entrada.
        num_classes (int): Número de classes de saída.

    Returns:
        model_resnet50_v2 (tf.keras.Model): Modelo compilado.
    '''
    # Carregar ResNet50 sem as camadas densas (top) e com pesos da ImageNet
    base_model_resnet50_v2 = ResNet50(weights='imagenet', include_top=False, input_shape=input_shape)

    # Congelar as camadas convolucionais do VGG16
    for layer in base_model_resnet50_v2.layers[-20:]:
        layer.trainable = True

    # Adicionar novas camadas densas customizadas
    x = base_model_resnet50_v2.output
    x = Flatten()(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.5)(x)
    predictions_resnet50_v2 = Dense(num_classes, activation='softmax')(x)

    model_resnet50_v2 = Model(inputs=base_model_resnet50_v2.input, outputs=predictions_resnet50_v2)
    return model_resnet50_v2


def compile_model_resnet50(model, learning_rate=0.0001):
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
