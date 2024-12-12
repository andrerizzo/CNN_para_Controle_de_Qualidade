# Uso de Redes Neurais Convolucionais (CNN) para Controle de Qualidade

Este estudo tem o objetivo de utilizar Redes Neurais Convolucionais para a identificação do padrão de qualidade de tomates. Ao final, o modelo deve ser capaz de identificar as seguintes classes de tomates:

* Verdes
* Maduros
* Velhos
* Danificados

Para este estudo utilizei a base de imagens https://www.kaggle.com/datasets/enalis/tomatoes-dataset.  
No estudo fiz uso Transfer Learning, onde utilizei o modelo VGG16 como base, porém removi as camadas densas criando um novo classificador com quetro neurônios de saída com função de ativação Softmax.  

**Após o fine tuning, o modelo atingiu acurácia de 97% durante o treinamento e posteriormente 94% com as imagens de teste.**  
