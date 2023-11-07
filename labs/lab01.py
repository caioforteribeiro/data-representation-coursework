import requests
import csv
from xml.dom.minidom import parseString

url="https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page=requests.get(url)
doc=parseString(page.content)
retrieveTags=["TrainStatus",
"TrainLatitude",
"TrainLongitude",
"TrainCode",
"TrainDate",
"PublicMessage",
"Direction"
]

#print(doc.toprettyxml())

#with open("trainxml.xml", "w") as xmlfp:
    #doc.writexml(xmlfp)

with open("train.csv", "w", newline="") as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)
