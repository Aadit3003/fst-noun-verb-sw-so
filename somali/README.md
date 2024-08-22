# Somali

## Run Commands
Use the following commands to generate the Somali word surface forms from the underlying forms
```
foma -l somali.xfst
read text underlying-forms.txt
compose net
print lower-words > output-surface-forms.txt
```

## Phonological Analysis
I discovered 6 rules while determining the URs (underlying representations) of the Somali verbs and nouns. I named and ordered them as follows:-
1. **Vowel Insertion** \
Any cluster of two consecutive consonants (with the exception of ‘j’ as the first consonant) in the root word have the same vowel inserted between them as the one that precedes this cluster.
(This applies only if the two consonants are word-final or before certain suffixes)

`0 -> V’ /  V’ C _ C [#, taj#, naj#, ta#]`
	

2. **M-N Form Change**\
‘m’ changes to ‘n’ word-finally and before certain suffixes.

`m -> n / _ [#, ta#, taj#, naj#]`

3. **Spirantization**\
Voiced stops become voiced fricatives when they occur between vowels.

`[g, b, d, ɖ] -> [ɣ, β, ð, ʐ] / V _ V`

4. **DT Deletion**\
‘t’ is deleted if it occurs after the voiced stops  ‘d’ or ‘ɖ’

`ta -> a / [d, ɖ] _ `

5. **LNAJ Conversion**\
When ‘l’ is followed by the sequence ‘naj’, the ‘n’ assimilates and becomes an ‘l’

`lnaj -> llaj / _ #`

6. **Sha-ification**\
The sequence ‘lt’ becomes ‘ʃ’ when it occurs before suffixes starting with  ‘a’

`lt -> ʃ / _ [a#, aj#]`

## Morphological Analysis
Somali verbs use the following suffixes:

| Glossing Abbreviation | Suffix Underlying Form |
|-----------------------|:----------------------:|
| SG                    |      0 (No suffix)     |
| SG.DEF                |           -ta          |
| PL                    |           -o           |
| 3SG.MASC              |           -aj          |
| 3SG.FEM               |          -taj          |
| 1PL.PAST              |          -naj          |

Note:
0 is used for empty string here (In the Vowel Insertion Rule)
C stands for Consonant
V stands for Vowel
