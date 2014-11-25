from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'MyProject'}

@view_config(route_name='index', renderer='templates/newpage.pt')
def hello_world(request):
    return {'content':'Hello!'}


@view_config(route_name='calculator', renderer='templates/index.pt', request_method='POST')
def calculator(request):
    return {request: params}
