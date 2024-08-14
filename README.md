# Brachy-Vector-Calculator
ESTRO 2024 Submission - Accepted

Creates Patient and Treatment objects in order to better represent the data. 

A given treatment is made up of a dosage to the tumour and each of the surrounding organs. Good treatments give a high dose to the tumour while trying to minimise the dosage to the surrounding organs - too low a dose to the tumour and the treatment is ineffective and too high a dose to the surrounding organs and the patient will not survive. 

After getting an experienced oncologist to rank a series of treatments depending on how good they beleived them to be, I tried to recreate these results just by looking at a transforming the data in some way. 

After some data analysis, we found that turning the each treatment (dose to tumour and each organ) into a vector, where all values reained the same except the dose to the tumour (if the tumour received a dose of x units, we replaced its value with 130 - x). We then found that the magnitude of the resulting vector had an inverse correlation to the effectiveness of the plan which the oncologist gave. 

This Python script finds Euclidean distances of vectors of doses of brachytherapy a patient recieves and then uses them to compare the effectivenss of different treatments.

The final poster that was submitted and accepted at ESTRO 2024 is also in the repository.
