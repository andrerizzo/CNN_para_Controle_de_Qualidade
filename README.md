# **Uso de Redes Neurais Convolucionais (CNN) para Controle de Qualidade**

## **Visão Geral**
Este projeto implementa uma solução de **Controle de Qualidade Automatizado** baseada em **Visão Computacional**. Utilizando **Redes Neurais Convolucionais (CNNs)** e **Transfer Learning**, o sistema realiza a detecção e classificação de defeitos em imagens de produtos, substituindo inspeções manuais tradicionais por um processo mais eficiente e preciso.  

Neste estudo, foi utilizada a base de dados:  
🔗 [Tomatoes Dataset (Kaggle)](https://www.kaggle.com/datasets/enalis/tomatoes-dataset)

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
- **Modelo Pré-Treinado:** VGG-16 (Transfer Learning)
- **Ambiente de Desenvolvimento:** Google Colab

---

## **Arquitetura do Projeto**

### 1. Pré-processamento das Imagens
- Redimensionamento para 224x224 pixels  
- Normalização dos valores de pixel para o intervalo [0, 1]  

### 2. Modelagem com CNN (VGG-16)
- Utilização de modelo pré-treinado com congelamento das camadas convolucionais
- Remoção das camadas densas originais
- Adição de novas camadas densas para classificação com 4 neurônios (softmax)
- Aplicação de **fine-tuning** nas camadas superiores

### 3. Treinamento e Validação
- Divisão dos dados: 60% Treino, 20% Validação, 20% Teste
- Otimizador: Adam  
- Função de perda: Categorical Crossentropy  
- Métricas: Acurácia e Loss

### 4. Resultados
- 📈 **Acurácia final:** 98%  
- ⚡ **Tempo médio de inferência:** ~20ms por imagem  
- ⏱️ **Redução estimada de tempo:** ~70% em relação à inspeção manual  

### 5. Próximos Passos
- Desenvolver uma interface gráfica (GUI) para uso por usuários não técnicos
- Avaliar outros modelos pré-treinados para comparação de desempenho

---

#---

### 👨‍💻 Sobre o Autor

**André Rizzo**  
📊 Cientista de Dados Sênior | Estatístico | MBA em IA e Big Data (USP)  
🧠 Especialista em Machine Learning, Deep Learning e Modelagem Estatística  
📍 Rio de Janeiro, Brasil  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andrerizzo1)
[![GitHub](https://img.shields.io/badge/GitHub-Portfólio-181717?logo=github&logoColor=white)](https://github.com/andrerizzo)
[![Email](https://img.shields.io/badge/Email-andrerizzo@hotmail.com-D14836?logo=gmail&logoColor=white)](mailto:andrerizzo@hotmail.com)

