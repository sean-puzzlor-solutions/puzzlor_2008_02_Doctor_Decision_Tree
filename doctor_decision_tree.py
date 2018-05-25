def doctor_decision_tree():
    # The cost to go to the doctor and have the test is $200 and the cost of a penicillin prescription is $50.
    c_doctor = 200
    c_penicillin = 50

    # The chance of the illness being a cold is 50%, flu is 20%, and bacterial is 30%.
    # The test results also match these ratios.
    p_cold = .5
    p_flu = .2
    p_bacteria = .3

    # If the test indicates that it is a cold, then there is a 80% likelihood that it is a cold.
    # If the test indicates a flu virus, then there is a 90% likelihood that it is the flu.
    # If the test indicates that it is bacterial, then there is a 95% likelihood that it is a bacterial illness.
    p_test_cold = .8
    p_test_flu = .9
    p_test_bacterial = .95
    # The alternative outcomes are evenly divided among the likelihood balance.

    # If the illness is a cold then you will miss 5 days of work which is a cost to you of $500.
    c_cold = 500
    # If the illness is the flu then you will miss 8 days of work at a cost to you of $800.
    c_flu = 800
    # If the illness is bacterial and is not treated you will miss 12 days of work at a cost of $1200.
    c_bacterial = 1200
    # If you correctly treat the bacterial illness you will only miss 2 days of work at a cost of $200.
    c_treatment = 200

    # decisions
    # Not going to the doctor
    c_not_going_to_the_doc = p_cold * c_cold + p_flu * c_flu + p_bacteria * c_bacterial
    print("Cost of not going to the doctor : ", c_not_going_to_the_doc)

    # Not going to the doctor, but buying penicillin
    c_penicillin_no_doc = (p_cold * c_cold + p_flu * c_flu + p_bacteria * c_treatment) + c_penicillin
    print("Cost of not going to the doctor, but buying penicillin : ", c_penicillin_no_doc)

    # Going to the doctor, choosing treatment if bacterial only
    c_going_to_the_doc_treat = c_doctor
    c_going_to_the_doc_treat += p_cold*((p_test_cold*c_cold)
                                        + (((1-p_test_cold)/2)*c_flu)
                                        + (((1-p_test_cold)/2)*c_bacterial))
    c_going_to_the_doc_treat += p_flu*(p_test_flu*c_flu
                                       + (((1 - p_test_flu)/2) * c_cold)
                                       + (((1 - p_test_flu)/2) * c_bacterial))
    c_going_to_the_doc_treat += p_bacteria * ((p_test_bacterial * c_treatment
                                              + (((1 - p_test_bacterial)/2) * c_cold)
                                              + (((1 - p_test_bacterial)/2) * c_flu)) + c_penicillin)
    print("Cost of going to the doctor, buying penicillin : ", c_going_to_the_doc_treat)

    # Going to the doctor, choosing treatment for all
    c_going_to_the_doc_treat_all = c_doctor + c_penicillin
    c_going_to_the_doc_treat_all += p_cold * ((p_test_cold * c_cold)
                                              + (((1 - p_test_cold) / 2) * c_flu)
                                              + (((1 - p_test_cold) / 2) * c_bacterial))
    c_going_to_the_doc_treat_all += p_flu * (p_test_flu * c_flu
                                             + ((1 - p_test_flu) * c_cold) / 2
                                             + ((1 - p_test_flu) * c_bacterial) / 2)
    c_going_to_the_doc_treat_all += p_bacteria * ((p_test_bacterial * c_treatment
                                                   + ((1 - p_test_bacterial) * c_cold / 2)
                                                   + ((1 - p_test_bacterial) * c_flu / 2)))
    print("Cost of going to the doctor, buying penicillin all the time : ", c_going_to_the_doc_treat_all)

    # Going to the doctor, never choosing treatment for all bacterial only
    c_going_to_the_doc_treat_none = c_doctor
    c_going_to_the_doc_treat_none += p_cold * ((p_test_cold * c_cold)
                                               + (((1 - p_test_cold) / 2) * c_flu)
                                               + (((1 - p_test_cold) / 2) * c_bacterial))
    c_going_to_the_doc_treat_none += p_flu * (p_test_flu * c_flu
                                              + ((1 - p_test_flu) * c_cold) / 2
                                              + ((1 - p_test_flu) * c_bacterial) / 2)
    c_going_to_the_doc_treat_none += p_bacteria * ((p_test_bacterial * c_bacterial
                                                    + ((1 - p_test_bacterial) * c_cold / 2)
                                                    + ((1 - p_test_bacterial) * c_flu / 2)))
    print("Cost of going to the doctor, no penicillin all the time : ", c_going_to_the_doc_treat_none)

    # Going to the doctor, choosing treatment for cold, bacterial
    c_going_to_the_doc_treat_cold = c_doctor
    c_going_to_the_doc_treat_cold += p_cold * ((p_test_cold * c_cold)
                                               + (((1 - p_test_cold) / 2) * c_flu)
                                               + (((1 - p_test_cold) / 2) * c_treatment) + c_penicillin)
    c_going_to_the_doc_treat_cold += p_flu * (p_test_flu * c_flu
                                              + ((1 - p_test_flu) * c_cold) / 2
                                              + ((1 - p_test_flu) * c_bacterial) / 2)
    c_going_to_the_doc_treat_cold += p_bacteria * ((p_test_bacterial * c_treatment
                                                    + ((1 - p_test_bacterial) * c_cold / 2)
                                                    + ((1 - p_test_bacterial) * c_flu / 2)) + c_penicillin)
    print("Cost of going to the doctor, buying penicillin for cold, bacterial : ", c_going_to_the_doc_treat_cold)

    # Going to the doctor, choosing treatment for cold, flu
    c_going_to_the_doc_treat_flus = c_doctor
    c_going_to_the_doc_treat_flus += p_cold * ((p_test_cold * c_cold)
                                               + (((1 - p_test_cold) / 2) * c_flu)
                                               + (((1 - p_test_cold) / 2) * c_bacterial))
    c_going_to_the_doc_treat_flus += p_flu * ((p_test_flu * c_flu
                                              + ((1 - p_test_flu) * c_cold) / 2
                                              + ((1 - p_test_flu) * c_treatment) / 2) + c_penicillin)
    c_going_to_the_doc_treat_flus += p_bacteria * ((p_test_bacterial * c_treatment
                                                    + ((1 - p_test_bacterial) * c_cold / 2)
                                                    + ((1 - p_test_bacterial) * c_flu / 2)) + c_penicillin)
    print("Cost of going to the doctor, buying penicillin for cold, flu : ", c_going_to_the_doc_treat_flus)


if __name__ == '__main__':
    doctor_decision_tree()
