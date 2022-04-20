Um projeto de pipeline de modelo de ml, no caso você precisa realizar um CLI que lhe permite:
    -- train: treinar o modelo novamente e avaliar o output
    -- evaluate: avaliar o modelo atual com os dados mais recentes
    -- use: aplicar o modelo em algum fim (ex: ativação de base)
    
    
Limitações:
- Utilizar python > 3.9
- Utilizar o sweetviz como fonte de insights primário
- Utilizar sklearn pipelines para transformação e exportação de modelos
- Realizar a hiperparametrização com skopt bayes
    - https://towardsdatascience.com/hyperparameter-optimization-with-scikit-learn-scikit-opt-and-keras-f13367f3e796
- Implementar ao menos 4 modelos simples para teste:
    - Logistic Regression
    - Decision Tree
    - Naive Bayes
    - KNN