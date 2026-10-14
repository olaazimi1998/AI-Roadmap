def bayes_therom(prior, likelihood, evidence):
    """ 
    P(A|B) = P(B|A) * P(A) / P(B)
    """ 


    posterior = (likelihood * prior) / evidence

    return posterior


    #prior = P(Fraud)

    #likelihood = P(NewDevice | Fraud)

    #evidence  = P(NewDevice)

    #posterior = P(Fraud | NewDevice)