'''
Arquivo: preprocess.py
Autor: André Rizzo

Módulo de pré-processamento para classificação de imagens de tomates.
Inclui renomeação de diretórios e geração de ImageDataGenerators para treino e validação.
'''


import tensorflow as tf
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.applications.vgg16 import preprocess_input

def train_val_test_generators(img_path, img_size, bt_size, val_split, test_split):
    '''
    Cria geradores de imagem para treino, validação e teste.

    Args:
        img_path (str): Caminho da pasta com imagens organizadas por classe.
        img_size (tuple): Tamanho das imagens (altura, largura).
        bt_size (int): Tamanho do batch.
        val_split (float): Proporção dos dados para validação (do total restante após teste).
        test_split (float): Proporção dos dados para teste (do total).

    Returns:
        tuple: (train_dataset, val_dataset, test_dataset)
    '''

    # Carrega todas as imagens do diretório, inferindo as classes com base nos nomes das subpastas.
    # Aplica redimensionamento, agrupamento em batches e embaralhamento com seed fixa.
    full_dataset = image_dataset_from_directory(
        directory=img_path,
        label_mode='categorical',     # Rótulos no formato one-hot
        labels='inferred',            # Infere os rótulos pelas subpastas
        image_size=img_size,          # Redimensiona para (altura, largura)
        batch_size=bt_size,           # Tamanho do batch
        shuffle=True,                 # Embaralha os dados
        seed=42                       # Reprodutibilidade do shuffle
    )

    class_names = full_dataset.class_names
    
    # Conta quantos batches existem no dataset completo
    total_batches = tf.data.experimental.cardinality(full_dataset).numpy()

    # Calcula a quantidade de batches para o conjunto de teste (ex: 20%)
    test_batches = int(total_batches * test_split)

    # Calcula a quantidade de batches para validação (ex: 20% do que sobrou após teste)
    val_batches = int((total_batches - test_batches) * val_split)

    # O restante vai para o conjunto de treino
    train_batches = total_batches - test_batches - val_batches

    # Separa os primeiros batches para teste
    test_dataset = full_dataset.take(test_batches)

    # Pula os batches já usados em teste
    remaining_dataset = full_dataset.skip(test_batches)

    # Dos dados restantes, separa uma parte para validação
    val_dataset = remaining_dataset.take(val_batches)

    # E o restante final é usado como conjunto de treino
    train_dataset = remaining_dataset.skip(val_batches)

    # Retorna os três datasets prontos para uso
    return train_dataset, val_dataset, test_dataset, class_names




def vgg16_pre_processing(train_ds, val_ds, test_ds):
    """
    Aplica o pré-processamento necessário para a VGG16 em datasets do tipo tf.data.Dataset.

    Args:
        train_ds, val_ds, test_ds (tf.data.Dataset): Datasets de treino, validação e teste.

    Returns:
        tuple: (train_ds, val_ds, test_ds) com as imagens pré-processadas.
    """

    AUTOTUNE = tf.data.AUTOTUNE

    train_ds = train_ds.map(lambda x, y: (preprocess_input(x), y))
    val_ds = val_ds.map(lambda x, y: (preprocess_input(x), y))
    test_ds = test_ds.map(lambda x, y: (preprocess_input(x), y))


    # Adiciona prefetch para melhorar desempenho
    train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)
    test_ds = test_ds.prefetch(buffer_size=AUTOTUNE)

    return train_ds, val_ds, test_ds