#https://raw.githubusercontent.com/googlei18n/language-resources/master/bn/data/lexicon.tsv
#https://github.com/googlei18n/language-resources/blob/master/third_party/iiit_ben_ant/etc/txt.done.data.utf8

from io import open
import json, regex

#txt.done.data.utf8
#lexicon.tsv
#output2_filter.utf8

with open('txt.done.data.utf8', mode='r', encoding='UTF-8', errors='strict', buffering=1) as f:
    read_data = f.read()
    write_data = open('output.utf8', 'w', encoding='UTF-8')
    for line in read_data:
        #sp = regex.findall('\W+',line)
        #s = regex.findall(u"[\u0980-\u09FF]+", line)
        s = regex.split(r"[A-Za-z0-9_\\\"\(\)#,.:\-^\/\[\]\=]", line)
        for line in s:
            write_data.write(line)
    write_data.close()

with open('lexicon.tsv', mode='r', encoding='UTF-8', errors='strict', buffering=1) as f:
    read_data = f.read()
    write_data = open('output2.utf8', 'w', encoding='UTF-8')
    for line in read_data:
        #sp = regex.findall('\W+',line)
        #s = regex.findall(u"[\u0980-\u09FF]+", line)
        s = regex.split(r"[A-Za-z0-9_\\\"\(\)#,.:\-^\/\[\]\=]", line)
        for line in s:
            write_data.write(line)
    write_data.close()

with open('output2.utf8', mode='r', encoding='UTF-8') as f1, open('output.utf8', mode='r', encoding='UTF-8') as f2:
    f1 = set(line.strip() for line in f1)
    f2 = set(line.strip() for line in f2)
    write_data = open('output_diff.utf8', 'w', encoding='UTF-8')
    write_data2 = open('output2_filter.utf8', 'w', encoding='UTF-8')
    list1 = []
    list2 = []
    for line in f2:
        words = line.split(' ')
        for item in words:
            list1.append(item)
            write_data.write(item+'\n')
    
    for line in f1:
        words = line.split(' ')
        for item in words:
            list2.append(item)
            write_data2.write(item+'\n')


rest = []
list3 = []
ache = 0
nai = 0

write_final = open('output_final.utf8', 'w', encoding='UTF-8')

print(len(list1))
print(len(list2))

#list3 = set(list1) & set(list2)
#print len(list3)

for word in list1:
    if word is not ' ' or word is not u'\n' or word is not '':
        if word in list2:
            list3.append(word)
            #write_final.write(word+'\n')
        else:
            if word not in rest and not any( word in s for s in list2):
                rest.append(word)
                write_final.write(word+'\n')



print(len(rest))
print(len(list3))