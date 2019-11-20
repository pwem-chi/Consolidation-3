dna_codon = input("Enter your DNA codons : ").upper()


def translate(codon):
    result = ""
    amino_codon = {
        "TTT":"F",
        "TTC":"F",
        "TTA":"L",
        "TTG":"L",
        "CTT":"L",
        "CTC":"L",
        "CTA":"L",
        "CTG":"L",
        "ATT":"I",
        "ATC":"I",
        "ATA":"I",
        "ATG":"M",
        "GTT":"V",
        "GTC":"V",
        "GTA":"V",
        "GTG":"V"}
    if len(codon) % 3 == 0:
        for c in range(0,len(dna_codon),3):
            result += amino_codon[dna_codon[c:c+3]]
    return result

def mutation():
    infile = open("DNA.txt", "r+")
    normal_dna = open("DNAnormal.txt", "w")
    mutated_dna = open("DNAmutated.txt", "w")
    
    data = infile.readlines()
    for line in data:
        normal_dna.write(line.replace('a','A'))
        mutated_dna.write(line.replace('a','T'))
        
    infile.close()
    normal_dna.close()
    mutated_dna.close()
    
def txt_translation(file):
    in_file = open(file, "r")
    content = in_file.read()
    translate(content)
    return translate(content)

    
print(translate(dna_codon))

mutation()

print(txt_translation("DNAnormal.txt"))
print(txt_translation("DNAmutated.txt"))


        
        
        
        