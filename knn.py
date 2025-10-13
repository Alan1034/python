from sklearn.neighbors import KNeighborsClassifier
def dme3():
    x=[[39,0,31],[3,2,65],[2,3,55],[9,38,2],[8,34,17],[5,2,57],[21,17,5],[45,2,9]]
    y=[0,1,2,2,2,1,0,0]
    estimator =KNeighborsClassifier(n_neighbors=5)
    estimator.fit(x,y)
    mypre =estimator.predict([[23,3,17]])
    print(f"预测结果为：{mypre}")
dme3()