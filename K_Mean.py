import random
import matplotlib.pyplot as plt

def dis(p1, p2):
    tot = 0
    for index in range(len(p1)):
        tot += (p1[index]-p2[index])*(p1[index]-p2[index])
    return tot


class K_Mean:
    def __init__(self):
        # 聚类数量
        self.num = 0
        self.data = None
        #聚类
        self.clusters = None
        #聚类中心
        self.centers = None

    def Train(self, data=[], num=2):
        self.data = data
        self.num = num
        #创建聚类
        self.clusters = []
        for index in range(num):
            #创建聚类中的点
            self.clusters.append([])
        #初始化聚类中心
        self.centers = []
        init = data
        random.shuffle(init)
        for index in range(num):
            self.centers.append(init[index])
        while True:
            for index in range(self.num):
                self.clusters[index] = []
            for point in data:
                distant = dis(point, self.centers[0])
                clus = 0
                for index in range(num):
                    if dis(point, self.centers[index]) < distant:
                        distant = dis(point, self.centers[index])
                        clus = index
                self.clusters[clus].append(point)
            check = False
            for index in range(num):
                if len(self.clusters[index]) == 0:
                    self.centers[index] = data[random.randint(len(data)-1)]
                    check=True
                else:
                    newCenter = [0] * len(self.clusters[index][0])
                    for point in self.clusters[index]:
                        for dim in range(len(point)):
                            newCenter[dim] += point[dim]
                    size = len(self.clusters[index])
                    for dim in range(len(newCenter)):
                        newCenter[dim] /= size
                if self.centers[index] != newCenter:
                    check = True
                self.centers[index] = newCenter
            if not check:
                break

    def Perdict(self, data):
        distant = dis(data, self.centers[0])
        res = 0
        for index in range(self.num):
            if dis(self.centers[index], data) < distant:
                res = index
                distant = dis(self.centers[index], data)
        return res

    def ShowPlot(self, mark):
        for index in range(self.num):
            for point in self.clusters[index]:
                plt.plot(point[0], point[1], mark[index], markersize=5)
        plt.show()



if __name__ == "__main__":
    k_mean = K_Mean()
    datas = [[1, 2], [2, 3], [3, 1], [2, 1], [6, 9], [7, 8], [8, 6], [4, 8], [11, 3], [9, 6], [12, 4]]
    k_mean.Train(data=datas, num=6)
    marks = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    k_mean.ShowPlot(marks)