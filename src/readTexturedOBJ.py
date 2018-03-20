from faceNormals import *
import numpy as np

def readTexturedOBJ(filepath):
    V = []
    F = []
    TV = [] # UV coordinate
    TF = [] # face list for texture vertices TV
    with open(filepath, "rb") as f:
        lines = f.readlines()
    while True:
        for line in lines:
            if line == "":
                break
            elif line.strip().startswith("vn"):
                continue
            elif line.strip().startswith("vt"):
                lineLength = len(line.replace("\n", "").split(" "))
                UV = line.replace("\n", "").split(" ")[1:3]
                UV = np.delete(UV,np.argwhere(UV == np.array([''])).flatten())
                TV.append(map(float, UV))
            elif line.strip().startswith("v"):
                lineLength = len(line.replace("\n", "").split(" "))
                vertices = line.replace("\n", "").split(" ")[1:4]
                vertices = np.delete(vertices,np.argwhere(vertices == np.array([''])).flatten())
                V.append(map(float, vertices))
            elif line.strip().startswith("f"):
                t_index_list = []
                textureFaceList = []
                for t in line.replace("\n", "").split(" ")[1:]:
                    t_index = t.split("/")[0]
                    try: 
                        t_index_list.append(int(t_index) - 1)
                    except ValueError:
                        continue
                    textureFace = t.split("/")[1]
                    try: 
                        textureFaceList.append(int(textureFace) - 1)
                    except ValueError:
                        continue
                F.append(t_index_list)
                TF.append(textureFaceList)
            else:
                continue
        break
    V = np.asarray(V)
    F = np.asarray(F)
    TV = np.asarray(TV)
    TF = np.asarray(TF)

    # flip triangles if wrong orientation
    tempV = np.concatenate((TV, np.zeros((TV.shape[0],1))), axis = 1)
    FN = faceNormals(tempV, TF)
    flipIdx = np.where(FN[:,2] == -1)[0]
    temp = TF[flipIdx,1]
    TF[flipIdx,1] = TF[flipIdx,2]
    TF[flipIdx,2] = temp

    return V, F, TV, TF

