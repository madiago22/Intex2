# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422061187.567221
_enable_loop = True
_template_filename = 'C:\\Users\\Carter\\OneDrive\\Programming\\Python\\test_dmp\\CHF\\templates/ManageAreas.html'
_template_uri = 'ManageAreas.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['listTitle', 'form', 'list']


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
        def listTitle():
            return render_listTitle(context._locals(__M_locals))
        def form():
            return render_form(context._locals(__M_locals))
        def list():
            return render_list(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'listTitle'):
            context['self'].listTitle(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'list'):
            context['self'].list(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'form'):
            context['self'].form(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_listTitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def listTitle():
            return render_listTitle(context)
        __M_writer = context.writer()
        __M_writer('\r\n    Areas\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def form():
            return render_form(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <form action="#" method="POST">\r\n        <table>\r\n            <tr>\r\n                <td> Area Name <input type="text"/></td><a  href="#"><img height="150"src="http://1.bp.blogspot.com/-Rzi4QHyQ1YY/UmIUpMs6XWI/AAAAAAAAAjQ/go3XOJ7rPoM/s320/IMG_0558.jpg"/></a>\r\n            </tr>\r\n            <tr>\r\n                <td> Area Description <input type="text"/></td>\r\n            </tr>\r\n            <tr>\r\n                <td> Place Number <input type="text"/></td>\r\n            </tr>\r\n        </table>\r\n            <div class="submitBtns">\r\n                <input class="btn btn-primary" value="Update" type="submit"/>\r\n                <input class="btn btn-danger" value="Archive" type="submit"style="margin: 10px;"/>\r\n            </div>\r\n    </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_list(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def list():
            return render_list(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <tr>\r\n        <td>Cobler Area</td>\r\n    </tr>\r\n\r\n    <tr>\r\n        <td>Treat/Refreshment Stand</td>\r\n    </tr>\r\n\r\n    <tr>\r\n        <td>Constitution Recitation</td>\r\n    </tr>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Carter\\OneDrive\\Programming\\Python\\test_dmp\\CHF\\templates/ManageAreas.html", "line_map": {"65": 3, "27": 0, "38": 1, "71": 21, "43": 5, "77": 21, "48": 19, "83": 7, "53": 39, "89": 7, "59": 3, "95": 89}, "uri": "ManageAreas.html"}
__M_END_METADATA
"""
