# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422854800.726911
_enable_loop = True
_template_filename = 'C:\\Dev\\Intex2\\CHF\\CHF\\templates/ManageUsers.html'
_template_uri = 'ManageUsers.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['listTitle', 'form', 'bottomList', 'list']


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
        def list():
            return render_list(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
        def bottomList():
            return render_bottomList(context._locals(__M_locals))
        def listTitle():
            return render_listTitle(context._locals(__M_locals))
        User = context.get('User', UNDEFINED)
        listForm = context.get('listForm', UNDEFINED)
        def form():
            return render_form(context._locals(__M_locals))
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


def render_form(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        User = context.get('User', UNDEFINED)
        listForm = context.get('listForm', UNDEFINED)
        def form():
            return render_form(context)
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


"""
__M_BEGIN_METADATA
{"line_map": {"128": 11, "129": 13, "107": 15, "68": 3, "135": 129, "74": 3, "80": 21, "122": 11, "88": 21, "89": 24, "90": 24, "91": 30, "92": 31, "93": 32, "94": 33, "95": 37, "27": 0, "101": 15, "43": 1, "48": 5, "113": 9, "53": 13, "120": 9, "121": 10, "58": 17, "123": 11, "124": 11, "125": 11, "126": 11, "127": 11}, "uri": "ManageUsers.html", "filename": "C:\\Dev\\Intex2\\CHF\\CHF\\templates/ManageUsers.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
