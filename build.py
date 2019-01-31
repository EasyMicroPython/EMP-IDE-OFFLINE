import os

flask_path = os.path.dirname(os.path.realpath(__file__))
flask_html_path = os.path.join(flask_path, 'emp_ide/templates/index.html')
flask_static_path = os.path.join(flask_path, 'emp_ide/static')

vue_path = '../EMP-IDE'
vue_html = os.path.join(vue_path, 'dist/index.html')
vue_static = os.path.join(vue_path, 'dist/')


def npm_build(des_path=vue_path):
    os.chdir(des_path)
    os.system('npm run build')
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


if __name__ == '__main__':
    print(flask_path)
    npm_build()
    del_flask_static()
    copy_html_to_flask()
    copy_static_to_flask()
    print('deploy done.')
