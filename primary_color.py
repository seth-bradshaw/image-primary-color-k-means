import imageio
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

def extract_primary_color(url):    
    imageData = imageio.imread(url) # returns 3d array: [[height], [width], [pixel rgb vals]]
    np_rgbValues = np.array(imageData[2]) # grab 2d pixel rgb vals array
    df_rgbVals = pd.DataFrame(np_rgbValues)

    kmeans = KMeans(n_clusters=10, random_state = 0)
    kmeans.fit_predict(df_rgbVals)
    
    rmax = kmeans.cluster_centers_[-1][0]
    gmax = kmeans.cluster_centers_[-1][1]
    bmax = kmeans.cluster_centers_[-1][2]

    return {'r': rmax, 'g': gmax, 'b': bmax}