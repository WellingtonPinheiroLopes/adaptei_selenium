import unittest

import HtmlTestRunner

from libraries.date.plans import NumberOfMessages, automated, plans, priceData
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
    closeSystem,
    vistUrl,
    writingInHTMLFieldsContainingText,
)
from libraries.login.login import loginSystem


class TestMinhaFuncao(unittest.TestCase):
    def setUp(self):
        loginSystem()

    def _baseRegisterNewPlans(
        self,
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
        writingInHTMLFieldsContainingText(
            tagInput, id, messageMonth, reportMonthlyMessage
        )
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

    def test_CreatingMonthlyPlansAskingTheClientVisibleYes(self):
        self._baseRegisterNewPlans(
            automated,
            NumberOfMessages,
            monthlyInterval,
            priceData,
            askCustomer,
            visibleYes,
        )

    closeSystem()


if __name__ == "__main__":
    # Gera o relatório HTML em um diretório 'html_report'
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="html_report"))
