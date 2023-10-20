from django.forms import ModelForm, Textarea

from .models import Anagrafica, Lesson, Pricelist, Trainer


class AnagraficaForm(ModelForm):
    class Meta:
        model = Anagrafica
        fields = ('ragione',
                  'attivita',
                  'indirizzo',
                  'civico',
                  'comune',
                  'provincia',
                  'cap',
                  'email',
                  'telefono_fisso',
                  'telefono_cellulare',
                  'partita_iva',
                  'codice_fiscale',
                  'regime_fiscale',
                  'codice_palestra',
                  'referente',
                  'abbveviativo',
                  'nome_app',
                  )


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ('nome',
                  'descrizione',
                  'costo_base',
                  'tipologia_lezione',
                  )
        widgets = {
            'descrizione': Textarea(attrs={"cols": 80, "rows": 20}),
        }


class TrainerForm(ModelForm):
    class Meta:
        model = Trainer
        fields = ('cognome',
                  'nome',
                  'ragione',
                  'indirizzo',
                  'civico',
                  'comune',
                  'provincia',
                  'cap',
                  'email',
                  'telefono_fisso',
                  'telefono_cellulare',
                  'codice_fiscale',
                  'partita_iva',
                  )


class PricelistForm(ModelForm):
    class Meta:
        model = Pricelist
        fields = ('nome_listino',
                  'qta_crediti',
                  'validita',
                  'validita_giorni',
                  'prezzo_finale',
                  'tasse',
                  'imponibile',
                  'prezzi_open',
                  'pagamento_online',
                  'tipo_vendita',
                  )
