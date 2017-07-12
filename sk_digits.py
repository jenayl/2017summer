import sys
import matplotlib.pyplot as plt
from time import time
from sklearn.datasets import load_digits
digits = load_digits()

fig, axes = plt.subplots(2, 5, figsize=(10,5), subplot_kw={'xticks':(), 'yticks':()})
for ax, img in zip(axes.ravel(), digits.images):
    ax.imshow(img)

t0=time()
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca = pca.fit(digits.data)
digits_pca = pca.transform(digits.data)
colors = ["#476A2A","#7851B8",'#BD3430','#4A2D4E','#875525',
          '#A83683','#4E655E','#853541','#3A3120','#535D8E']

plt.figure(figsize=(10,10))
plt.xlim(digits_pca[:,0].min(), digits_pca[:,0].max())
plt.ylim(digits_pca[:,1].min(), digits_pca[:,1].max())

for i in range(len(digits.data)):
    plt.text(digits_pca[i,0], digits_pca[i,1], str(digits.target[i]),
             color = colors[digits.target[i]],
             fontdict={'weight':'bold', 'size':9})
plt.xlabel("first PC")
plt.ylabel("second PC")
plt.show()
print "PCA time: ", time()-t0

t1 = time()
from sklearn.manifold import TSNE
tsne = TSNE(random_state=42)
digits_tsne = tsne.fit_transform(digits.data)

plt.figure(figsize=(10,10))
plt.xlim(digits_tsne[:,0].min(), digits_tsne[:,0].max()+1)
plt.ylim(digits_tsne[:,1].min(), digits_tsne[:,1].max()+1)

for i in range(len(digits.data)):
    plt.text(digits_tsne[i,0], digits_tsne[i,1], str(digits.target[i]),
             color = colors[digits.target[i]],
             fontdict={'weight': 'bold', 'size': 9})
plt.xlabel("t-SNE feature 0")
plt.ylabel("t-SNE feature 1")
plt.show()
print "t-SNE time: ", time()-t1

#tSNE -> DBSCAN
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler = scaler.fit(digits_tsne)
scaled_t = scaler.transform(digits_tsne)

t2 = time()
from sklearn.cluster import DBSCAN
dbscan = DBSCAN()
clusters = dbscan.fit_predict(scaled_t)

plt.scatter(scaled_t[:,0], scaled_t[:,1], c=clusters, s=60, edgecolors='black')
plt.xlabel("feature 1")
plt.ylabel("feature 2")
plt.show()
print "DBSCAN time: ", time()-t2

#tSNE -> k-MEANS