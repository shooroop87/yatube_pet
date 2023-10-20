from django.contrib import admin

from configuration.models import Anagrafica, Lesson, Pricelist, Trainer


class AnagraficaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ragione',
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
        'author',
    )
    list_editable = (
        'ragione',
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
        'author',
    )
    empty_value_display = '-empty-'


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'descrizione',
        'costo_base',
        'tipologia_lezione',
        'author',
    )
    list_editable = (
        'nome',
        'descrizione',
        'costo_base',
        'tipologia_lezione',
        'author',
    )
    search_fields = ('nome',)
    list_filter = ('pub_date',)
    empty_value_display = '-empty-'


class PricelistAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome_listino',
        'qta_crediti',
        'validita',
        'validita_giorni',
        'prezzo_finale',
        'tasse',
        'imponibile',
        'prezzi_open',
        'pagamento_online',
        'tipo_vendita',
        'author',
    )
    list_editable = (
        'nome_listino',
        'qta_crediti',
        'validita',
        'validita_giorni',
        'prezzo_finale',
        'tasse',
        'imponibile',
        'prezzi_open',
        'pagamento_online',
        'tipo_vendita',
        'author',
    )
    search_fields = ('nome_listino',)
    list_filter = ('pub_date',)
    empty_value_display = '-empty-'


class TrainerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cognome',
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
        'author',
    )
    list_editable = (
        'cognome',
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
        'author',
    )
    search_fields = ('cognome', 'nome',)
    list_filter = ('pub_date',)
    empty_value_display = '-empty-'


admin.site.register(Anagrafica, AnagraficaAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Pricelist, PricelistAdmin)
