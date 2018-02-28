#https://raw.githubusercontent.com/googlei18n/language-resources/master/bn/data/lexicon.tsv
#https://github.com/googlei18n/language-resources/blob/master/third_party/iiit_ben_ant/etc/txt.done.data.utf8

from io import open
import json, regex

#txt.done.data.utf8
#lexicon.tsv
with open('txt.done.data.utf8', mode='r', encoding='UTF-8', errors='strict', buffering=1) as f:
    read_data = f.read()
    write_data = open('output.utf8', 'w', encoding='UTF-8')
    for line in read_data:
        #sp = regex.findall('\W+',line)
        #s = regex.findall(u"[\u0980-\u09FF]+", line)
        s = regex.split(r"[A-Za-z0-9_\\\"\(\)#,.:\-^\/\[\]\=]", line)
        for item in s:
            #print item
            write_data.write(item)
    write_data.close()
with open('output2.utf8', mode='r', encoding='UTF-8') as f1, open('output.utf8', mode='r', encoding='UTF-8') as f2:
    f1 = set(line.strip() for line in f1)
    f2 = set(line.strip() for line in f2)
    write_data = open('output_diff.utf8', 'w', encoding='UTF-8')
    for line in f1:
        for line1 in f2:
            #print line1
            if line == line1:
                write_data.write(line)
        if line:
            write_data.write(line)