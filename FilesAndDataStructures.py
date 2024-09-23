# Loading from a file
thesaurus = {
  'strong' : {'mighty', 'tough', 'robust'},
  'small' : {'tiny', 'little'},
  'fast' : {'speedy', 'quick'},
  'calm' : {'mellow', 'chill', 'relaxed', 'peaceful'},
}

print(thesaurus)

def save_thesaurus(thes):
    f = open('thesaurus.txt', 'w')
    for k, v in thes.items():
        l = list(v)
        # print(k l)
        # print(k + ' : ' + ' '.join(l) + '\n')
        f.write(k + ' : ' + ' '.join(l) + '\n')
    f.close()

save_thesaurus(thesaurus)



