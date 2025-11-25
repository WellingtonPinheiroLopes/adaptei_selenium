from libraries.date.text import selectcompany, toEnter
from libraries.date.time import fiveSeconds, oneSeconds
from libraries.date.url import accessAdaptei
from libraries.date.user import dPassword, dUser
from libraries.elementsHtml.htmlLogin import password, username
from libraries.elementsHtml.htmlStandard import (
    button,
    contains,
    tagId,
    tagInput,
    tagSpan,
)
from libraries.language.l_selenium import (
    ClickingOnHTMLElementsContainingXPHATContais,
    expectedTime,
    vistUrl,
    writingInHTMLFieldsContainingTextTypeId,
)


def loginSystem():
    vistUrl(accessAdaptei)

    writingInHTMLFieldsContainingTextTypeId(tagInput, tagId, username, dUser)
    expectedTime(oneSeconds)
    writingInHTMLFieldsContainingTextTypeId(tagInput, tagId, password, dPassword)
    expectedTime(oneSeconds)
    ClickingOnHTMLElementsContainingXPHATContais(button, contains, toEnter)
    expectedTime(oneSeconds)
    ClickingOnHTMLElementsContainingXPHATContais(tagSpan, contains, selectcompany)
    expectedTime(oneSeconds)
