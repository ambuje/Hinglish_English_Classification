# Hinglish_English_Classification
Language Identification for Code-Mixed Language.
It classifies hinglish and english words using RNN
Created a Deep Learning Model on *Keras* for identifying language.
The pretrained model works for Hindi and English Code-mixed language. But the model can be modified for other languages as well.
<br>

Accuracy of the model is about 90%

To Run the code please visit my [Azure Notebooks](https://notebooks.azure.com/shreyanse081/projects/langclass).

This project is the part of a Bigger project of [Roman to devnagri Conversion]().

## Code-Mixed
Code-mixing is the mixing of two or more languages or language varieties in speech. Some people use the terms "code-mixing" and "code-switching" interchangeably, especially in studies of syntax, morphology, and other formal aspects of language. 
For Example:
"ye repository bhasha phechanne ke liye banai gai hai."
Which actually translates to:
"this repository is made for language identification."
<br>

## Pretrained Model
Pretrained Weight file(.h5) and Model File(.json) can be found in the folder. To use it, just download the .h5 file and .json file and Give the appropriate path in the program.
<br>

## Dataset
There are two files, one is '.csv' (Created) and another is '.tsv' (Orignal). The '.csv' file is created upon '.tsv' file by us. 
<br>

## Libraries
<ul>
  <li>Python v3.6</li>
  <li>Keras v2.1.5</li>
</ul>
