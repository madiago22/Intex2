# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422084951.963217
_enable_loop = True
_template_filename = 'C:\\Users\\Carter\\OneDrive\\Programming\\Python\\test_dmp\\CHF\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    \r\n    <title>Colonial Heritage</title>\r\n    \r\n')
        __M_writer('      <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n      <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css" rel="stylesheet">\r\n      <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\r\n      <link rel="icon" type = "image/x-icon" href="http://img.freeflagicons.com/thumb/star_icon/united_states_of_america/united_states_of_america_640.png">\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n  \r\n  </head>\r\n  <body>\r\n  <div id="topNav">\r\n\r\n  </div>\r\n    <div id="wrapper">\r\n\r\n        <table>\r\n<!-- BANNER -->\r\n        <tbody>\r\n        <tr id="banner">\r\n\r\n           <td colspan="2">\r\n               <h2 id="title">The Colonial Heritage Foundation</h2>\r\n               <div id="brBanner">\r\n\r\n                 <div class="input-group" id="searchBar">\r\n                  <span class="input-group-btn">\r\n                    <button class="btn btn-default" type="button">Go!</button>\r\n                  </span>\r\n                  <input type="text" class="form-control" placeholder="Search for...">\r\n                </div>\r\n\r\n               <div id="login">\r\n                    <button class="btn btn-primary loginBtn"  >Login</button>\r\n                   <a href="#">Create an Account</a>\r\n               </div>\r\n\r\n             </div>\r\n           </td>\r\n\r\n        </tr>\r\n\r\n<!-- SIDEBAR -->\r\n\r\n        <tr id="middle">\r\n            <td id="sidebar">\r\n\r\n                 <div class="sidebar">\r\n                     <!-- OLD BOOTSTRAP SIDEBAR\r\n                    <ul class="nav nav-pills nav-stacked">\r\n                      <li  role="presentation" ><a href="/CHF/index">Home</a></li>\r\n                      <li  role="presentation"><a href="/CHF/about">About</a></li>\r\n                      <li role="presentation"><a href="/CHF/Contact">Contact</a></li>\r\n                      <li  role="presentation"><a href="/CHF/Terms">Terms</a></li>\r\n                    </ul>\r\n                    -->\r\n                   <ul class="navbar">\r\n                      <li id="home" class="screenNav" role="presentation" ><a href="#">Home</a></li>\r\n                      <li id="store" role="presentation"><a href="#">Store</a>\r\n                        <ul class="subNav">\r\n                            <li id="sales"><a href="#">Sales</a></li>\r\n                            <li id="rentals"><a href="#">Rentals</a></li>\r\n                        </ul>\r\n                      </li>\r\n                      <li id="contact" class="screenNav"role="presentation"><a href="#">Contact</a></li>\r\n                      <li id="terms" role="presentation"><a href="#">Terms</a></li>\r\n                   </ul>\r\n\r\n\r\n                </div>\r\n            </td>\r\n\r\n\r\n\r\n\r\n\r\n\r\n<!-- CONTENT -->\r\n\r\n           <td id="content">\r\n               <div id="homeScreen">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n                </div>\r\n                <div id="contactScreen">\r\n                     <p>This is the contact Screen</p>\r\n                </div>\r\n           </td>\r\n\r\n\r\n\r\n       </tr>\r\n\r\n<!-- FOOTER -->\r\n        <tr  id="footer">\r\n           <td colspan="2">\r\n                <ul class="footerNav">\r\n                  <li id="aboutBtn" role="presentation"><a href="/CHF/about">About</a></li>\r\n                  <li id="contactBtn" role="presentation"><a href="/CHF/Contact">Contact</a></li>\r\n                  <li id="termsBtn" role="presentation"><a href="/CHF/Terms">Terms</a></li>\r\n               </ul>\r\n\r\n\r\n\r\n\r\n           </td>\r\n        </tr>\r\n        </tbody>\r\n        </table>\r\n    </div>\r\n<!-- LOGIN FORM -->\r\n<div id="loginPage">\r\n    <span class="glyphicon glyphicon-remove remove-icon"></span>\r\n    <h2>Welcome</h2>\r\n   <div id="formSecion">\r\n    <form id="loginForm" action="#" method="POST">\r\n       <p>Username: <input type="text"/></p>\r\n        <p>Password:  &nbsp<input type="password"/></p>\r\n        <input type="submit" id="loginSubmit" class="btn btn-success"value="Login">\r\n    </form>\r\n       <a href="#" style="color:#0f51ac;margin-top:20px; font-size:10px;">Forgot Password?</a>\r\n    </div>\r\n</div>\r\n\r\n\r\n\r\n\r\n')
        __M_writer('        ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n\r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Carter\\OneDrive\\Programming\\Python\\test_dmp\\CHF\\templates/base.htm", "line_map": {"33": 5, "34": 15, "35": 20, "36": 20, "37": 20, "42": 96, "43": 142, "44": 142, "45": 142, "16": 4, "18": 0, "51": 94, "57": 94, "27": 2, "28": 4, "29": 5, "63": 57}, "source_encoding": "ascii", "uri": "base.htm"}
__M_END_METADATA
"""
