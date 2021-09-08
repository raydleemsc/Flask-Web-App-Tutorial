#!/usr/bin/python2.7
#from website import create_app as application
#application.debug = True
def application(environ, start_response):
    line_break='<br/>'
    status = '200 OK'
    output = '<h1>Environment Versions</h1>'
    output += line_break
    output += '<ul>'
    output += '<li>'
    output += 'mod_wsgi.version = ' + str(environ['mod_wsgi.version'])
    output += '</li>'
    output += line_break
    output += '<li>'
    output += env_string(environ, 'mod_wsgi.version')
    output += '</li>'
    output += line_break
    output += '</ul>'
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]

def env_string(e,env_var):
    if e.has_key(env_var):
        return env_var + ' = ' + str(e[env_var])