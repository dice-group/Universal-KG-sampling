#path
file_pathEN = '/Users/ljymacbook/Downloads/interlanguage_links_en.ttl'
file_pathFR = '/Users/ljymacbook/Downloads/interlanguage_links_fr.ttl'
file_final ='/Users/ljymacbook/Downloads/data/entity_links.txt'
file_rel_EN ='/Users/ljymacbook/Downloads/data/rel_EN.txt'
file_rel_FR ='/Users/ljymacbook/Downloads/data/rel_FR.txt'

def read_links_raw(file_path, language):
    prefix = '<http://'
    if language == 'en':
        prefix += 'dbpedia.org'
    else:
        prefix += language
    links = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip(' .\n').split(' ')
            if len(line) != 3 or not line[2].startswith(prefix):
                continue
            line[0] = line[0].lstrip('<').rstrip('>')
            line[2] = line[2].lstrip('<').rstrip('>')
            links.add((line[0], line[2]))
            
    file.close()
    if language == 'en':
        links = set([(e2, e1) for (e1, e2) in links])  #change the sequcene as EN_FR
    return links
  
#read triples 
def read_triples(file_path):
    
    triples = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip('\n').split('\t')
            triples.add((line[0], line[1], line[2]))
    file.close()
    print('read_triples:', file_path, 'triple_num:', len(triples))
    return triples

#define the filter,if the e1 and e2 have triples
def filter_links(links, triples1, triples2, is_rel_triples=True):
    ents1 = set([h for (h, _, _) in triples1])
    ents2 = set([h for (h, _, _) in triples2])
    #do the judgements
    if is_rel_triples:
        ents1 = ents1 | set([t for (_, _, t) in triples1])
        ents2 = ents2 | set([t for (_, _, t) in triples2])
    links_new = set([(e1, e2) for (e1, e2) in links if e1 in ents1])
    links_new = set([(e1, e2) for (e1, e2) in links_new if e2 in ents2])
    return links_new
  
  
#write links 
 def write_links(filepath, ent_links):
    
    file = open(filepath, 'w', encoding='utf-8')
    for (e1, e2) in ent_links:
        output = e1 + '\t' + e2 + '\n'
        file.write(output)
    #file.close()
    print('write_links:', file_final, 'ent_link_num:', len(ent_links))
    return
  
  
#read raw EN-FR entity linking
en_other = read_links_raw(file_pathEN, 'fr') 
print('en_other:', len(en_other))

#read raw FR-EN entity linking
other_en = read_links_raw(file_pathFR, 'en') 
print('other_en:', len(other_en))

#join two raw entity linking sets
links_new = en_other | other_en  
#other = 'DBP_' + 'fr'
print('raw links:', len(links_new))


#filters the raw links
rel_triples1 = read_triples(file_rel_EN)
rel_triples2 = read_triples(file_rel_FR)

links_new = filter_links(links_new, rel_triples1, rel_triples2)
print('after filter_links by rel_triples:', len(links_new))
 
write_links(file_final, links_new)
