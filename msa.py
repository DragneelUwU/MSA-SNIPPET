def pairwise_alignment(seq1, seq2, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
    alignment = ""
    alignment_score = 0

    for base1, base2 in zip(seq1, seq2):
        if base1 == base2:
            alignment += "|"  # Match
            alignment_score += match_score
        elif base1 == '-' or base2 == '-':
            alignment += " "   # Gap
            alignment_score += gap_penalty
        else:
            alignment += "."  # Mismatch
            alignment_score += mismatch_penalty

    return alignment, alignment_score

def multiple_sequence_alignment(*sequences, **alignment_params):
    num_sequences = len(sequences)
    
    for i in range(num_sequences - 1):
        for j in range(i + 1, num_sequences):
            seq1 = sequences[i]
            seq2 = sequences[j]
            
            alignment, alignment_score = pairwise_alignment(seq1, seq2, **alignment_params)

            print(f"Alignment between sequence {i+1} and sequence {j+1}:")
            print(seq1)
            print(alignment)
            print(seq2)
            print(f"Alignment Score: {alignment_score}")
            print()

# Example usage:
seq1 = "ATGTGAGC"
seq2 = "ATAGGCTA"
sequence3 = "ATCGGTTA"
sequence4 = "ATGCTAGCTAGATCGAT"

multiple_sequence_alignment(seq1, seq2, sequence3, sequence4)



for i in range(10):
    print(i)