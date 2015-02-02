# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422890598.057362
_enable_loop = True
_template_filename = 'C:\\Dev\\Intex2\\CHF\\CHF\\templates/ManageUsers.html'
_template_uri = 'ManageUsers.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['form', 'bottomList', 'list', 'listTitle']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'manage.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        User = context.get('User', UNDEFINED)
        listForm = context.get('listForm', UNDEFINED)
        def list():
            return render_list(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
        def bottomList():
            return render_bottomList(context._locals(__M_locals))
        def form():
            return render_form(context._locals(__M_locals))
        def listTitle():
            return render_listTitle(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'listTitle'):
            context['self'].listTitle(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'list'):
            context['self'].list(**pageargs)
        

        __M_writer('\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bottomList'):
            context['self'].bottomList(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'form'):
            context['self'].form(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def form():
            return render_form(context)
        User = context.get('User', UNDEFINED)
        listForm = context.get('listForm', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n        <form method="POST">\r\n        <table>\r\n                ')
        __M_writer(str(listForm))
        __M_writer('\r\n        </table>\r\n\r\n             <div class="submitBtns">\r\n\r\n\r\n')
        if User =='' :
            __M_writer('                     <input type="submit"class="btn btn-success" name="createButton" value="Create"/>\r\n')
        else:
            __M_writer('                     <a class="resetLink"href="#">Reset Password</a>\r\n                     <input type="submit"class="btn btn-primary" name="updateButton" value="Update" />\r\n                     <input type="submit"class="btn btn-danger archiveBtn" name="archiveButton"value="Archive" style="margin: 10px;"/>\r\n')
        __M_writer('\r\n\r\n            </div>\r\n        </form>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bottomList(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bottomList():
            return render_bottomList(context)
        __M_writer = context.writer()
        __M_writer('\r\n         <a class="btn createBtn" href="/CHF/ManageUsers">Create New</a>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_list(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        def list():
            return render_list(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        for client in users:
            __M_writer('            <tr><td><a href="/CHF/ManageUsers.edit/')
            __M_writer(str(client.id))
            __M_writer('">')
            __M_writer(str(client.user.first_name))
            __M_writer(' ')
            __M_writer(str(client.user.last_name))
            __M_writer('</a> </td></tr>\r\n')
        __M_writer('    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_listTitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def listTitle():
            return render_listTitle(context)
        __M_writer = context.writer()
        __M_writer('\r\n        Users\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"129": 3, "68": 21, "135": 129, "76": 21, "77": 24, "78": 24, "79": 30, "80": 31, "81": 32, "82": 33, "83": 37, "89": 15, "27": 0, "95": 15, "112": 11, "101": 9, "43": 1, "108": 9, "109": 10, "110": 11, "111": 11, "48": 5, "113": 11, "114": 11, "115": 11, "116": 11, "53": 13, "58": 17, "123": 3, "117": 13}, "filename": "C:\\Dev\\Intex2\\CHF\\CHF\\templates/ManageUsers.html", "uri": "ManageUsers.html"}
__M_END_METADATA
"""
