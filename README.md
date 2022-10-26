TestcasesProgram.py inneholder en metode som returnerer True / False basert på om året som skrives inn er et skuddår / ikke et skuddår.
TestcasesTesting.py tar alle conditions som finnes i TestcasesProgram.py metoden og tester dem individuelt med flere variabler ved bruk av pytest.mark.parametrize.
Prosjektmappen lastes opp til repository og Github Actions er konfigurert til å kjøre når det er noe som pushes til repository.
Github Actions installerer pytest ved å bruke requirements.txt som er en del av prosjektmappen.
