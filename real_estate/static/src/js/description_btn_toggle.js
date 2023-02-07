odoo.define("real_estate", function (require) {
  "use strict";

  var ajax = require("web.ajax");
  var core = require("web.core");
  var _t = core._t;

  $(document).ready(function () {
    $("#hide_button").click(function () {
      $("#field_div").toggle();
    });
  });
});
