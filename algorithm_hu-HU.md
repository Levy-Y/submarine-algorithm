# Az algoritmus a következőképpen működik:

1. Az összes gyöngy közül kiválasztja azokat, amelyeknek az értéke eléri a moho_min értéket.
2. A kiindulópontot (origo) hozzáadja az útvonalhoz.
3. Amíg vannak értékes gyöngyök, a legközelebbi gyöngyöt választja ki, és hozzáadja az útvonalhoz, feltéve, hogy a rendelkezésre álló távolság elegendő a gyöngy eléréséhez és a kiindulópontba való visszatéréshez.
4. Ha a rendelkezésre álló távolság nem elegendő a következő gyöngy eléréséhez és a kiindulópontba való visszatéréshez, a tengeralattjáró visszatér a kiindulópontba.

# Smart MOHO:
1. MOHO-t használja alapul
2. A moho_min értékét változtatja, és az eredmények alapján, a legnagyobb gyöngyértéket biztosító útvonalat választja ki, majd jeleníti meg.