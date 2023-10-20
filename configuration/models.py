from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Anagrafica(models.Model):
    ragione = models.TextField(
        verbose_name='Ragione sociale',
        blank=True,
        null=True,
    )
    attivita = models.TextField(
        verbose_name='Tipo attività svolta',
        blank=True,
        null=True,
    )
    indirizzo = models.TextField(
        verbose_name='Indirizzo:',
        blank=True,
        null=True,
    )
    civico = models.TextField(
        verbose_name='Civico:',
        blank=True,
        null=True,
    )
    comune = models.TextField(
        verbose_name='Comune:',
        blank=True,
        null=True,
    )
    provincia = models.TextField(
        verbose_name='Provincia:',
        blank=True,
        null=True,
    )
    cap = models.TextField(
        verbose_name='CAP:',
        blank=True,
        null=True,
    )
    email = models.TextField(
        verbose_name='Email:',
        blank=True,
        null=True,
    )
    telefono_fisso = models.TextField(
        verbose_name='Telefono Fisso:',
        blank=True,
        null=True,
    )
    telefono_cellulare = models.TextField(
        verbose_name='Telefono Cellulare:',
        blank=True,
        null=True,
    )
    partita_iva = models.TextField(
        verbose_name='Partita Iva:',
        blank=True,
        null=True,
    )
    codice_fiscale = models.TextField(
        verbose_name='Codice Fiscale:',
        blank=True,
        null=True,
    )
    regime_fiscale = models.TextField(
        verbose_name='Regime Fiscale:',
        blank=True,
        null=True,
    )
    codice_palestra = models.TextField(
        verbose_name='Codice Palestra Registrazione:',
        blank=True,
        null=True,
    )
    referente = models.TextField(
        verbose_name='Referente',
        blank=True,
        null=True,
    )
    abbveviativo = models.TextField(
        verbose_name='Abbreviativo contratto',
        blank=True,
        null=True,
    )
    nome_app = models.TextField(
        verbose_name='Nome sull applicativo',
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='anagrafica',
        verbose_name='Автор',
        help_text='Автор',
        null=True
    )

    class Meta:
        verbose_name = 'Anagrafica'
        verbose_name_plural = 'Anagrafiche'


class Lesson(models.Model):
    nome = models.CharField(
        max_length=23,
        verbose_name='Nome corso ( max 23 caratteri )',
        help_text='Inserisci il nome del corso (Pilates, Yoga, ecc..)'
    )
    descrizione = models.TextField(
        verbose_name='Descrizione',
        help_text='Inserisci una rapida descrizione massimo 50 parole',
        blank=True,
        null=True
    )
    costo_base = models.CharField(
        max_length=100,
        verbose_name='Costo base del corso:',
        help_text='1',
    )
    tipologia_lezione = models.CharField(
        verbose_name='Tipologia Lezione:',
        max_length=10,
        choices=(
            ('Gruppo', 'Gruppo'),
            ('Privata', 'Privata'),
        )
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data creazione del corso',
        help_text='Data si crea in automatico'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='lessons',
        verbose_name='Автор',
        help_text='Автор',
        null=True,
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Corso'
        verbose_name_plural = 'Corsi'


class Trainer(models.Model):
    cognome = models.TextField(
        verbose_name='Cognome',
        help_text='Cognome'
    )
    nome = models.TextField(
        verbose_name='Nome',
        help_text='Nome'
    )
    ragione = models.TextField(
        verbose_name='Ragione sociale',
        blank=True,
        null=True,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data inserimento',
        help_text='Data inserimento'
    )
    indirizzo = models.TextField(
        verbose_name='Indirizzo:',
        blank=True,
        null=True,
    )
    civico = models.TextField(
        verbose_name='Civico:',
        blank=True,
        null=True,
    )
    comune = models.TextField(
        verbose_name='Comune:',
        blank=True,
        null=True,
    )
    provincia = models.TextField(
        verbose_name='Provincia:',
        blank=True,
        null=True,
    )
    cap = models.TextField(
        verbose_name='CAP:',
        blank=True,
        null=True,
    )
    email = models.TextField(
        verbose_name='Email:',
        blank=True,
        null=True,
    )
    telefono_fisso = models.TextField(
        verbose_name='Telefono Fisso:',
        blank=True,
        null=True,
    )
    telefono_cellulare = models.TextField(
        verbose_name='Telefono Cellulare:',
        blank=True,
        null=True,
    )
    codice_fiscale = models.TextField(
        verbose_name='Codice Fiscale:',
        blank=True,
        null=True,
    )
    partita_iva = models.TextField(
        verbose_name='Partita Iva:',
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='trainers',
        verbose_name='Автор',
        help_text='Автор',
        null=True,
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Istruttore'
        verbose_name_plural = 'Istruttori'


class Pricelist(models.Model):
    nome_listino = models.TextField(
        verbose_name='Nome listino',
        help_text='Nome listino'
    )
    qta_crediti = models.TextField(
        verbose_name='Quantità Crediti',
        help_text='Quantità Crediti'
    )
    validita = models.TextField(
        verbose_name='Validitá',
        help_text='Validitá',
        blank=True,
        null=True,
    )
    validita_giorni = models.TextField(
        verbose_name='Validitá in giorni',
        help_text='Validitá in giorni'
    )
    prezzo_finale = models.TextField(
        verbose_name='Prezzo finale',
        blank=True,
        null=True,
    )
    tasse = models.TextField(
        verbose_name='Tasse',
        blank=True,
        null=True,
    )
    imponibile = models.TextField(
        verbose_name='Imponibile',
        blank=True,
        null=True,
    )
    prezzi_open = models.TextField(
        verbose_name='Listino prezzi OPEN',
        blank=True,
        null=True,
    )
    pagamento_online = models.CharField(
        verbose_name='Pagamento Online',
        max_length=2,
        choices=(
            ('Si', 'Si'),
            ('No', 'No'),
        )
    )
    tipo_vendita = models.CharField(
        verbose_name='Tipo Vendita',
        max_length=20,
        choices=(
            ('Acquisto signolo', 'Acquisto signolo'),
            ('Abbonamento mensile', 'Abbonamento mensile'),
        )
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data inserimento',
        help_text='Data inserimento'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='pricelists',
        verbose_name='Автор',
        help_text='Автор',
        null=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Listino Prezzi'
        verbose_name_plural = 'Listino Prezzi'
