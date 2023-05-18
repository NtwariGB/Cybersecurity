import yara

def analyze_file(file_path, rule_file):
    rules = yara.compile(rule_file)
    matches = rules.match(file_path)

    if matches:
        print("Le fichier a été détecté par les règles suivantes :")
        for match in matches:
            print(match)

    else:
        print("Le fichier n'a pas été détecté par les règles.")
        

if __name__ == '__main__':
    file_path = 'file_to_analyze.txt'
    rule_file = 'rules.yar'
    analyze_file(file_path, rule_file)
