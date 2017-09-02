# Classification of Acute Kidney Injury (AKI) using a differential leucocyte count

An asymptomatic rise in serum creatinine is frequently encountered in post kidney transplant
patients, with the most common cause being subclinical infection, acute rejection or CNI
toxicity. As biopsy and culture reports take at least 2-3 days, we study the practicality of a
differential leucocyte count to differentiate between these conditions. Though not confirmatory
we try to assess the practicality of a simple CBC test in transplant patients.

## Using the project on your system

  * Install python 2.x
  * pip install nltk
  * pip install numpy
  * pip install scipy
  * pip install sklearn
  * pip install pandas
  * Run using **python classifier.py** and **python classifier-ratio.py**
  * The script randomises the input for training.
  * The small input size and random function stop us from having a consistent accuracy

## Sample run:

    Mihirs-MacBook-Pro:aki-classification-using-dlc mihirwagle$ python classifier.py

        training time: 0.002 s
        predicting time: 0.0 s

        accuracy = 0.368421052632

    Mihirs-MacBook-Pro:aki-classification-using-dlc mihirwagle$ python classifier-ratio.py

        training time: 0.001 s
        predicting time: 0.0 s

        accuracy = 0.631578947368

## Results

SVM analysis shows no significant association between total leucocyte count, lymphocyte counts(*L*), neutrophil(*N*) and monocyte (*M*) counts (*per mm3*) and the specified classes. However when the script was run to see association between *N/L* and *N/M* and various classes, we see significant results.

## Conclusion

Although not confirmatory, the differential leucocyte count, especially the ratios N/L and N/M,
can help to predict whether an instance of AKI is due to rejection, infection or drug toxicity.

## Limitations of study

  * Small sample size
  * Retrospective study
  * Pre-renal causes (such as diarrhea) not included.
  * Viral infection group like BKV was too small to include in the study.
  * Subset analysis of T cell not done (*As done in most studies in subclinical ejection*)
