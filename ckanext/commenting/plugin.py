import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckanext.commenting.logic import action
from ckanext.commenting.logic import auth


class CommentingPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IActions)
    p.implements(p.IAuthFunctions)
    # IConfigurer

    def update_config(self, config):
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')
        tk.add_resource('fanstatic', 'commenting')

    def get_actions(self):
        return {'comment_create': action.comment_create,
                'comment_delete': action.comment_delete,
                'comment_show': action.comment_show,
                'package_show': action.package_show,  # override to add comment information in to pkg_dict
               }

    def get_auth_functions(self):
        return {'comment_create': auth.comment_create,
                'comment_delete': auth.comment_delete,
                'comment_show': auth.comment_show,
               }
