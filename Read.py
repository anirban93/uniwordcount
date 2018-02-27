#https://raw.githubusercontent.com/googlei18n/language-resources/master/bn/data/lexicon.tsv
#https://github.com/googlei18n/language-resources/blob/master/third_party/iiit_ben_ant/etc/txt.done.data.utf8

from io import open
import json, regex


with open('txt.done.data.utf8', mode='r', encoding='UTF-8', errors='strict', buffering=1) as f:
    read_data = f.read()
    write_data = open('output.utf8', 'w', encoding='UTF-8')
    for line in read_data:
        sp = regex.findall('\(+ |\W+ | \)+',line)
        s = regex.findall(u"[\u0980-\u09FF]+", line)
        for item in sp:
            #print item
            write_data.write(item)
    write_data.close()