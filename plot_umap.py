import umap.umap_ as umap
import matplotlib.pyplot as plt, seaborn as sns

def draw_umap(data, hue, n_neighbors=100, min_dist=0.1, n_components=2, metric='euclidean', title=''):
    fit = umap.UMAP(
        n_neighbors=n_neighbors,
        min_dist=min_dist,
        n_components=n_components,
        metric=metric
    )
    u = fit.fit_transform(data);
    fig = plt.figure()

    if n_components == 2:
        sns.scatterplot(x=u[:,0], y=u[:, 1], hue=hue, palette="dark").set(title="UMAP Data 2D")
    if n_components == 3:
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(u[:,0], u[:,1], u[:,2], c=data, s=100)
        plt.title(title, fontsize=18)