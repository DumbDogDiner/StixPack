import json
for i in range (0,24+1):
    nbfile = open("note_block_"+str(i)+".json","w")
    js = {
        "parent": "block/cube_top",
        "textures": {
            "top": "block/note_block/note_block_"+str(i),
            "side": "block/note_block"
        }
    }
    json.dump(js, nbfile, indent=2)
    nbfile.flush()
    nbfile.close()
