# Conditional Probability 

* The probability of an even occurring, assuming one or more event has already ocurred 
	* Probability of Y given that X has already ocurred. 

* Two events, A and B, are considered to be independent if event A has no effect on the probability of event B. 
	* P(B|A) = P(B)

* If events A and B are not independent, consider the probability that both events have ocurred. 
	* The intersection of events A and B 
	* P(A ∩ B) = P(B|A) * P(A) 

#### Conditional Probability 
```
	P(B|A) = P(A ∩ B) / P(A) 
```

#### Bayes' Theorem 

* Let A and B be two events s.t. P(A|B) is the occurrence of A ocurring given that B has occurred and that P(B|A) is the occurence of B given that A has occurred. 

```
P(A|B) = P(B|A) * P(A) / P(B) 

       = P(B|A) * P(A) / P(B|A) * P(A) + P(B|A') * P(A')
```

