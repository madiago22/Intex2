# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422060578.202765
_enable_loop = True
_template_filename = 'C:\\Users\\Carter\\OneDrive\\Programming\\Python\\test_dmp\\CHF\\templates/ManageUsers.html'
_template_uri = 'ManageUsers.html'
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
        def form():
            return render_form(context)
        __M_writer = context.writer()
        __M_writer('\r\n        <form action="#" method="POST">\r\n        <table>\r\n\r\n                <tr>\r\n\t\t\t\t\t<td> First Name <input type="text"/></td>\r\n                    <td class="pictureCell" > <a  href="#"><img height="150"src="https://marriottschool.byu.edu/msmadmin/securefile/empphoto/?file=b0%2F5352.jpg"/></a></td>\r\n\t\t\t\t</tr>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<td> Last Name <input type="text"/></td><td> Address <input type="text"/></td>\r\n\t\t\t\t</tr>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<td> City <input type="text"/></td><td> State <input type="text"/></td>\r\n\t\t\t\t</tr>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<td> Zip <input type="text"/></td><td> Email <input type="text"/></td>\r\n\t\t\t\t</tr>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<td> Security Question <input type="text"/></td><td> Security Answer <input type="text"/></td>\r\n\t\t\t\t</tr>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<td> Client Type <input type="text"/></td><td> Phone Number <input type="text"/></td>\r\n\t\t\t\t</tr>\r\n\r\n        </table>\r\n\r\n             <div class="submitBtns">\r\n                 <a class="resetLink"href="#">Reset Password</a>\r\n                <input class="btn btn-primary" value="Update" type="submit"/>\r\n                <input class="btn btn-danger" value="Archive" type="submit"style="margin: 10px;"/>\r\n            </div>\r\n        </form>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_list(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def list():
            return render_list(context)
        __M_writer = context.writer()
        __M_writer('\r\n        <tr>\r\n            <td>Carter Hesterman</td>\r\n        </tr>\r\n         <tr>\r\n            <td>Sam Lucero</td>\r\n        </tr>\r\n         <tr>\r\n            <td>Trevor Jones</td>\r\n        </tr>\r\n         <tr>\r\n            <td>Parish Hansen</td>\r\n        </tr>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Carter\\OneDrive\\Programming\\Python\\test_dmp\\CHF\\templates/ManageUsers.html", "line_map": {"48": 22, "64": 3, "82": 9, "27": 0, "70": 26, "38": 1, "88": 9, "58": 3, "43": 5, "76": 26, "94": 88}, "uri": "ManageUsers.html"}
__M_END_METADATA
"""
