from  urllib import request

class Dataset:
   
    def __init__(self):
        pass

    def __get(self):
        url = 'https://raw.githubusercontent.com/maskot1977/ipython_notebook/master/toydata/location.txt'
        request.urlretrieve(url, '../storage/location.txt')
    
    def load(self):
        """
        各都道府県の経度緯度の情報を読み込む関数
        data:dict, data has the key "town_name",and the value is dict, whose keys are 'Longitude' and 'Latitude'.
        """
        import csv
        data = {}
        with open("../storage/location.txt", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == "Town":
                    continue
                else:
                    data[row[0]] = {'Longitude':float(row[1]), 'Latitude':float(row[2])}
        return data  

    def default_to_regular(self, defaultdict):
        data = dict(defaultdict)
        return data

if __name__=="__main__":
    dataset = Dataset()
    data = dataset.load()
    print(data)