#   Calculating Expected Offspring
'''
Given: Six nonnegative integers, each of which does not exceed 20,000. 
The integers correspond to the number of couples in a population possessing
each genotype pairing for a given factor. In order, the six given integers 
represent the number of couples having the following genotypes:

1.- AA-AA
2.- AA-Aa
3.- AA-aa
4.- Aa-Aa
5.- Aa-aa
6.- aa-aa

Return: The expected number of offspring displaying the dominant phenotype 
in the next generation, under the assumption that every couple has exactly two offspring.
'''
def expected_dominant(AAxAA:int, AAxAa:int, AAxaa:int, AaxAa:int, Aaxaa:int, aaxaa:int)->float:
    offspring = 2
    p_AAxAA = 1
    p_AAxAa = 1
    p_AAxaa = 1
    p_AaxAa = 0.75
    p_Aaxaa = 0.5
    p_aaxaa = 0
    return offspring*((AAxAA*p_AAxAA) + (AAxAa * p_AAxAa) + (AAxaa * p_AAxaa) + (AaxAa * p_AaxAa) + (Aaxaa * p_Aaxaa) + (aaxaa * p_aaxaa))

def main():
    AAxAA = 1
    AAxAa = 0
    AAxaa = 0
    AaxAa = 1
    Aaxaa = 0
    aaxaa = 1
    print(expected_dominant(AAxAA, AAxAa, AAxaa, AaxAa, Aaxaa, aaxaa))
    


if __name__ == "__main__":
    main()