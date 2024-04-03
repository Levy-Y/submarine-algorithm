### `Nyelvek`: **[HU]** [[EN](README_en_US.md)]

# Pearlhunt: Egy Python Projekt 3D Gyöngyvadászathoz

A Pearlhunt egy Python-alapú alkalmazás, amely szimulálja 3D térben a gyöngyvadászat folyamatát. Ez a projekt a Tkinter könyvtárat használja a grafikus felhasználói felület (GUI) létrehozásához, a Matplotlib-et a 3D ábrázoláshoz, és a NumPy-t numerikus műveletekhez. Az alkalmazás lehetővé teszi a felhasználóknak, hogy adatokat importáljanak egy fájlból vagy véletlenszerűen generáljanak pontokat, amelyek a 3D térben lévő gyöngyöket jelentik. Ezután egy útkereső algoritmust alkalmaz, amely meghatározza a leghatékonyabb utat a gyöngyök gyűjtéséhez, figyelembe véve értéküket és távolságukat a kiindulási ponttól (az origótól).

## Funkciók

- **3D Ábrázolás**: A Matplotlib segítségével ábrázolja 3D térben a gyöngyöket, lehetővé téve a felhasználók számára a gyöngyök eloszlásának megfigyelését.
- **Adatimportálás**: A felhasználók importálhatnak adatokat egy fájlból, ahol minden sor egy gyöngyöt képvisel a koordinátáival és értékével.
- **Véletlenszerű Pontok Generálása**: Generál egy meghatározott számú véletlenszerű gyöngyöt egy meghatározott tartományban.
- **Algoritmus Végrehajtása**: Végrehajt egy MOHO (Multi-Objective Optimization Heuristic) algoritmust, amely meghatároz egy optimális utat a gyöngyök gyűjtéséhez az értékük és távolságuk alapján.
- **Intelligens MOHO**: A MOHO algoritmus fejlett változata, amely optimalizálja az érték küszöbértékét a maximális gyöngygyűjtés érdekében.
- **Testreszabható Paraméterek**: A felhasználók testreszabhatják a maximális koordinátákat, a gyöngyök minimális és maximális értékeit, a generálandó vagy importálandó gyöngyök számát.

## Algoritmus magyarázat:
[Algoritmus](algorithm_hu-HU.md)

## Telepítés

A Pearlhunt futtatásához győződjön meg róla, hogy a Python telepítve van a rendszerén. Ezután telepítse a szükséges könyvtárakat a pip segítségével:

```batch
pip install matplotlib numpy customtkinter
```
Vagy

```
Futtassa a setup.bat szkriptet, és beállítja az alkalmazás összes szükséges könyvtárát
```

## Használat

1. **Futtassa az Alkalmazást**: Futtassa a Python szkriptet a Pearlhunt GUI elindításához.
2. **Válassza ki az Adatforrást**: Válassza ki, hogy importálja-e az adatokat egy fájlból vagy generálja-e véletlenszerű pontokat.
- **Konfigurálja a Paramétereket**: Állítsa be a maximális koordinátákat, a gyöngyök minimális és maximális értékeit, és a generálandó gyöngyök számát.
3. **Konfigurálja az Algoritmust**: Állítsa be a sebességet és a rendelkezésre álló időt a kívánságainak megfelelően, és döntse el, hogy használja-e az intelligens MOHO-t (az intelligens MOHO alapértelmezetten engedélyezve van).
4. **Indítsa el az Algoritmust**: Kattintson a "Start Algorithm" gombra, hogy futtassa a MOHO algoritmust és vizualizál egy optimális utat a gyöngyök gyűjtéséhez.
5. **Mentés PDF-be**: Továbbá mentheti a gráfot egy .pdf fájlba, ha szeretné.

## Screenshotok a projektről
![Screenshot](https://github.com/Levy-Y/submarine-algorithm/blob/main/ScreenShots/beta-v1.0-release-screenshot.PNG)

## Licensz

Ez a projekt az MIT Licenc alatt áll. Lásd a `LICENSE` fájlt a részletekért.
