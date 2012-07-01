#   Copyright 2012 Sergey Kirillov
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

SASS_STYLE_NESTED = 0
SASS_STYLE_EXPANDED = 1
SASS_STYLE_COMPACT = 2
SASS_STYLE_COMPRESSED = 3


cdef extern from "libsass/sass_interface.h":

    cdef struct sass_options:
        int output_style
        char* include_paths


    cdef struct sass_context:
        char* source_string
        char* output_string
        sass_options options
        int error_status
        char* error_message


    cdef struct sass_file_context:
        char* input_path
        char* output_string
        sass_options options
        int error_status
        char* error_message


    sass_context*   sass_new_context()
    void            sass_free_context(sass_context*)
    int             sass_compile(sass_context*)

    sass_file_context*   sass_new_file_context()
    void            sass_free_file_context(sass_file_context*)
    int             sass_compile_file(sass_file_context*)


class CompileError(Exception): pass

def compile_string(bytes s, include_paths=None, int output_style=SASS_STYLE_NESTED):
    """Compiles SASS string to CSS"""

    include_paths = include_paths or ''
    cdef sass_context* ctx = sass_new_context()
    try:
        ctx.source_string = s
        ctx.options.include_paths = include_paths
        ctx.options.output_style = output_style
        sass_compile(ctx)
        if ctx.error_status:
            raise CompileError(ctx.error_message or 'Unknown compilation error')
        return ctx.output_string
    finally:
        sass_free_context(ctx)


def compile_file(bytes path, include_paths=None, int output_style=SASS_STYLE_NESTED):
    """Compiles SASS file to CSS string"""

    include_paths = include_paths or ''
    cdef sass_file_context* ctx = sass_new_file_context()
    try:
        ctx.input_path = path
        ctx.options.include_paths = include_paths
        ctx.options.output_style = output_style
        sass_compile_file(ctx)
        if ctx.error_status:
            raise CompileError(ctx.error_message or 'Unknown compilation error')
        return ctx.output_string
    finally:
        sass_free_file_context(ctx)        
