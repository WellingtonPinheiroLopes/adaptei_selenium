from lib.date.text import selectcompany, toEnter
from lib.date.time import oneSeconds
from lib.date.url import accessAdaptei
from lib.date.user import dPassword, dUser
from lib.html.htmlLogin import password, username
from lib.html.htmlStandard import button, tagId, tagInput, tagSpan , tdNormalizeSpace
from lib.language.l_selenium import (
    ClickOnAnHTMLElementContainingText,
    expectedTime,
    vistUrl,
    writingInHTMLFieldsContainingTextTypeId,
)


def login():
    vistUrl(accessAdaptei)
    writingInHTMLFieldsContainingTextTypeId(tagInput, tagId, username, dUser)
    writingInHTMLFieldsContainingTextTypeId(tagInput, tagId, password, dPassword)
    ClickOnAnHTMLElementContainingText(button, tdNormalizeSpace , toEnter)
    expectedTime(oneSeconds)
    ClickOnAnHTMLElementContainingText(tagSpan, tdNormalizeSpace , selectcompany)
