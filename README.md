# **Uso de Redes Neurais Convolucionais (CNN) para Controle de Qualidade**

## **Visão Geral**
Este projeto implementa uma solução de **Controle de Qualidade Automatizado** baseada em **Visão Computacional**. Utilizando **Redes Neurais Convolucionais (CNN)** e **Transfer Learning**, o sistema realiza a detecção e classificação de defeitos em imagens de produtos, substituindo inspeções manuais tradicionais por um processo eficiente e preciso.  
Para este estudo utilizei a base de imagens https://www.kaggle.com/datasets/enalis/tomatoes-dataset, onde ao final, o modelo foi capaz de identificar as seguintes classes de tomates:
* Verdes
* Maduros
* Velhos
* Danificados

---

## **Objetivo**
* Automatizar o processo de inspeção de qualidade.  
* Detectar e classificar defeitos com alta acurácia.  
* Reduzir o tempo e os erros associados à inspeção manual.  

---  

## **Tecnologias Utilizadas**
* Linguagem: Python  
* Bibliotecas Principais:
   * TensorFlow / Keras
   * Scikit-learn
   * Pandas / NumPy
   * Matplotlib / Seaborn
* Modelo Pré-Treinado (Transfer Learning):
   * **VGG-16**  
* Ambiente de Desenvolvimento:
   * Google Colab

---

## **Arquitetura do Projeto**  

1. **Pré-Processamento das Imagens:**
* Redimensionamento das imagens para 224x224 pixels.
* Normalização dos valores dos pixels para a faixa [0, 1].

2. **Modelagem com Redes Neurais Convolucionais (CNN):**
* Implementação de modelos baseados em VGG-16 com Transfer Learning.
* Congelamento dos parâmetros das camadas superiores das camadas superiores do modelos pré-treinado.
* Remoção das camadas densas do modelo original.  
* Adição de novas camadas com quatro neurônios de saída e função de ativação SoftmaxAdição para a tarefa de classificação.
* Fine-tuning do novo modelo.

3. **Treinamento e Validação:**  
* Separação dos dados: 60% Treinamento, 20% Validação e 20% Teste.
* Uso de Cross-Entropy Loss e Adam Optimizer com taxa de aprendizado ajustada.
* Monitoramento da performance utilizando Acurácia e Loss.

4. **Resultados:**
* Acurácia Final do Modelo: 98%
* Tempo Médio de Inferência: ~20ms por imagem.
* Estimativa de redução de 70% em comparação com o tempo de inspeção manual.

5. **Próximos Passos:**
* Implementar uma interface gráfica (GUI) para facilitar a utilização por usuários não técnicos.
* Explorar outros modelos pré-treinados em busca de melhorias adicionais.

---

## Contato
* **Autor:** André Rizzo
* **LinkedIn:** linkedin.com/in/andrerizzo1
* **GitHub:** github.com/andrerizzo
* **Email:** andrerizzo@hotmail.com
