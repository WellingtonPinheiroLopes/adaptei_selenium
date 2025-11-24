from libraries.date.text import selectcompany, toEnter
from libraries.date.time import oneSeconds
from libraries.date.url import accessAdaptei
from libraries.date.user import dPassword, dUser
from libraries.elementsHtml.htmlLogin import password, username
from libraries.elementsHtml.htmlStandard import button, tagId, tagInput, tagSpan, tdNormalizeSpace
from libraries.language.l_selenium import (
    ClickOnAnHTMLElementContainingText,
    expectedTime,
    vistUrl,
    writingInHTMLFieldsContainingTextTypeId,
)


def test_loginSystem():
    vistUrl(accessAdaptei)
    writingInHTMLFieldsContainingTextTypeId(tagInput, tagId, username, dUser)
    writingInHTMLFieldsContainingTextTypeId(tagInput, tagId, password, dPassword)
    ClickOnAnHTMLElementContainingText(button, tdNormalizeSpace, toEnter)
    expectedTime(oneSeconds)
    ClickOnAnHTMLElementContainingText(tagSpan, tdNormalizeSpace, selectcompany)
