from flask import Flask, json, request
import pandas as pd
from scipy.spatial.distance import cdist
import numpy as np
import pickle
import flask

def closest_node(node, nodes):
    return nodes[cdist([node], nodes).argmin()]

api = Flask(__name__)

df = pd.read_csv("models/website/cluster_label_for_dataset.csv")
print(df.columns)
filteredDf = df[['lat', 'long', 'population', 'conflict_intensity', 'corruption_perception_index','solar', 'wind_speed', 'kmeans_label', 'birch_label', 'gaussian_label', 'iso3_code']]
filteredDfDict = dict()
filteredDfNodes = []
filteredDfFullNodes = []
idx = 0
for index, row in filteredDf.iterrows():
    if idx % 100000 == 0:
        print(idx)
    idx += 1
    if row['lat'] not in filteredDfDict:
        filteredDfDict[row['lat']] = dict()
    filteredDfDict[row['lat']][row['long']] = row.to_dict()
    filteredDfNodes.append([row['lat'], row['long']])
    filteredDfFullNodes.append(row.to_dict())
nodes = np.asarray(filteredDfNodes)

# filteredDfDict = pickle.load(open("models/website/filteredDfDict.p", "rb"))
# nodes = pickle.load(open("models/website/nodes.p", "rb"))

# pickle.dump(filteredDfDict, open("models/website/filteredDfDict.p", "wb"))
# pickle.dump(nodes, open("models/website/nodes.p", "wb"))


print("Ready")
@api.route('/closestPointData', methods=["GET"])
def getClosestPointData():
    lat = float(request.args.get('lat'))
    lon = float(request.args.get('lon'))
    closestPoint = closest_node([lat, lon], nodes)
    if cdist([closestPoint], [[lat, lon]]).min() > 0.5:
        response = flask.jsonify({"status": "none", "data": None})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    response = flask.jsonify({"status": "success", "data": filteredDfDict[closestPoint[0]][closestPoint[1]]})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    api.run('127.0.0.1')