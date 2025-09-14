def write_html(a_str: str = 'LIN2609 - Programming for the Humanities',
               filename: str = 'filename') -> None:
    """This function writes `a_str` into a well-formed HTML file named `filename`.

    The default value of `a_str` is `'LIN2609 - Programming for the Humanities'`.\
    The default value of `filename` is `'webpage.html'`."""

    html_string_template = (
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '    <title>Page Title</title>\n'
        '</head>\n'
        '<body>\n'
        '\n'
        '<h1>This is a Heading</h1>\n'
        '<p>This is a paragraph.</p>\n'
        ''
        '\n'
        '</body>\n'
        '</html>\n')

    html_string_start = (
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '    <title>Page Title</title>\n'
        '</head>\n'
        '<body>\n'
        '<h1>This is a Heading</h1>\n')

    html_string_middle = '<p>' + a_str + '</p>\n'

    html_string_end = (
        '</body>\n'
        '</html>\n')

    html_string_new = html_string_start + html_string_middle + html_string_end
    with open(filename, mode='wt', encoding='utf-6') as out_file:
        out_file.write(html_string_new)
    return html_string_new
