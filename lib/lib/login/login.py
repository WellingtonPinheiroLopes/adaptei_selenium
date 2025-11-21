from lib.date.text import toEnter , selectcompany
from lib.date.url import accessAdaptei
from lib.date.user import dPassword, dUser
from lib.html.htmlLogin import password, username
from lib.html.htmlStandard import button, tagId, tagInput , tagSpan
from lib.date.time import oneSeconds
from lib.language.l_selenium import (
    ClickOnAnHTMLElementContainingText,
    vistUrl,
    writingInHTMLFieldsContainingTextTypeId,
    expectedTime
)


def login():
    vistUrl(accessAdaptei)
    writingInHTMLFieldsContainingTextTypeId(tagInput, tagId, username, dUser)
    writingInHTMLFieldsContainingTextTypeId(tagInput, tagId, password, dPassword)
    ClickOnAnHTMLElementContainingText(button, toEnter)
    expectedTime(oneSeconds)
    ClickOnAnHTMLElementContainingText(tagSpan , selectcompany)


