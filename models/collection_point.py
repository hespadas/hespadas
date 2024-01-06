from odoo import models, fields, api
import werkzeug
import logging

_logger = logging.getLogger(__name__)


class WasteCollectionPoint(models.Model):
    _name = "collection.point"
    _description = "Waste Collection Point"

    name = fields.Char(string="Name", required=True)
    street_name = fields.Char(string="Street")
    house_number = fields.Char(string="Number")
    street_district = fields.Char(string="District")
    street_postal_code = fields.Char(string="Postal Code")
    waste_type = fields.Many2one(
        "waste.type", string="Waste Type", help="Type of waste collected at the point."
    )
    telephone = fields.Char(string="Telephone Number")
    email = fields.Char(string="Email")
    daily_limit = fields.Integer(
        string="m³ Daily Limit",
        help="Maximum number of waste units that can be collected per day.",
    )
    opening_hours = fields.Text(string="Opening Hours")
    google_maps_url = fields.Char(
        string="Google Maps URL", compute="_compute_google_maps_url"
    )

    def _get_api_key(self):
        api_key = (
            self.env["ir.config_parameter"].sudo().get_param("google_maps_api_key")
        )
        if not api_key:
            _logger.warning("Google Maps API key not found")
        return api_key

    @api.depends("street_name", "house_number", "street_district", "street_postal_code")
    def _compute_google_maps_url(self):
        api_key = self._get_api_key()
        if not api_key:
            self.google_maps_url = False
            return
        BASE_URL = "https://www.google.com/maps/embed/v1/place"
        address_parts = filter(
            None,
            [
                self.street_name,
                self.house_number,
                self.street_district,
                self.street_postal_code,
            ],
        )
        address_full = ", ".join(address_parts)

        if not address_full.strip():
            self.google_maps_url = False
            return

        query = werkzeug.urls.url_encode({"key": api_key, "q": address_full})
        self.google_maps_url = f"{BASE_URL}?{query}"
