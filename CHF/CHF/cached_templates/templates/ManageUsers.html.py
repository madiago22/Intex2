# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422839471.015497
_enable_loop = True
_template_filename = 'C:\\Dev\\Intex2\\CHF\\CHF\\templates/ManageUsers.html'
_template_uri = 'ManageUsers.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['form', 'listTitle', 'list']


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
        def form():
            return render_form(context._locals(__M_locals))
        listForm = context.get('listForm', UNDEFINED)
        def list():
            return render_list(context._locals(__M_locals))
        def listTitle():
            return render_listTitle(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'listTitle'):
            context['self'].listTitle(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'list'):
            context['self'].list(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'form'):
            context['self'].form(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        listForm = context.get('listForm', UNDEFINED)
        def form():
            return render_form(context)
        __M_writer = context.writer()
        __M_writer('\r\n        <form method="POST">\r\n        <table>\r\n\r\n                ')
        __M_writer(str(listForm))
        __M_writer('\r\n        </table>\r\n\r\n             <div class="submitBtns">\r\n                 <a class="resetLink"href="#">Reset Password</a>\r\n                <input type="submit"class="btn btn-primary" name="updateButton" value="Update" />\r\n                <input type="submit"class="btn btn-danger" name="archiveButton"value="Archive" style="margin: 10px;"/>\r\n            </div>\r\n        </form>\r\n    ')
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


def render_list(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def list():
            return render_list(context)
        users = context.get('users', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"line_map": {"67": 17, "68": 21, "69": 21, "75": 3, "109": 103, "81": 3, "87": 9, "27": 0, "94": 9, "95": 10, "96": 11, "97": 11, "98": 11, "99": 11, "100": 11, "101": 11, "102": 11, "103": 13, "40": 1, "45": 5, "50": 13, "60": 17}, "uri": "ManageUsers.html", "filename": "C:\\Dev\\Intex2\\CHF\\CHF\\templates/ManageUsers.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
