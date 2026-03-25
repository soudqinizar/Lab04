import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def check(self, e):
        self._view.print.controls.clear()

        try:
            testo = self._view.textfield.value
            lingue = self._view.lingue.value
            ricerca = self._view.ricerca.value
        except:
            self._view.print.controls.append(ft.Text("ERRORE", color="red"))
            self._view.print.controls.append(ft.Text(f"ERRORE {self._view.textfield.value} , {self._view.lingue.value}, {self._view.ricerca.value}", color="red"))
            self._view.update()
            return

        if testo == "":
            self._view.print.controls.append(ft.Text(f"Inserire un testo valido", color="red"))
            self._view.update()
            return
        if lingue == None:
            self._view.print.controls.append(ft.Text(f"Seleziona una lingua", color="red"))
            self._view.update()
            return
        if ricerca == None:
            self._view.print.controls.append(ft.Text(f"Seleziona un tipo di ricerca", color="red"))
            self._view.update()
            return

        errori, tempo= self.handleSentence(testo, lingue, ricerca)

        self._view.print.controls.append(
            ft.Row([
                ft.Text("Il testo da verificare è:"),
                ft.Text(testo, color=ft.colors.BLUE)
            ])
        )

        if errori == " - ":
            self._view.print.controls.append(
                ft.Row([
                    ft.Text("Non ci sono parole errate.", color="green"),
                ])
            )
        else:
            self._view.print.controls.append(
                ft.Row([
                    ft.Text("Le Parole Errate sono:"),
                    ft.Text(errori, color=ft.colors.RED)
                ])
            )
        self._view.lingue.value = ""
        self._view.ricerca.value = ""
        self._view.textfield.value = ""
        self._view.update()


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text