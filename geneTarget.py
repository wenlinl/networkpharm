import json

# open the file
content = open('src/Co-Occurrence_ChemicalGeneSymbolNeighbor_CID_5351516.json', 'r')

# transfer to dict type
content_dict = json.load(content)

# return list
linkData = content_dict["LinkDataSet"]["LinkData"]

# create result file
result = open('result', 'w')

# iterate list
for item_dict in linkData:
    geneSymbol = item_dict["Evidence"]["ChemicalGeneSymbolNeighbor"]["NeighborName"]
    result.writelines(geneSymbol+'\n')
    print(geneSymbol)

# close the file
content.close()
