# Morphological and Phonological Analysis of East African languages (so, sw)
Morphological and Phonological analysis of 2 East African languages - Somali and Swahili. The Somali list of underlying forms contains 135 words (both nouns and verbs), and the Swahili list of lexeme forms contains 452 words (52 nouns, 400 verbs). We use FOMA and LEXC scripts to write the Finite State Transducers for both languages.

## File Structure

The files are organized as follows
* somali
  * somali.xfst - The xfst script with the morphophonological rules for Somali nouns and verbs
  * underlying-forms.txt - The list of 135 underlying forms
  * output-surface-forms.txt - The list of 135 surface forms of the Somali words (output of the FOMA script)
* swahili
  * swahili.lexc - The lexc FST with the morphophonotactics for Swahili nouns and verbs
  * swahili.xfst - The xfst script with the morphophonological rules for Swahili nouns and verbs
  * lexical.txt - The lexical forms of 452 Swahili words (52 Nouns and 400 Verbs)
  * morphemic.txt - The morpheme (boundaries indicated) of these 452 Swahili words (output of the LEXC script)
  * surface.txt - The surface forms of the 452 Swahili words (output of the FOMA script)
* utilities
  * diff.py - Python program to compare txt files (line by line) and report differences
 


## Somali

### Run Commands
Use the following commands to generate the Somali word surface forms from the underlying forms
```
foma -l somali.xfst
read text underlying-forms.txt
compose net
print lower-words > output-surface-forms.txt
```

### Phonological Analysis
- Refer to the following [README](https://github.com/Aadit3003/fst-noun-verb-sw-so/tree/c43d6eeb1d84769d7dd163b3532fdba53af3e3b7/somali) for a details on the 6 Somali Phonological rules I used.
- Refer to the following [FOMA script](https://github.com/Aadit3003/fst-noun-verb-sw-so/blob/c43d6eeb1d84769d7dd163b3532fdba53af3e3b7/somali/somali.xfst) for the Somali Finite State Transducer.

## Swahili
### Run Commands
To generate the Morphemic and Lexical Forms using the LEXC file
```
lexc swahili.lexc
print upper-words > lexical.txt
print lower-words > morphemic.txt
```
To generate the Lexical and Surface Forms using the XFST file
```
source swahili.xfst
print upper-words > lexical.txt
print lower-words > surface.txt
```


### Morphological + Phonological Analysis
- Refer to the following [README](https://github.com/Aadit3003/fst-noun-verb-sw-so/blob/e7f386f1b5df79c68062287f6b90b2de540be7da/swahili/README.md) for a details on the Swahili Morphological and Phonological rules I used.
- Refer to the following [LEXC script](https://github.com/Aadit3003/fst-noun-verb-sw-so/blob/e7f386f1b5df79c68062287f6b90b2de540be7da/swahili/swahili.lexc) for the Swahili Morphological Finite State Transducer.
- Refer to the following [FOMA script](https://github.com/Aadit3003/fst-noun-verb-sw-so/blob/e7f386f1b5df79c68062287f6b90b2de540be7da/swahili/swahili.xfst) for the Swahili Phonological Finite State Transducer.

