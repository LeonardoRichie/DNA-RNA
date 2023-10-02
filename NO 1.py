
def complement_dna(dna_sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement_sequence = [complement_dict[base] for base in dna_sequence]
    return ''.join(complement_sequence)

genetic_code = {
     "UUU": "Phe (F)", "UUC": "Phe (F)", "UUA": "Leu (L)", "UUG": "Leu (L)",
    "CUU": "Leu (L)", "CUC": "Leu (L)", "CUA": "Leu (L)", "CUG": "Leu (L)",
    "AUU": "Ile (I)", "AUC": "Ile (I)", "AUA": "Ile (I)", "AUG": "Met (M)",
    "GUU": "Val (V)", "GUC": "Val (V)", "GUA": "Val (V)", "GUG": "Val (V)",
    "UCU": "Ser (S)", "UCC": "Ser (S)", "UCA": "Ser (S)", "UCG": "Ser (S)",
    "CCU": "Pro (P)", "CCC": "Pro (P)", "CCA": "Pro (P)", "CCG": "Pro (P)",
    "ACU": "Thr (T)", "ACC": "Thr (T)", "ACA": "Thr (T)", "ACG": "Thr (T)",
    "GCU": "Ala (A)", "GCC": "Ala (A)", "GCA": "Ala (A)", "GCG": "Ala (A)",
    "UAU": "Tyr (Y)", "UAC": "Tyr (Y)", "UAA": "Stop ()", "UAG": "Stop ()",
    "CAU": "His (H)", "CAC": "His (H)", "CAA": "Gln (Q)", "CAG": "Gln (Q)",
    "AAU": "Asn (N)", "AAC": "Asn (N)", "AAA": "Lys (K)", "AAG": "Lys (K)",
    "GAU": "Asp (D)", "GAC": "Asp (D)", "GAA": "Glu (E)", "GAG": "Glu (E)",
    "UGU": "Cys (C)", "UGC": "Cys (C)", "UGA": "Stop (*)", "UGG": "Trp (W)",
    "CGU": "Arg (R)", "CGC": "Arg (R)", "CGA": "Arg (R)", "CGG": "Arg (R)",
    "AGU": "Ser (S)", "AGC": "Ser (S)", "AGA": "Arg (R)", "AGG": "Arg (R)",
    "GGU": "Gly (G)", "GGC": "Gly (G)", "GGA": "Gly (G)", "GGG": "Gly (G)"
}


input_dna = "TTACGA"


complement_sequence = complement_dna(input_dna)

#Transcribe DNA to mRNA
mrna_sequence = complement_sequence.replace("T", "U")


codons = [mrna_sequence[i:i+3] for i in range(0, len(mrna_sequence), 3)]
amino_acid_sequence = []
for codon in codons:
    if len(codon) == 3 and codon in genetic_code:
        amino_acid = genetic_code[codon]
        if amino_acid != "Stop":
            amino_acid_sequence.append(amino_acid)
        else:
            break
    else:
        print(f"Invalid codon: {codon}")


print("Input DNA =", input_dna)
print("Complement =", complement_sequence)
print("mRNA = ",mrna_sequence)
print("Aminoacid =", ' - '.join(amino_acid_sequence))