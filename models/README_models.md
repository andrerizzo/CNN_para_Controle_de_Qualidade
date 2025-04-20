# 📂 Pasta `models/`

Esta pasta armazena os **modelos treinados** ou arquivos relacionados à arquitetura e pesos finais do projeto.

## 🧠 Modelos Utilizados

Durante o projeto, foram treinadas redes CNN baseadas nos seguintes backbones:

- VGG16 (Transfer Learning e Fine-tuning)
- ResNet50 (Transfer Learning e Fine-tuning)

## 🔽 Download de Modelos (em breve)

Modelos finais não estão armazenados diretamente aqui devido ao limite de espaço do GitHub.

### Alternativas:

- **Treinar localmente** utilizando os scripts do projeto.
- **Disponibilizar via Hugging Face Hub, Google Drive ou outro repositório externo (opcional no futuro).**

## 📎 Sugestão de Estrutura

```
models/
├── resnet50v2/
│   ├── model_weights.h5
│   ├── model_config.json
│   └── training_history.pkl
├── vgg16/
│   └── ...
```

## 💡 Dica

Você pode utilizar o script `src/train_model.py` (ou notebook equivalente) para treinar e salvar um novo modelo com base nos dados disponíveis.
