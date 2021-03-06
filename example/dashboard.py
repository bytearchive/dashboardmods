from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from admin_tools.dashboard import Dashboard
from admin_tools.dashboard import modules
from dashboardmods import get_memcache_dash_modules, get_rss_dash_modules, get_varnish_dash_modules


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for twtv3.
    """ 
    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)

        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            title=_('Quick links'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                {
                    'title': _('Return to site'),
                    'url': '/',
                },
                {
                    'title': _('Change password'),
                    'url': reverse('admin:password_change'),
                },
                {
                    'title': _('Log out'),
                    'url': reverse('admin:logout')
                },
            ]
        ))

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            title=_('Applications'),
            exclude_list=('django.contrib',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.AppList(
            title=_('Administration'),
            include_list=('django.contrib',),
        ))

        # # append a recent actions module
        # self.children.append(RecentActionsDashboardModule(
        #     title=_('Recent Actions'),
        #     limit=5
        # ))
        # 
        # # append a feed module
        # self.children.append(FeedDashboardModule(
        #     title=_('Latest Web Development Activities'),
        #     feed_url='http://www.pivotaltracker.com/user_activities/de98454d195bc113ba489ff01ae2673a',
        #     limit=5
        # ))
        
        self.children.extend(get_memcache_dash_modules())
        self.children.extend(get_varnish_dash_modules())
        self.children.extend(get_rss_dash_modules())
    
    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        pass
