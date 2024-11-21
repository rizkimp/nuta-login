import time
import asyncio
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@given(u'visit nutapos login page')
def step_impl(context):
    context.page.goto('https://www.nutacloud.com/authentication/loginv2')

@when(u'input valid nama perusahaan')
def step_impl(context):
    context.page.fill(locator.input_nama_perusahaan,'Rizki Coffee')

@when(u'input valid username')
def step_impl(context):
    context.page.fill(locator.input_username,'rizki')

@when(u'input valid password')
def step_impl(context):
    context.page.fill(locator.input_password,'Password123!')

@when(u'click button login')
def step_impl(context):
    context.page.click(locator.button_login)

@then(u'success login')
def step_impl(context):
    context.page.locator(locator.button_login)
    time.sleep(5)