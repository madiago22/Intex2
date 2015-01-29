# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422061175.57169
_enable_loop = True
_template_filename = 'C:\\Users\\Carter\\OneDrive\\Programming\\Python\\test_dmp\\CHF\\templates/ManageSaleItems.html'
_template_uri = 'ManageSaleItems.html'
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
        __M_writer('\r\n    Sale Items\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_form(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def form():
            return render_form(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <form action="#" method="POST">\r\n        <table>\r\n            <tr>\r\n                <td> Item Name <input type="text"/></td><a  href="#"><img height="150"src="http://i3.cpcache.com/product/936970557/thomas_paine_historical_mugs.jpg?color=White&height=460&width=460&qv=90"/></a>\r\n\r\n            </tr>\r\n            <tr>\r\n                <td> Item Description <input type="text"/></td>\r\n            </tr>\r\n            <tr>\r\n                <td> Low Price <input type="text"/></td>\r\n            </tr>\r\n            <tr>\r\n                <td> High Price <input type="text"/></td>\r\n            </tr>\r\n        </table>\r\n            <div class="submitBtns">\r\n                <input class="btn btn-primary" value="Update" type="submit"/>\r\n                <input class="btn btn-danger" value="Archive" type="submit"style="margin: 10px;"/>\r\n            </div>\r\n    </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_list(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def list():
            return render_list(context)
        __M_writer = context.writer()
        __M_writer("\r\n    <tr>\r\n        <td>Hand-Crafted Breaches</td>\r\n    </tr>\r\n\r\n    <tr>\r\n        <td>Thomas Payne Mug</td>\r\n    </tr>\r\n\r\n    <tr>\r\n        <td>George Washington's Actual Incisors</td>\r\n    </tr>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Carter\\OneDrive\\Programming\\Python\\test_dmp\\CHF\\templates/ManageSaleItems.html", "line_map": {"65": 3, "27": 0, "38": 1, "71": 21, "43": 5, "77": 21, "48": 19, "83": 7, "53": 43, "89": 7, "59": 3, "95": 89}, "uri": "ManageSaleItems.html"}
__M_END_METADATA
"""
