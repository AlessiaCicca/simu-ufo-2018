import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_avvistamenti(self, e):
        anno=self._view.dd_anno.value
        if anno is None:
            self._view.create_alert("Selezionare un anno")
        grafo = self._model.creaGrafo( anno)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        for nodo in grafo:
            self._view.dd_stato.options.append(ft.dropdown.Option(
                text=nodo))
        self._view.update_page()
    def handle_sequenza(self, e):
        stato = self._view.dd_stato.value
        if stato is None:
            self._view.create_alert("Selezionare uno stato")
        costo, listaNodi = self._model.getBestPath(stato)
        self._view.txt_result.controls.append(ft.Text(f"La soluzione migliore è costituita da {costo} stati"))
        for nodo in listaNodi:
            self._view.txt_result.controls.append(ft.Text(f"{nodo}"))
        self._view.update_page()

    def handle_analizza(self, e):
        stato=self._view.dd_stato.value
        if stato is None:
            self._view.create_alert("Selezionare uno stato")
        prec,succ,all=self._model.analisi(stato)
        self._view.txt_result.controls.append(ft.Text("PRECEDENTI"))
        for nodo in prec:
            self._view.txt_result.controls.append(ft.Text(f"{nodo}"))
        self._view.txt_result.controls.append(ft.Text("SUCCESSORI"))
        for nodo in succ:
            self._view.txt_result.controls.append(ft.Text(f"{nodo}"))
        self._view.txt_result.controls.append(ft.Text(f"RAGGIUNGIBILI TOTALE {len(all)}"))
        for nodo in all:
          self._view.txt_result.controls.append(ft.Text(f"{nodo}"))
        self._view.update_page()


    def fillDD(self):
        anni=self._model.getAnni
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(
                text=anno))
