from libraries.date.plans import NumberOfMessages, automated, plans, priceData
from libraries.date.time import fiveSeconds, halfAsecond, oneSeconds
from libraries.date.url import urlConnect
from libraries.elementsHtml.htmlStandard import (
    alt,
    button,
    contains,
    id,
    img,
    nzSelect,
    save,
    tagDiv,
    tagInput,
    tdNormalizeSpace,
)
from libraries.elementsHtml.htmlVisionPlans import (
    Plan,
    askCustomer,
    interval,
    messageMonth,
    monthlyInterval,
    newPlan,
    paymentMethod,
    price,
    visibleId,
    visibleYes,
)
from libraries.language.l_selenium import (
    ClickingOnHTMLElementsContainingXPHATContais,
    ClickOnAnHTMLElementContainingText,
    clickOnSpecificHTMLElement,
    vistUrl,
    writingInHTMLFieldsContainingText,
)


def baseRegisterNewPlans(
    informPlans,
    reportMonthlyMessage,
    reportInterval,
    informPrice,
    pleaseSpecifyMonthRrYear,
    visibleYesOrNo,
):
    vistUrl(urlConnect)
    ClickOnAnHTMLElementContainingText(img, alt, plans)
    clickOnSpecificHTMLElement(newPlan)
    writingInHTMLFieldsContainingText(tagInput, id, Plan, informPlans)
    writingInHTMLFieldsContainingText(tagInput, id, messageMonth, reportMonthlyMessage)
    ClickOnAnHTMLElementContainingText(nzSelect, id, interval)
    ClickOnAnHTMLElementContainingText(tagDiv, tdNormalizeSpace, reportInterval)
    writingInHTMLFieldsContainingText(tagInput, id, price, informPrice)
    ClickOnAnHTMLElementContainingText(nzSelect, id, paymentMethod)
    ClickOnAnHTMLElementContainingText(
        tagDiv, tdNormalizeSpace, pleaseSpecifyMonthRrYear
    )
    ClickOnAnHTMLElementContainingText(nzSelect, id, visibleId)
    ClickOnAnHTMLElementContainingText(tagDiv, tdNormalizeSpace, visibleYesOrNo)
    ClickingOnHTMLElementsContainingXPHATContais(button, contains, save)


def test_CreatingMonthlyPlansAskingTheClientVisibleYes():
    baseRegisterNewPlans(
        automated, NumberOfMessages, monthlyInterval, priceData, askCustomer, visibleYes
    )
