from lib.date.text import toEnter
from lib.date.url import accessAdaptei
from lib.date.user import dPassword, dUser
from lib.html.htmlLogin import password, username
from lib.html.htmlStandard import button, tagId, tagInput
from lib.language.l_selenium import (
    ClickOnAnHTMLElementContainingText,
    vistUrl,
    writingInHTMLFieldsContainingTextTypeId,
)


def login():
    vistUrl(accessAdaptei)
    writingInHTMLFieldsContainingTextTypeId(tagInput, tagId, username, dUser)
    writingInHTMLFieldsContainingTextTypeId(tagInput, tagId, password, dPassword)
    ClickOnAnHTMLElementContainingText(button, toEnter)
