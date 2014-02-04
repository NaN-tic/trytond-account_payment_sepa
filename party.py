#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__metaclass__ = PoolMeta
__all__ = ['Party']


class Party:
    __name__ = 'party.party'
    sepa_creditor_identifier = fields.Char('SEPA Creditor Identifier', size=35)
    sepa_mandates = fields.One2Many('account.payment.sepa.mandate', 'party',
        'SEPA Mandates')
