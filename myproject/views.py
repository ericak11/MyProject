from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'MyProject'}

@view_config(route_name='index', renderer='templates/newpage.pt')
def hello_world(request):
    return {'content':'Hello!'}


@view_config(route_name='calculator', renderer='templates/index.pt', request_method='POST')
def calculator(request):
    first_num = int(request.params['num_one'])
    second_num = int(request.params['num_two'])
    operator = request.params['math']
    if operator == "add":
      sum = first_num + second_num
      operation = "addition"
    elif operator == "subtract":
      sum = first_num - second_num
      operation = "subtraction"
    elif operator == "multiply":
      sum = first_num * second_num
      operation = "multiplication"
    elif operator == "divide":
      sum = float(first_num)/float(second_num)
      operation = "division"

    return {'answer': sum, 'method': operation}
