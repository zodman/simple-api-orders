from invoke import run as local
from fabric import task
from patchwork.transfers import rsync

exclude_dirs = [".git", "node_modules", ".cache", ".github", "db.sqlite3",
                ".env"]


@task
def init_db(ctx):
    local("rm -f db.sqlite3")
    local("python manage.py migrate")
    local("python populate.py")


@task
def test(c):
    local("coverage run manage.py test --failfast -v3")
    local("coverage report -m ")
    local("coverage html")


@task
def deploy(ctx):
    directory_app = "apps/newapp"
    app_name = "newapp"
    local("python manage.py collectstatic --noinput", echo=True)
    local("find . -name '__pycache__' |xargs rm -rf ", echo=True)
    rsync(ctx, ".", directory_app, exclude=exclude_dirs)
    with ctx.cd(directory_app):
        with ctx.prefix(f"source ~/{directory_app}/.env/bin/activate"):
            ctx.run("pip install -r requirements.txt")
            ctx.run("python manage.py migrate")
    ctx.run(f"sudo supervisorctl restart {app_name}")


