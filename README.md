# Morphological Analysis of East African languages (so, sw)
Morphological analysis of Somali and Swahili Noun + Verb forms

## File Structure

The files are organized as follows
* somali
  * somali.xfst
  * underlying-forms.txt
  * output-surface-forms.txt
* swahili
  * swahili.lexc
  * swahili.xfst
  * lexical.txt
  * morphemic.txt
  * surface.txt




## Somali

### Run Commands
Use the following commands to generate the Somali word surface forms from the underlying forms
```
foma -l somali.xfst
read text underlying-forms.txt
compose net
print lower-words > output-surface-forms.txt
```

### Morphological Analysis
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


## Swahili
### Run Commands
The following code files that handle both Nouns and Verbs at once:
- `swahili.lexc`
- `swahili.xfst`

I used the following run commands to generate and verify my outputs:
1. To generate the Morphemic and Lexical Forms using the LEXC file
```
lexc swahili.lexc
print upper-words > lexical.txt
print lower-words > morphemic.txt
```
2. To generate the Lexical and Surface Forms using the XFST file
```
source swahili.xfst
print upper-words > lexical.txt
print lower-words > surface.txt
```


### Morphological Analysis

#### Noun Rules
1. The Singular Prefix is [u] which has two allomorphs
  - ‘w’ before vowels
  - ‘u’ otherwise
2. The Plural Prefix is [n] which has several allomorphs
  - ‘n’ becomes ‘ɲ’ before Vowels
  - ‘n’ is deleted before Fricatives (s, f, v, ʃ)
  - ‘n’ is deleted before stops (p, t, k), and the word-initial stops are aspirated
  - If ‘l’ occurs after the prefix ‘n’, it becomes ‘d’. ([n l] -> [n d])
  - ‘n’ becomes ‘ŋ’ before Velars (g)
  - ‘n w’ and ‘n b’’ both become ‘mb’
  - ‘n’ Otherwise (E.g. Dentals (d, z))

The Plural prefix allomorphy seems to be an assimilation of the ‘n’ to the place of articulation of the consonant that comes after the ‘n’.

Clarifications - In the XFST and LEXC files:-
I have used the symbols “th”, “kh”, and “ph” to represent the aspirated characters
The “t͡ʃ” symbol sometimes gives trouble while using ‘apply up’ or ‘apply down’

#### Verb Rules
1. The verbs seem to have the following structure **Subject_prefix ^ Tense ^ Object_Prefix ^ Verb_Stem** (^ indicates morpheme boundaries)
2. The Subject prefixes are

| Pronoun | Tag   | Prefix |
|---------|-------|--------|
| he      | +3SgS | a-     |
| I       | +1SgS | ni-    |
| you     | +2SgS | u-     |
| we      | +1PlS | tu-    |
| they    | +3PlS | wa-    |


3. The Tense prefixes are

| Tense   | Tag   | Prefix |
|---------|-------|--------|
| Future  | +Fut  | ta-    |
| Present | +Pres | na-    |
| Perfect | +Perf | me-    |
| Past    | +Past | li-    |

4. The Object prefixes are
   
| Pronoun | Tag   | Prefix |
|---------|-------|--------|
| him     | +3SgO | m-     |
| me      | +1SgO | ni-    |
| you     | +2SgO | ku-    |
| us      | +1PlO | tu-    |
| them    | +3PlO | wa-    |


5. Finally, the “tu-” prefix (+1PlS) gets aspirated word-initially to “tʰu”.

