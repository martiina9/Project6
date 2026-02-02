# 🎭 Playwright Python Testy

Automatizované UI testy pro [Playwright](https://playwright.dev/) dokumentaci pomocí **Pythonu** a **Playwrightu**.  

✨ **Testované funkce:** navigace, vyhledávání, přepínání témat (dark/light), submenu a návrat přes logo.

---

## 📝 Seznam testů

| Test | Popis | 
|------|-------|
| `test_title` | Ověří, že titulek stránky obsahuje "Playwright" | 
| `test_get_started` | Klikne na "Get Started" a přejde na úvodní stránku dokumentace |
| `test_search_shows_results` | Vyhledá "locators" a ověří, že jsou výsledky | 
| `test_theme_choice` | Přepne téma stránky mezi dark/light a ověří změnu | 
| `test_playwright_submenu` | Rozbalí submenu "Playwright Test" a zkontroluje první položku | 
| `test_logo_navigation` | Klikne na logo "Playwright" a vrátí se na hlavní stránku | 

---

## 🚀 Jak spustit testy

1. Otevři projekt v IDE podporující Python a Playwright (např. VS Code).  
2. Ujisti se, že máš nainstalovaný **Python**, **pytest** a **Playwright**.  
3. Spusť testy přímo z IDE nebo přes GitHub Actions:  
   - Testy ověřují navigaci, vyhledávání, submenu a přepínání témat.  
4. Výsledky testů se zobrazí přímo v konzoli nebo v GitHub Actions workflow.

---

## 🔧 Poznámky

- Testy jsou psané pomocí **synchronous API Playwrightu**.  
- Každý test obsahuje **docstring**, který vysvětluje, co test kontroluje.  
- `expect(...).to_have_url()` používá **regex**, takže URL může obsahovat drobné variace.  

---

## 🌟 Přispívání

1. Forkni tento repozitář  
2. Vytvoř novou větev: `feature/moj-test`  
3. Napiš své testy  
4. Pošli pull request  

---

