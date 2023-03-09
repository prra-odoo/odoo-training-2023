from odoo import http

# 3to access static data

# class Controller(http.Controller):
#     @http.route("/estate", auth="public")
#     def index(self, **kw):
#         return http.request.render(
#             "estate.index",
#             {"properties": ["Burj Khalifa", "Taj Mahal", "Red Fort", "Effiel Tower"]},
#         )
# 3 to access stored data


class Controller(http.Controller):
    @http.route(
        ["/properties", "/properties/page/<int:page>"], auth="public", website=True
    )
    def index(self, page=1, **kw):

        Properties = http.request.env["estate.property"]
        total_properties = Properties.search_count([])
        pager = http.request.website.pager(
            url="/properties/",
            total=total_properties,
            page=page,
            step=3,
            url_args=None,
        )
        properties = Properties.search(
            [("state", "in", ["new", "received"])],
            limit=3,
            offset=pager["offset"],
        )

        vals = {"properties": properties, "pager": pager}

        # Properties = http.request.env["estate.property"]
        return http.request.render("estate.index", vals)


class Controller(http.Controller):
    @http.route(
        '/properties/<model("estate.property"):property>/', auth="public", website=True
    )
    def index(self, property, **kw):
        return http.request.render("estate.second_page", {"property": property})


# 7 URl fields


# class Controller(http.Controller):
#     @http.route("/estate/<int:id>", auth="public", website=True)
#     def index(self, id):
#         return "<h1>{} ({}) </h1>".format(id, type(id).__name__)

# # 5 using model converter


# class Controller(http.Controller):
#     @http.route(
#         '/estate/<model("estate.property"):property>', auth="public", website=True
#     )
#     def property(self, property):
#         return http.request.render("estate.property.offer", {"offer": property})
