---
title: Confusion Matrix
date: 2015-08-12

---

<!-- BEGIN_SUMMARY -->
A confusion matrix, also known as a contingency table or an error matrix or tavle of confusion, is a specific table layout that allows visualization of the performance of an algorithm, typically a supervised learning one (in unsupervised learning it is usually called a matching matrix).

<!-- END_SUMMARY -->
It is a table with two rows and two columns that reports the number of false positives, false negatives, true positives, and true negatives.

For example, for a test that screens people for a given disease, the confusion matrix will be:

![](figure/confusion-matrix-0.png)

with  
x true positives (TP) : the number of sick people correctly identified as sick  
z false positives (FP) : the number of healthy people incorrectly identified as sick  
t true negatives (TN) : the number of healthy people correctly identified as healthy  
y false negatives (FN) : the number of sick people incorrectly identified as healthy  

The following probabilities are associated with the confusion matrix:  

$Sensitivity = Pr\left(positive\ test\ |\ disease\right)$  
$Specificity = Pr\left(negative\ test\ |\ no\ disease\right)$  
$Positive\ Predictive\ Value = Pr\left(disease\ |\ positive\ test\right)$  
$Negative\ Predictive\ Value =  Pr\left(no disease\ |\ negative\ test\right)$  
$Accuracy = Pr\left(correct\ outcome\right)$

which are computed the following way:

$$Sensitivity = \frac{TP}{TP+FN}$$  
$$Specificity = \frac{TN}{FP+TN}$$  
$$Positive\ Predictive\ Value = \frac{TP}{TP+FP}$$  
$$Negative\ Predictive\ Value = \frac{TN}{FN+TN}$$  
$$Accuracy = \frac{TP+TN}{TP+FP+FN+TN}$$  

## Examples

A diagnostic test with sensitivity 67% and specificity 91% is applied to 2030 people to look for a disorder with a population prevalence of 1.48%.

Let's build the associated 2×2 contingency table:

![](figure/confusion-matrix-1.png)

![](figure/confusion-matrix-2.png)


Suppose that we have created a machine learning algorithm that predicts whether a link will be clicked with 99% sensitivity and 99% specificity. The rate the link is clicked is 1/1000 of visits to a website. If we predict the link will be clicked on a specific visit, what is the probability it will actually be clicked?

Let's be 100000 the number of visits:

![](figure/confusion-matrix-3.png)

According to the confusion matrix above, the probability that the link will be actually clicked is 9%.

