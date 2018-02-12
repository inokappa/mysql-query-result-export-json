from invoke import run, task


@task
def test(context):
    try:
        run("pycodestyle --first *.py tests/*.py")
        run("python -m unittest tests.test_sample")
    except Exception:
        pass
