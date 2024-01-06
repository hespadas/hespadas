odoo.define('garbage_collection_points.GoogleMapsWidget', function (require) {
    "use strict";

    const FieldChar = require('web.basic_fields').FieldChar;
    const fieldRegistry = require('web.field_registry');

    const GoogleMapsWidget = FieldChar.extend({
        template: null,

        _renderReadonly: function () {
            this.$el.html('<iframe src="' + this.value + '" width="100%" height="450" frameborder="0" style="border:0;" allowfullscreen="true"></iframe>');
        },

        _renderEdit: function () {
            this.$el.html('<input type="text" class="o_field_char o_field_widget" value="' + this._formatValue(this.value) + '"/>');
        },
    });

    fieldRegistry.add('google_maps', GoogleMapsWidget);

    return GoogleMapsWidget;
});