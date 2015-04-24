import ckan.plugins as p
import ckan.plugins.toolkit as tk


class CommentingPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IActions)
    # IConfigurer

    def update_config(self, config):
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')
        tk.add_resource('fanstatic', 'commenting')

    def get_actions(self):
        actions = {'comment_create': action.comment_create,
                   'comment_delete': action.comment_delete,
                   'comment_get': action.comment_get,
                   'comment_show': action.comment_show,
                  }
        return actions
