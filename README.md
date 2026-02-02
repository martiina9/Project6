# 🧪 Automatické testy – Playwright & Pytest

Tento repozitář obsahuje **automatické end-to-end testy** webové stránky  🌐 [Playwright](https://playwright.dev)

Testy jsou napsané v **Pythonu** pomocí knihoven **Playwright** a **Pytest** a slouží jako ukázka základního automatizovaného testování webových aplikací.

---

## 🔧 Použité technologie

- 🐍 Python  
- 🧪 Pytest  
- 🎭 Playwright (Sync API)

---

## 📝 Seznam testů

| Test | Popis | 
|------|-------|
| `test_title` | Ověří, že titulek stránky obsahuje "Playwright" | 
| `test_get_started` | Klikne na "Get Started" a přejde na úvodní stránku dokumentace |
| `test_search_shows_results` | Vyhledá "locators" a ověří, že výsledky obsahují slovo "locators" | 
| `test_theme_choice` | Přepne téma stránky mezi dark/light a ověří změnu | 
| `test_playwright_submenu` | Najde a rozbalí submenu "Playwright Test", zkontroluje první položku, přes logo se vrátí na hlavní stránku |   


Byli vyžadované 3 automatické testy - 2 přidané navíc pro lepší ukázku práce s Playwright

---

## ▶️ Jak testy spustit

### 1️⃣ Naklonuj repo
### 2️⃣ Vytvoř a aktivuj virtuální prostředí

```bash
python3 -m venv nazev_prostredi
source nazev_prostredi/bin/activate #Linux, macOS
nazev_prostredi\Scripts\activate #Windows
```
### 3️⃣ Nainstaluj requirements.txt
```
pip install pytest playwright
playwright install
```
### 4️⃣ Naimportuj knihovny 
### 4️⃣ Spuštění testů

- Testy se spouštějí přímo v termináli
- Spouštíme pomocí pytest -s, protože testy obsahují i print()
- Výsledky i s vypsaným print() se objeví v termináli
```
python3 -m pytest -s
```
---
### 🧠 Co testy ověřují

- správné načtení stránky
- navigaci mezi stránkami
- práci s lokátory
- reakci aplikace na uživatelské akce
- viditelnost a existenci prvků v UI

---

## 🔧 Poznámky

- Testy jsou psané pomocí **sync API Playwrightu**.  
- Každý test obsahuje **docstring**, který vysvětluje, co test kontroluje.  
- `expect(...).to_have_url()` používá **regex**, takže URL může obsahovat drobné variace.  

