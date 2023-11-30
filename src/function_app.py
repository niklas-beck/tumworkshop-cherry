import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="http-trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. But who are you?",
             status_code=200
        )


# Add a new function here

@app.route(route="sum")
def sum(req: func.HttpRequest) -> func.HttpResponse:

    a = req.params.get('a')
    b = req.params.get('b')

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return func.HttpResponse(
            f'The values of "a" and "b" are not Integers :(', 
            status_code=400
        )

    if a and b:
        sum_a_b = int(a) + int(b)
        return func.HttpResponse(f"The sum of {a} and {b} is {sum_a_b}")
    else:
        return func.HttpResponse(
             'Please provide two Integers as query parameters for "a" and "b"',
             status_code=200
        )
