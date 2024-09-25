JAZZMIN_SETTINGS = {
    'site_title': 'E-commerce',

    'site_header': 'E-commerce',

    'site_brand': 'E-commerce',

    # 'site_logo': '',

    # 'login_logo': '',

    'site_logo_classes': 'img-circle',

    # 'site_icon': '',

    'welcome_sign': 'E-commerce',

    'copyright': 'E-commerce',

    'search_model': [],

    'user_avatar': None,

    # 'topmenu_links': [
    #     {'name': 'Home', 'url': 'admin:index', 'permissions': ['auth.view_user']},
    #     {'model': 'auth.User'},
    #     {'app': 'Post'}
    # ],

    'usermenu_links': [
        {'model': 'auth.User'}
    ],

    'show_sidebar': True,

    'navigation_expanded': True,

    'hide_apps': [],

    'hide_models': [],

    # 'order_with_respect_to': ['auth', 'Post'],

    # 'custom_links': {
    #     'Post': [
    #         {
    #             'name': 'Make messages',
    #             'icon': 'fas fa-comments',
    #             'permissions': ['Post']
    #         }
    #     ]
    # },

    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.User': 'fas fa-user',
        'auth.Group': 'fas fa-users',
        'main.Category': 'fas fa-solid fa-list',
        'main.Clothing': 'fas fa-solid fa-vest',
        'main.ClothingImage': 'fas fa-solid fa-image',
    },

    'default_icon_parents': 'fas fa-chevron-circle-right',

    'default_icon_children': 'fas fa-circle',

    'related_modal_active': True,

    'custom_css': None,

    'custom_js': None,

    'use_google_fonts_cdn': True,

    'show_ui_builder': False,

    'changeform_format': 'horizontal_tabs',

    # 'changeform_format_overrides': {'auth.User': 'collapsible', 'auth.Group': 'vertical_tabs'},

    # 'language_chooser': True
}