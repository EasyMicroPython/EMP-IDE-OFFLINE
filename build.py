import os

flask_path = os.path.dirname(os.path.realpath(__file__))
flask_html_path = os.path.join(flask_path, 'emp_offline/templates/index.html')
flask_static_path = os.path.join(flask_path, 'emp_offline/static')

vue_path = '../MicroIDE'
vue_html = os.path.join(vue_path, 'dist/index.html')
vue_static = os.path.join(vue_path, 'dist/')


def npm_build(des_path=vue_path):
    os.chdir(des_path)
    os.system('yarn build')
    os.chdir(flask_path)


def del_flask_static(des_path=flask_static_path):
    try:
        os.system('rm -rf ' + des_path)
        print(des_path, 'removed.')
    except:
        pass


def copy_static_to_flask(src_path=vue_static, des_path=flask_static_path):
    os.system('cp -rp ' + src_path + ' ' + des_path)
    print('static files copy done')


def copy_html_to_flask(src_path=vue_html, des_path=flask_html_path):
    os.system('cp -rp ' + src_path + ' ' + des_path)
    print('index.html copy done')


def format_html():
    with open(flask_html_path, 'r') as f:
        raw_html = f.read()

    raw_html_parts = raw_html.split(
        "gtag('config', 'UA-127068587-1');</script>")

    raw_html_head = raw_html_parts[0]

    raw_html_link_parts = raw_html_parts[1].split('<div id=app></div>')[0]
    raw_html_script_parts = raw_html_parts[1].split('<div id=app></div>')[1]

    raw_html_link_parts = raw_html_link_parts.replace(
        'href=/', 'href=\"{{ url_for(\'static\', filename=\'')

    raw_html_link_parts = raw_html_link_parts.replace(' rel=', '\') }}\" rel=')

    raw_html_script_parts = raw_html_script_parts.replace(
        'src=/', 'src=\"{{ url_for(\'static\', filename=\'')

    raw_html_script_parts = raw_html_script_parts.replace(
        '></script>', '\') }}\"></script>')

    formated_html = "%sgtag('config', 'UA-127068587-1');</script>%s<div id=app></div>%s" % (
        raw_html_head, raw_html_link_parts, raw_html_script_parts)

    with open(flask_html_path, 'w') as f:
        f.write(formated_html)


if __name__ == '__main__':
    print(flask_path)
    npm_build()
    del_flask_static()
    copy_html_to_flask()
    copy_static_to_flask()
    format_html()
    print('deploy done.')
