from website import create_app as application
#def application(environ, start_response):
#    status = '200 OK'
#    output = str(environ['mod_wsgi.version'])
#    response_headers = [('Content-type', 'text/plain'),
#                        ('Content-Length', str(len(output)))]
#    start_response(status, response_headers)
#    return [output]
