import pytest
from playwright.sync_api import sync_playwright, Page, expect
import re

#=================== First test ====================
def test_title(page):
    """Check, if the page title contains word Playwright. """

    page.goto("https://playwright.dev")
    title = page.title()
    assert "Playwright" in title

#=================== Second test ====================

def test_get_started(page):
    """Click 'Get Started' and verify navigation to docs intro page."""

    page.goto("https://playwright.dev")
    get_started = page.locator("a.getStarted_Sjon")
    get_started.click()
    expect(page).to_have_url(re.compile(r".*/docs/intro.*"))

#=================== Third test ====================

def test_search_shows_results(page):
    """Find the search input, enter 'locators', and verify the results."""

    page.goto("https://playwright.dev")
    page.locator("span.DocSearch-Button-Placeholder").click()

    search_input = page.locator("input.DocSearch-Input")
    search_input.fill("locators")

    results_container = page.locator(".DocSearch-Dropdown-Container")
    results_container.wait_for(state="visible")

    result_titles = results_container.locator(".DocSearch-Hit-title")
    expect(result_titles).not_to_have_count(0)
    expect(results_container).to_contain_text("locators", ignore_case=True)

#=================== Fourth test ====================

def test_theme_choice(page):
    """Toggle theme from light to dark (or vice versa) and verify."""

    page.goto("https://playwright.dev")
    html = page.locator("html")
    initial_theme = html.get_attribute("data-theme")
    print("Initial theme: ", initial_theme)

    page.locator("button.toggleButton_gllP").click()
    expected_theme = "dark" if initial_theme == "light" else "light"
    expect(html).not_to_have_attribute("data-theme", expected_theme)
    print("New theme: ", expected_theme)

#=================== Fifth test ====================

def test_playwright_submenu(page):
    """
    Navigate to Docs, expand 'Playwright Test' submenu and check the first item.
    Then return to the main page and verify the URL.
    """

    page.goto("https://playwright.dev")
    
    
    page.locator("a.navbar__item.navbar__link[href='/docs/intro']").click()
    expect(page).to_have_url(re.compile(r".*/docs/intro.*"))
    
    
    toggle = page.locator("a.menu__link.menu__link--sublist:has-text('Playwright Test')")
    toggle.wait_for(state="visible")
    toggle.click()
    
    first_subitem = page.locator("a[href='/docs/test-agents']")
    expect(first_subitem).to_be_visible()

    logo = page.locator("b.navbar__title:text('Playwright')")
    logo.click()

    expect(page).to_have_url("https://playwright.dev/")
    

    








