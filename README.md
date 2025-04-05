# **Uso de Redes Neurais Convolucionais (CNN) para Controle de Qualidade**

## **Visão Geral**
Este projeto implementa uma solução de **Controle de Qualidade Automatizado** baseada em **Visão Computacional**. Utilizando **Redes Neurais Convolucionais (CNNs)** e **Transfer Learning**, o sistema realiza a detecção e classificação de defeitos em imagens de produtos, substituindo inspeções manuais por um processo mais eficiente e preciso.  

🔗 Dataset utilizado: [Tomatoes Dataset (Kaggle)](https://www.kaggle.com/datasets/enalis/tomatoes-dataset)

O modelo final foi capaz de identificar as seguintes classes de tomates:
- 🍅 Verdes  
- 🍅 Maduros  
- 🍅 Velhos  
- 🍅 Danificados

---

## **Objetivo**
- Automatizar o processo de inspeção de qualidade  
- Detectar e classificar defeitos com alta acurácia  
- Reduzir tempo e erros associados à inspeção manual  

---

## **Tecnologias Utilizadas**
- **Linguagem:** Python  
- **Bibliotecas Principais:**
  - TensorFlow / Keras
  - Scikit-learn
  - Pandas / NumPy
  - Matplotlib / Seaborn
- **Modelos Pré-Treinados:** VGG-16 e ResNet50
- **Ambiente de Desenvolvimento:** Google Colab
- Todo o pipeline de treinamento foi executado em ambiente **Google Colab**, com uso de GPU **NVIDIA A100 (versão premium)**.  


---

## **Arquitetura do Projeto**

### 1. Pré-processamento das Imagens
- Redimensionamento para 224x224 pixels  
- Normalização dos valores de pixel para o intervalo [0, 1]  

### 2. Modelagem com CNN
- Utilização de modelos pré-treinados (VGG16 e ResNet50)
- Congelamento das camadas convolucionais
- Adição de camadas densas customizadas
- Fine-tuning nas camadas superiores em versões "v2"

### 3. Treinamento e Validação
- Divisão dos dados: 60% Treino, 20% Validação, 20% Teste
- Otimizador: Adam  
- Função de perda: Categorical Focal Crossentropy  
- Métricas: Acurácia e Loss

---

## 🧪 Modelos Avaliados

Durante o desenvolvimento, foram implementadas e comparadas quatro variações baseadas em redes pré-treinadas:

| Modelo              | Backbone     | Estratégia                       |
|---------------------|--------------|----------------------------------|
| VGG16               | VGG16        | Transfer Learning (camadas congeladas) |
| VGG16 (V2)          | VGG16        | Fine-tuning nas camadas superiores |
| ResNet50            | ResNet50     | Transfer Learning (camadas congeladas) |
| ResNet50 (V2)       | ResNet50     | Fine-tuning nas camadas superiores |

---

## 📊 Comparativo de Desempenho

### Acurácia

![](/img/Accuracy_graph.png)  


### Tabela Comparativa

| Modelo         | Acurácia | 
|----------------|----------|
| VGG16          |      98%  | 
| VGG16 (V2)     |      97%       | 
| ResNet50       |      96%       | 
| **ResNet50 (V2)**  | **99%**    | 

> 🔹 O modelo **ResNet50 (V2)** apresentou o melhor desempenho geral e foi selecionado como modelo final do projeto.

---

## 📈 Avaliação Detalhada por Modelo

### 📋 Relatórios de Classificação (base de teste)

- **VGG16**  
![](/img/Classification_report_VGG16.png)

- **VGG16 (V2)**  
![](/img/Classification_report_VGG16v2.png)  

- **ResNet50**  
![](/img/Classification_report_ResNet50.png)  

- **ResNet50 (V2)**  
![](/img/Classification_report_ResNet50v2.png) 

---

### 🔄 Matrizes de Confusão

Inserir abaixo as imagens geradas para cada modelo:

| Modelo         |  |
|----------------|--------------------|
| VGG16          | ![](/img/Confusion_Matrix_VGG16.png) |
| VGG16 (V2)     | ![](/img/Confusion_Matrix_VGG16v2.png) |
| ResNet50       | ![](/img/Confusion_Matrix_ResNet50.png)|
| ResNet50 (V2)  | ![](/img/Confusion_Matrix_ResNet50v2.png) |

---

## **Próximos Passos**
- Desenvolver uma interface gráfica (GUI) com Streamlit ou Gradio
- Publicar modelo via API para produção

---

## 👨‍💻 Sobre o Autor

**André Rizzo**  
📊 Cientista de Dados Sênior | Estatístico | MBA em IA e Big Data (USP)  
🧠 Especialista em Machine Learning, Deep Learning e Modelagem Estatística  
📍 Rio de Janeiro, Brasil  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andrerizzo1)
[![GitHub](https://img.shields.io/badge/GitHub-Portfólio-181717?logo=github&logoColor=white)](https://github.com/andrerizzo)
[![Email](https://img.shields.io/badge/Email-andrerizzo@hotmail.com-D14836?logo=gmail&logoColor=white)](mailto:andrerizzo@hotmail.com)

