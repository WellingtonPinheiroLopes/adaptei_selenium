from lib.modules.vision.suitsConnect import (
    test_connectDate,
    test_searchActiveStatus,
    test_searchActiveStatusWithPlans,
    test_searchForActiveStatusWithMonthlyPlans,
    test_searchForInactiveStatusWithMonthlyPlans,
    test_searchForIncompleteStatusWithMonthlyPlans,
    test_searchForOpenStatusWithMonthlyPlans,
    test_searchInactiveStatus,
    test_searchInactiveStatusWithPlans,
    test_searchIncompleteStatus,
    test_searchIncompleteStatusWithPlans,
    test_searchOpenStatus,
    test_searchOpenStatusWithPlans,
    test_searchForActiveStatusAnnuallPlans,
    test_searchForIncompleteStatusWithAnnualPlans,
    test_searchForOpenStatusWithAnnualPlans,
    test_searchForInactiveStatusWithAnnualPlans,
  
    
)


def test_runningAllVisionConnectTests():
    test_connectDate()
    test_searchActiveStatus()
    test_searchIncompleteStatus()
    test_searchOpenStatus()
    test_searchInactiveStatus()
    ####
    test_searchActiveStatusWithPlans()
    test_searchIncompleteStatusWithPlans()
    test_searchOpenStatusWithPlans()
    test_searchInactiveStatusWithPlans()
    ####
    test_searchForActiveStatusWithMonthlyPlans()
    test_searchForIncompleteStatusWithMonthlyPlans()
    test_searchForOpenStatusWithMonthlyPlans()
    test_searchForInactiveStatusWithMonthlyPlans()
    ####
    test_searchForActiveStatusAnnuallPlans()
    test_searchForIncompleteStatusWithAnnualPlans()
    test_searchForOpenStatusWithAnnualPlans()
    test_searchForInactiveStatusWithAnnualPlans()
  
    