#%%
import json
import sys

with open("note_block.json","w") as note_block:

    orientation = [0,90,180,270]
    instruments = {0 : ["bell","chime","cow_bell","flute"],90:["basedrum","hat","snare","bass"],180:["harp","iron_xylophone","xylophone","guitar"],270:["bit","pling","didgeridoo","banjo"]}
    multipart = list()
    for i in range(0,25):
        for j in orientation:
            instlist = list()
            for instrument in instruments[j]:
                instlist.append({"note":i, "instrument":instrument})
            applydict = {"model":"block/note_block/note_block_"+str(i), "y":j}

            whenapply = {"when":{"OR":instlist}, "apply":applydict}
            multipart.append(whenapply)
    json.dump({"multipart":multipart}, note_block, indent=4)
    note_block.flush()
    note_block.close()
# %%
