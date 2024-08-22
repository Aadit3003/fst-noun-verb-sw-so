# Morphological Analysis of East African languages (so, sw)
Morphological analysis of Somali and Swahili Noun + Verb forms

## File Structure



## Run Commands

## Somali

## Swahili
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


## Somali Rules



## Swahili Analysis
### Noun Rules
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

### Verb Rules
1. The verbs seem to have the following structure
Subject_prefix ^ Tense ^ Object_Prefix ^ Verb_Stem
^ indicates morpheme boundaries
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

