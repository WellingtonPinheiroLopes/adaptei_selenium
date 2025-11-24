from libraries.date.date import finalPeriod, initialPeriod
from libraries.date.text import proPlans
from libraries.date.time import oneSeconds
from libraries.date.url import urlConnect
from libraries.elementsHtml.htmlStandard import (
    nzPlaceholder,
    nzSelect,
    placeholder,
    tagDiv,
    tagInput,
    tdNormalizeSpace,
    toLookFor,
)
from libraries.elementsHtml.htmlVisionConnect import (
    ConnectAllPlans,
    connectActiveStatus,
    connectAllIntervals,
    connectAllStatuses,
    connectAnnualInterval,
    connectFineDate,
    connectMonthlyInterval,
    connectStartDate,
    connectStatusInactive,
    connectStatusIncomplete,
    connectStatusOpen,
)
from libraries.language.l_selenium import (
    ClickOnAnHTMLElementContainingText,
    clearHtmlFields,
    expectedTime,
    vistUrl,
    writingInHTMLFieldsContainingText,
)


def connectDate():
    vistUrl(urlConnect)
    expectedTime(oneSeconds)
    ###
    ClickOnAnHTMLElementContainingText(tagInput, placeholder, connectStartDate)
    expectedTime(oneSeconds)
    clearHtmlFields(tagInput, placeholder, connectStartDate)
    expectedTime(oneSeconds)
    writingInHTMLFieldsContainingText(
        tagInput, placeholder, connectStartDate, initialPeriod
    )
    ####
    ClickOnAnHTMLElementContainingText(tagInput, placeholder, connectFineDate)
    expectedTime(oneSeconds)
    clearHtmlFields(tagInput, placeholder, connectFineDate)
    expectedTime(oneSeconds)
    writingInHTMLFieldsContainingText(
        tagInput, placeholder, connectFineDate, finalPeriod
    )
    # expectedTime(oneSeconds)

    ClickOnAnHTMLElementContainingText(tagInput, placeholder, toLookFor)
    expectedTime(oneSeconds)
    #####


def searchStatus(
    status, informStatus, allPlans, informPlans, allIntervals, informIntervals
):

    if status:
        ClickOnAnHTMLElementContainingText(nzSelect, nzPlaceholder, connectAllStatuses)
        ClickOnAnHTMLElementContainingText(tagDiv, tdNormalizeSpace, informStatus)

    if allPlans:
        ClickOnAnHTMLElementContainingText(nzSelect, nzPlaceholder, ConnectAllPlans)
        ClickOnAnHTMLElementContainingText(tagDiv, tdNormalizeSpace, informPlans)

    if allIntervals:
        ClickOnAnHTMLElementContainingText(nzSelect, nzPlaceholder, connectAllIntervals)
        ClickOnAnHTMLElementContainingText(tagDiv, tdNormalizeSpace, informIntervals)


def test_searchActiveStatus():
    connectDate()
    expectedTime(oneSeconds)
    searchStatus(
        status=True,
        informStatus=connectActiveStatus,
        allPlans=False,
        informPlans="",
        allIntervals=False,
        informIntervals="",
    )


def test_searchIncompleteStatus():
    searchStatus(
        status=True,
        informStatus=connectStatusIncomplete,
        allPlans=False,
        informPlans="",
        allIntervals=False,
        informIntervals="",
    )


def test_searchOpenStatus():
    searchStatus(
        status=True,
        informStatus=connectStatusOpen,
        allPlans=False,
        informPlans="",
        allIntervals=False,
        informIntervals="",
    )


def test_searchInactiveStatus():
    searchStatus(
        status=True,
        informStatus=connectStatusInactive,
        allPlans=False,
        informPlans="",
        allIntervals=False,
        informIntervals="",
    )


####


def test_searchActiveStatusWithPlans():
    searchStatus(
        status=True,
        informStatus=connectActiveStatus,
        allPlans=True,
        informPlans=proPlans,
        allIntervals=False,
        informIntervals="",
    )


def test_searchIncompleteStatusWithPlans():
    searchStatus(
        status=True,
        informStatus=connectStatusIncomplete,
        allPlans=True,
        informPlans=proPlans,
        allIntervals=False,
        informIntervals="",
    )


def test_searchOpenStatusWithPlans():
    searchStatus(
        status=True,
        informStatus=connectStatusOpen,
        allPlans=True,
        informPlans=proPlans,
        allIntervals=False,
        informIntervals="",
    )


def test_searchInactiveStatusWithPlans():
    searchStatus(
        status=True,
        informStatus=connectStatusInactive,
        allPlans=True,
        informPlans=proPlans,
        allIntervals=False,
        informIntervals="",
    )


####


def test_searchForActiveStatusWithMonthlyPlans():
    searchStatus(
        status=True,
        informStatus=connectActiveStatus,
        allPlans=True,
        informPlans=proPlans,
        allIntervals=True,
        informIntervals=connectMonthlyInterval,
    )


def test_searchForIncompleteStatusWithMonthlyPlans():
    searchStatus(
        status=True,
        informStatus=connectStatusIncomplete,
        allPlans=True,
        informPlans=proPlans,
        allIntervals=True,
        informIntervals=connectMonthlyInterval,
    )


def test_searchForOpenStatusWithMonthlyPlans():
    searchStatus(
        status=True,
        informStatus=connectStatusOpen,
        allPlans=True,
        informPlans=proPlans,
        allIntervals=True,
        informIntervals=connectMonthlyInterval,
    )


def test_searchForInactiveStatusWithMonthlyPlans():
    searchStatus(
        status=True,
        informStatus=connectStatusInactive,
        allPlans=True,
        informPlans=proPlans,
        allIntervals=True,
        informIntervals=connectMonthlyInterval,
    )


####


def test_searchForActiveStatusAnnuallPlans():
    searchStatus(
        status=True,
        informStatus=connectActiveStatus,
        allPlans=True,
        informPlans=proPlans,
        allIntervals=True,
        informIntervals=connectAnnualInterval,
    )


def test_searchForIncompleteStatusWithAnnualPlans():
    searchStatus(
        status=True,
        informStatus=connectStatusIncomplete,
        allPlans=True,
        informPlans=proPlans,
        allIntervals=True,
        informIntervals=connectAnnualInterval,
    )


def test_searchForOpenStatusWithAnnualPlans():
    searchStatus(
        status=True,
        informStatus=connectStatusOpen,
        allPlans=True,
        informPlans=proPlans,
        allIntervals=True,
        informIntervals=connectAnnualInterval,
    )


def test_searchForInactiveStatusWithAnnualPlans():
    searchStatus(
        status=True,
        informStatus=connectStatusInactive,
        allPlans=True,
        informPlans=proPlans,
        allIntervals=True,
        informIntervals=connectAnnualInterval,
    )
