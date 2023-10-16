menu = [{'title': 'Добавить книгу', 'url_name': 'add_book'},
        {'title': 'О сайте', 'url_name': 'about'}, ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)
        context['menu'] = user_menu

        return context
