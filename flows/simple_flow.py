from prefect import task, Flow


@task
def say_hello():
    print("Hello, World!")


with Flow("My First Flow") as flow:
    say_hello()
flow.register(project_name="simple_flow")
