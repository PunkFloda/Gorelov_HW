from gensim.models import Word2Vec
import pandas as pd
import ast
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
import numpy as np

w2v_model = Word2Vec(
    min_count=5,
    window=5,
    vector_size=1000,
    negative=5,
    workers=24,
    alpha=0.03,
    min_alpha=0.0007,
    sample=6e-5,
    sg=1)
# vector_size — размер векторного представления слова (word embedding).
# negative — сколько неконтекстных слов учитывать в обучении, используя negative sampling.
# alpha — начальный learning_rate, используемый в алгоритме обратного распространения ошибки (Backpropogation).
# min_alpha — минимальное значение learning_rate, на которое может опуститься в процессе обучения.
# sg — если 1, то используется реализация Skip-gram; если 0, то CBOW.

df = pd.read_excel('output_table.xlsx')  # Уже почищено и токенизировано в файле preprocessing
sentences = df['text_token'].apply(ast.literal_eval)

w2v_model.build_vocab(sentences)  # Получаем словарь
print(len(w2v_model.wv.index_to_key))
w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=5, report_delay=1)  # Обучение
print(*w2v_model.wv.most_similar(positive=["obama"], topn=15), sep='\n')  # Выводим 30 самых схожих с "obama"
print()
print(*w2v_model.wv.most_similar(positive=["oil"], topn=15), sep='\n')
print()
print(*w2v_model.wv.most_similar(positive=["obama", "president"], negative=["clinton"], topn=15), sep='\n')
# Выводим 30 самых схожих с обама + президент - клинтон
print(w2v_model.wv.most_similar_to_given("obama", ["president", "clinton", "obamacare"]))


# Выводим самое схожее с "obama" из трех предложенных


def tsne_scatterplot(model, word, list_names):
    """Plot in seaborn the results from the t-SNE dimensionality reduction algorithm."""
    vectors_words = [model.wv.get_vector(word)]
    word_labels = [word]
    color_list = ['red']

    close_words = model.wv.most_similar(word)
    for wrd_score in close_words:
        wrd_vector = model.wv.get_vector(wrd_score[0])
        vectors_words.append(wrd_vector)
        word_labels.append(wrd_score[0])
        color_list.append('blue')

    for wrd in list_names:
        wrd_vector = model.wv.get_vector(wrd)
        vectors_words.append(wrd_vector)
        word_labels.append(wrd)
        color_list.append('green')

    vectors_words = np.array(vectors_words)
    Y = TSNE(n_components=2, random_state=0, perplexity=min(5, len(vectors_words) - 1), init="pca").fit_transform(
        vectors_words)

    df = pd.DataFrame({"x": Y[:, 0], "y": Y[:, 1], "words": word_labels, "color": color_list})
    fig, _ = plt.subplots(figsize=(9, 9))
    p1 = sns.regplot(data=df, x="x", y="y", fit_reg=False, marker="o",
                     scatter_kws={"s": 40, "facecolors": df["color"]})
    for line in range(0, df.shape[0]):
        p1.text(df["x"][line], df["y"][line], " " + df["words"][line].title(),
                horizontalalignment="left", verticalalignment="bottom",
                size="medium", color=df["color"][line], weight="normal").set_size(15)

    plt.xlim(Y[:, 0].min() - 50, Y[:, 0].max() + 50)
    plt.ylim(Y[:, 1].min() - 50, Y[:, 1].max() + 50)
    plt.title('t-SNE visualization for {}'.format(word.title()))


tsne_scatterplot(w2v_model, "obama", ["clinton", "obamacare"])
