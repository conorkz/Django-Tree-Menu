# Django Tree Menu

A flexible Django app for creating and rendering dynamic, multi-level tree menus.

## Key Features

- **Template Tag:** Easy integration using the `{% draw_menu 'menu_name' %}` template tag.
- **Customizable:** Expand/collapse behavior based on the selected item.
- **Database-Driven:** Menus are stored in the database for easy management.
- **Admin Integration:** Edit menus using the standard Django admin interface.
- **URL Mapping:** Menu items can link to hardcoded URLs or named URLs.
- **Multiple Menus:** Support for multiple menus on a single page, identified by name.
- **Efficient:** Renders each menu with a single database query.
