---
title: R : Variance Inflation
tags: R, stats
date: 2015-07-18

---

This is my note on swirl course Regression Model : Overfitting and Underfitting.

## Definition
<!-- BEGIN_SUMMARY -->
A variance inflation factor (VIF) is a ratio of estimated variances, the variance due to including the ith regressor, divided by that due to including a corresponding ideal regressor which is uncorrelated with the others.
VIF is the square of standard error inflation.

<!-- END_SUMMARY -->
More simply, it estimates how much the variance of a coefficient is "inflated" because of linear dependence with other predictors. Thus, a VIF of 1.8 tells us that the variance of a particular coefficient is 80% larger than it would be if that predictor was completely uncorrelated with all the other predictors.  
The VIF has a lower bound of 1 but no upper bound. 


## Examples with the swiss dataset
To explore VIF, we'll use the Swiss Fertility and Socioeconomic Indicators (1888) dataset which reports standardized fertility measure and socio-economic indicators for each of 47 French-speaking provinces of Switzerland at about 1888. 

```r
data(swiss)
head(swiss)
```

We fit a model with Fertility as outcome and use the R's function vif (from the car package) to compute variance inflations:
```r
data(swiss)
head(swiss)
mdl <- lm(Fertility ~ ., data = swiss)
library(car)
vif(mdl)
```

```
##      Agriculture      Examination        Education         Catholic Infant.Mortality 
##         2.284129         3.675420         2.774943         1.937160         1.107542
```

For each regression coefficient, the variance inflation due to including all the others.  
For instance, the variance in the estimated coefficient of Education is 2.774943 times what it might have been if Education were not correlated with the other regressors.  
We can guess that Examination and Education are likely to be correlated, so most of the variance inflation for Education is due to including Examination.


```r
mdl2 <- lm(Fertility ~ . - Examination, swiss)
vif(mdl2)
```

```
##      Agriculture        Education         Catholic Infant.Mortality 
##         2.147153         1.816361         1.299916         1.107528
```

As expected, omitting Examination in the model decreased the VIF for Education, from 2.774943 to 1.816361. Notice it has almost no effect on the VIF for Infant Mortality.

Including new variables to a model will increase standard errors of coefficient estimates of other correlated refressors. On the other hand, omitting varaibles results can bias in coefficients of regressors which are correlated with the omitted one.

Analysis of variance (ANOVA) is a useful way to quantify the significance of additional regressors.


```r
fit1 <- lm(Fertility ~ Agriculture, data = swiss)
fit3 <- lm(Fertility ~ Agriculture + Examination + Education, data = swiss)
anova(fit1, fit3)
```

```
## Analysis of Variance Table
## 
## Model 1: Fertility ~ Agriculture
## Model 2: Fertility ~ Agriculture + Examination + Education
##   Res.Df    RSS Df Sum of Sq      F    Pr(>F)    
## 1     45 6283.1                                  
## 2     43 3180.9  2    3102.2 20.968 4.407e-07 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

The null hypothesis is rejected at the 0.001 level based on a right-tailed F test (F value=20.968).  

RSS (Residual sum of squares) are 6283.1 and 3180.9.  
We can check the results with the R's deviance function, which calculate the residual sum of squares:


```r
deviance(fit1)
```

```
## [1] 6283.116
```

```r
deviance(fit3)
```

```
## [1] 3180.925
```

The F statistic is the ratio of the two sums of squares divided by their respective degrees of freedom.  
For the F value computing, this is the ratio of the difference of deviance divided by the difference in the residual degrees of freedom of fit1 and fit3 (2) and the fit3's residual sum of squares divided by its degrees of freedom. fit3 has 43 residual degrees of freedom (47 number of samples - 4 predictors (the 3 named and the intercept)):

```r
n <- (deviance(fit1) - deviance(fit3))/2
d <- deviance(fit3)/43
n/d
```

```
## [1] 20.96783
```
If the two scaled sums are independent and centrally chi-squared distributed with the same variance, the statistic will have an F distribution with parameters given by the two degrees of freedom.

For the p-value is the probability that a value of n/d or larger would be drawn from an F distribution which has parameters 2 and 43. The p-value is 4.407e-07, a very unlikely value if the null hypothesis vwere true.

The p-value can be computed with the R's pf function:

```r
pf(n/d, 2, 43, lower.tail = FALSE)
```

```
## [1] 4.406913e-07
```

Based on the calculated p-value, a false rejection of the null hypothesis is extremely unlikely. We are confident that fit3 is significantly better than fit1, with one caveat: analysis of variance is sensitive to its assumption that model residuals are approximately normal.  
If they are not, we could get a small p-value for that reason.  
It is thus worth testing residuals for normality. The Shapiro-Wilk test tests the residual of fit 3. Normality is its null hypothesis.


```r
shapiro.test(fit3$residuals)
```

```
## 
## 	Shapiro-Wilk normality test
## 
## data:  fit3$residuals
## W = 0.97276, p-value = 0.336
```

The Shapiro-Wilk p-value of 0.336 fails to reject normality, supporting confidence in the analysis of variance.


We can go on with ANOVA and other variables:


```r
fit5 <- lm(Fertility ~ Agriculture + Examination + Education + Catholic, data = swiss)
fit6 <- lm(Fertility ~ Agriculture + Examination + Education + Catholic + Infant.Mortality, data = swiss)
anova(fit1, fit3, fit5, fit6)
```

```
## Analysis of Variance Table
## 
## Model 1: Fertility ~ Agriculture
## Model 2: Fertility ~ Agriculture + Examination + Education
## Model 3: Fertility ~ Agriculture + Examination + Education + Catholic
## Model 4: Fertility ~ Agriculture + Examination + Education + Catholic + 
##     Infant.Mortality
##   Res.Df    RSS Df Sum of Sq       F    Pr(>F)    
## 1     45 6283.1                                   
## 2     43 3180.9  2   3102.19 30.2107 8.638e-09 ***
## 3     42 2513.8  1    667.13 12.9937 0.0008387 ***
## 4     41 2105.0  1    408.75  7.9612 0.0073357 ** 
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```
It appears that each model is a significant improvement on its predecessor.

<!-- 
## Experimenting VIF high values

Regardless of your criterion for what constitutes a high VIF, there are at least three situations in which a high VIF is not a problem and can be safely ignored:

2. The high VIFs are caused by the inclusion of powers or products of other variables.

Sources
http://statisticalhorizons.com/multicollinearity
-->
