
file_rel_EN ='/Users/ljymacbook/Downloads/data/rel_EN.txt'
file_attr_EN ='/Users/ljymacbook/Downloads/data/attr_EN.txt'
file_rel_FR ='/Users/ljymacbook/Downloads/data/rel_FR.txt'
file_attr_FR ='/Users/ljymacbook/Downloads/data/attr_FR.txt'
file_rel_triples_EN='/Users/ljymacbook/Downloads/mappingbased_objects_en.ttl'
file_rel_triples_FR='//Users/ljymacbook/Downloads/mappingbased_objects_fr.ttl'
file_attribute_triples_EN='/Users/ljymacbook/Downloads/attributes_en.ttl'
file_attribute_triples_FR='/Users/ljymacbook/Downloads/mappingbased_literals_fr.ttl'



def read_triple_dbp_raw(file_path, language):
    triples = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip(' .\n').split('> ')
            if len(line) != 3:
                continue
            # print(line)
            s = line[0].lstrip('<')
            p = line[1].lstrip('<')
            o = line[2].lstrip('<').rstrip('>')
            if '"@'+language in o:
                o = o.lstrip('"').rstrip('"@'+language)
            # print(s, p, o)
            triples.add((s, p, o))
    print('read raw triple dbp:', len(triples))
    return triples


def write_triples(file_path, triples):
  
    file = open(file_path, 'w', encoding='utf-8')
    output = ''
    for (e, p, o) in triples:
        output = e + '\t' + p + '\t' + o + '\n'
        file.write(output)
    file.close()
    print('write_triples:', file_path, 'triple_num:', len(triples))
    return
   

rel_triples_fr = read_triple_dbp_raw(file_rel_triples_FR, 'fr')
attr_triples_fr = read_triple_dbp_raw(file_attribute_triples_FR, 'fr')
write_triples(file_rel_FR, rel_triples_fr)
write_triples(file_attr_FR, attr_triples_fr)

rel_triples_en = read_triple_dbp_raw(file_rel_triples_EN, 'en')
attr_triples_en = read_triple_dbp_raw(file_attribute_triples_EN, 'en')
write_triples(file_rel_EN, rel_triples_en)
write_triples(file_attr_EN, attr_triples_en)



