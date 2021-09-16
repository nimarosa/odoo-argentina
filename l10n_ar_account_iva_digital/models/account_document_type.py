##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields
import logging
_logger = logging.getLogger(__name__)


class L10nLatamDocumentType(models.Model):
    _inherit = "l10n_latam.document.type"

    export_to_digital = fields.Boolean(
        help='Seleccionar para que este documento sea importado en el Libro IVA Digital'
    )
